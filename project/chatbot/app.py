from flask import Flask, request, jsonify, render_template
from celery import Celery
from flask_socketio import SocketIO, emit
import torch
from diffusers import StableDiffusionPipeline
import os

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
socketio = SocketIO(app, message_queue='redis://localhost:6379/0')

# 대화 상태를 저장할 변수
chat_state = {
    'stage': 0,
    'hobby': None,
    'memory': None,
    'image_task_id': None
}

# 이미지 생성 함수
@celery.task
def generate_image_task(prompt):
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(model_id)
    pipe = pipe.to(device)

    # 이미지 생성 하이퍼파라미터 조정
    generator = torch.manual_seed(42)  # 재현성을 위한 시드 설정
    image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5, generator=generator).images[0]
    
    image_path = os.path.join('static', 'generated_image.png')
    image.save(image_path)
    socketio.emit('image_generated', {'image_url': f'/{image_path}'}, to='/', namespace='/')
    return image_path

# 취미에 따른 추천 함수
def suggest_hobby_revival(hobby):
    suggestions = {
        '낚시': '지역 낚시 동호회에 가입하거나, 가까운 낚시터를 찾아보세요. 온라인으로 낚시 장비를 구매할 수도 있습니다.',
        '피아노': '피아노 레슨을 받을 수 있는 온라인 플랫폼: Simply Piano, Flowkey',
        '그림 그리기': '유튜브의 무료 그림 강좌, 지역 미술 학원',
        '독서': '좋은 책을 찾기 위한 추천 사이트: Goodreads, 알라딘 서점'
    }
    return suggestions.get(hobby, '인터넷 검색을 통해 관련 자료를 찾아보세요.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = ''

    if chat_state['stage'] == 0:
        response = "과거에 했던 취미를 말해주세요!"
        chat_state['hobby'] = user_input
        chat_state['stage'] = 1
    elif chat_state['stage'] == 1:
        response = f"과거에 {chat_state['hobby']}를 좋아했군요! 기억나는 상황을 설명해 줄래요?"
        chat_state['stage'] = 2
    elif chat_state['stage'] == 2:
        chat_state['memory'] = user_input
        image_prompt = f"{chat_state['memory']} 상황을 그린 이미지"
        try:
            task = generate_image_task.apply_async(args=[image_prompt])
            chat_state['image_task_id'] = task.id
            response = "기억나는 상황을 설명해 줘서 고마워요! 이미지를 생성 중입니다. 잠시만 기다려 주세요..."
        except Exception as e:
            response = f"이미지를 생성하는데 문제가 발생했습니다: {e}"
        chat_state['stage'] = 3
    elif chat_state['stage'] == 3:
        response = "이미지를 생성 중입니다. 잠시만 기다려 주세요... 원하는 주제에 대해 더 이야기해볼까요?"
    elif chat_state['stage'] == 4:
        if "좋아해요" in user_input or "네" in user_input or "응" in user_input:
            suggestion = suggest_hobby_revival(chat_state['hobby'])
            response = f"{chat_state['hobby']}를 다시 해보고 싶다면, {suggestion}"
            chat_state['stage'] = 0  # 대화 상태 초기화
            chat_state['hobby'] = None
            chat_state['memory'] = None
            chat_state['image_task_id'] = None
        else:
            response = "다른 취미를 말해 줄래요?"

    return jsonify({'response': response})

if __name__ == '__main__':
    socketio.run(app, debug=True)
