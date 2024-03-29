# Реализация API для расписания КС ПГУТИ
Данный проект направлен на упрощенние просмотра расписания занятий конкретной группы в конкретный день с помощью VK бота.

* response.py - основной скрипт
* db.py - класс базы данных
* database.sql - дамп базы данных
* bot.py - VK бот

В файле ***response.py*** мы берем всю HTML страницу, которая является одной большой таблицей с множеством строк и столбцов внутри. 
Скрипт ищет и вырезает конкретный фрагмент таблицы, в котором совпадает класс и формирует JSON.

В последствии, элемент обрабатывается VK ботом ***bot.py*** и выводиться пользователю.
В ***db.py*** описан Python-класс, который отвечает за соединение с базой данных, в которой учитывается привязанность пользователя или беседы к группе.

Также присутствует файл **_tokens.py_**, содержащий следующие переменные:
```python
bot_token: str
bot_id: int
```
Он скрыт в .gitignore в целях безопасности, поэтому его нужно создать самостоятельно.

Для запуска бота используется **_bot.py_**. Если требуется сформировать JSON файл с результатом, то можно запустить **_response.py_**, предварительно заменив аргумент в конце файла (комментарием обозначил дополнительные инструкции).