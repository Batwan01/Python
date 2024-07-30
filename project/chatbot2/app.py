from flask import Flask, request, render_template_string
from openai import OpenAI

# OpenAI API 키 설정
api_key = 'sk-None-wuFkP3pAQsk3kZy356yZT3BlbkFJaiAIChgbpgQyomE6imuF'

# OpenAI 클라이언트 인스턴스 생성
client = OpenAI(api_key=api_key)


# Flask 애플리케이션 생성
app = Flask(__name__)

# HTML 템플릿
html_template = '''
<!doctype html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .chat-container { max-width: 600px; margin: 50px auto; }
        .chat-box { border: 1px solid #ccc; padding: 10px; border-radius: 5px; }
        .chat-bubble { padding: 10px; border-radius: 10px; margin-bottom: 10px; }
        .chat-bot { background-color: #f0f0f0; text-align: left; }
        .chat-user { background-color: #0084ff; color: white; text-align: right; }
        .chat-input { width: 100%; padding: 10px; margin-top: 10px; }
        .chat-button { width: 100%; padding: 10px; margin-top: 10px; background-color: #0084ff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1>Chatbot</h1>
        <div class="chat-box">
            {% for message in messages %}
                <div class="chat-bubble {{ message['sender'] }}">
                    <p>{{ message['text'] }}</p>
                </div>
            {% endfor %}
        </div>
        <form method="POST">
            <input type="text" name="user_input" class="chat-input" placeholder="메시지를 입력하세요..." required>
            <button type="submit" class="chat-button">보내기</button>
        </form>
        {% if image_url %}
        <h2>생성된 이미지:</h2>
        <img src="{{ image_url }}" alt="Generated Image" style="max-width: 100%;">
        {% endif %}
    </div>
</body>
</html>
'''

# 대화 저장소
messages = []
user_responses = {
    "activity": "",
    "age": "",
    "location": "",
    "companions": "",
    "season": ""
}

@app.route('/', methods=['GET', 'POST'])
def index():
    global messages, user_responses
    image_url = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        messages.append({'sender': 'chat-user', 'text': user_input})

        if len(messages) == 2:
            user_responses["activity"] = user_input
            messages.append({'sender': 'chat-bot', 'text': questions[1]})
        elif len(messages) == 4:
            user_responses["age"] = user_input
            messages.append({'sender': 'chat-bot', 'text': questions[2]})
        elif len(messages) == 6:
            user_responses["location"] = user_input
            messages.append({'sender': 'chat-bot', 'text': questions[3]})
        elif len(messages) == 8:
            user_responses["companions"] = user_input
            messages.append({'sender': 'chat-bot', 'text': questions[4]})
        elif len(messages) == 10:
            user_responses["season"] = user_input
            messages.append({'sender': 'chat-bot', 'text': "설명 고마워요!! 조금만 기다려 주세요!"})

            prompt = f"A {user_responses['age']} year old having fun doing {user_responses['activity']} at a {user_responses['location']} during {user_responses['season']} with {'friends' if '친구' in user_responses['companions'] else 'alone'}."
            
            # OpenAI API 호출
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            
            # response['data'][0]['url']을 사용하여 이미지 URL 추출
            image_url = response.data[0].url
            messages.append({'sender': 'chat-bot', 'text': "이미지가 생성되었습니다!"})
    
    if len(messages) == 0:
        messages.append({'sender': 'chat-bot', 'text': questions[0]})
    
    return render_template_string(html_template, messages=messages, image_url=image_url)

# 챗봇 질문 리스트
questions = [
    "안녕하세요! 과거의 추억, 취미를 말해주세요!",
    "정말 멋져요! 그때의 기억을 구체적으로 설명해 줄 수 있어요? 몇 살이었어요?",
    "고마워요! 어디에서 취미를 즐겼나요?",
    "재미있었겠네요!! 혼자 있었나요?",
    "계절은 언제였나요?",
    "설명 고마워요!! 조금만 기다려 주세요!"
]

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)