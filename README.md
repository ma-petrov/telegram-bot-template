# Шаблон телеграм бота

1. На сервере, где выполняется деплой, должен быть ssh-ключ для подключения
к github с сервера.

2. Создать репозиторий бота из шаблона, склонировать.

3. Запустить в локальном репозитории `create.py`, ввести параметры.
Скрипт заполняет шаблоны и удаляется.

4. Добавить секреты в репозиторий:
    - `DEPLOY_SERVER` - адрес хостинга, где будет выполнен деплой;
    - `USERNAME` - пользователь, от имени которого выполняется деплой;
    - `SSH_PRIVATE_KEY` - приватный ssh-ключ пользователя для подключения
    к серверу с github;
    - `TELEGRAM_BOTS_ALERTING_TO` - канал/пользователь которому отправляются
    сообщения со статусом деплоя;
    - `TELEGRAM_BOTS_ALERTING_TOKEN` - токен бота, который отправляет сообщения
    со статусом деплоя.

5. Сделать push в main, что стриггерит деплой.

6. Первый раз деплой продйет с ошибкой "Нет .prod.env файла", поэтому нужно
создать его в дирректории `~/telegram-bots/{название репозитория}`.
В нем должны быть обязательные переменные:
    - `BOT_TOKEN` - токен бота
