def solution(data, ext, val_ext, sort_by):
    
    dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    answer = sorted(
        [x for x in data if x[dict[ext]] < val_ext],
        key=lambda x: x[dict[sort_by]],
    )
    
    return answer