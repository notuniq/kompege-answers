# КЕГЭ Ответы

## Описание

Этот скрипт позволяет получать ответы с сайта **kompege.ru**. 

Вы указываете ссылку на вариант, а скрипт обрабатывает данные и выводит ответы к заданиям. Для заданий с видеорешениями также отображаются ссылки на соответствующие видео с таймкодами. 

Пример ссылки:  
```
https://kompege.ru/variant?kim=25059935
```

## Требования

- Python 3.x
- Библиотека `requests` (установить с помощью команды `pip install requests`)

## Использование

1. Вставьте ссылку на вариант в переменную `variant_link` в коде.
2. Запустите скрипт командой `python main.py`.
3. Получите ответы в удобном формате.

## Пример вывода:
```
№1 (101): A
№2 (102): B https://youtu.be/video_id&t=90
№3 (103): C
```

## Обратная связь

Если у вас есть вопросы или предложения, пожалуйста, создайте issue или свяжитесь с автором в Telegram - un1work.t.me.
