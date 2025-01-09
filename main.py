import requests
import json

variant_link = 'ВСТАВЬТЕ ССЫЛКУ НА ВАРИАНТ СЮДА'

def link(var):
    check = requests.get(f'https://kompege.ru/api/v1/variant/kim/{var}')
    return check

check = link(variant_link)
data = check.json()
k = 1
if 'tasks' in data:
    tasks = data['tasks']
    for task in tasks:
        taskId = task.get('taskId')
        key = task.get('key')
        video = task.get('video')
        timecode = task.get('timecode')
        if not video:
            if key is not None:
                print(f"№{k} ({taskId}):", key)
        else:
            if key is not None:
                print(f"№{k} ({taskId}):", key, f'https://youtu.be/{video}&t={timecode}')
        k += 1
else:
    print("В ответе нет информации о заданиях")
