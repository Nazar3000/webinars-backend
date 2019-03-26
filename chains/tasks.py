from telegram import Bot

from Project_W.celery import app


@app.task
def send_bot_message(content, msg_type, api_key, bot_pk, chat_id):
    print('inside')
    from bots.models import BotBase
    print(content, msg_type, api_key, bot_pk)

    bot_instance = BotBase.objects.get(pk=bot_pk)
    if bot_instance.telegram_chat_id:
        bot = Bot(api_key)

        bot.send_message(chat_id=chat_id, text=content)
