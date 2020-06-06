# Сайт типа яндекс афиши

Есть карта, на ней точки- места которые тебе стоило бы посетить. Один минус: это всё прекрыто из-за карантина!
### [ПОСМОТРЕТЬ САЙТ](https://killthebee.github.io/mini_flibusta_part2/pages/index1.html)
![Куда пойти](scr/scr.png)

## Запуск, локально

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте БД командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
