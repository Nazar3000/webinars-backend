from telegram import Bot

from Project_W.celery import app


def get_msg_type_and_content(message):
    msg_type = None
    content = None
    if message.text:
        msg_type = 'text'
        content = message.text
    elif message.link:
        msg_type = 'link'
        content = message.link
    elif message.image:
        msg_type = 'image'
        content = message.image
    elif message.audio:
        msg_type = 'audio'
        content = message.audio
    elif message.video:
        msg_type = 'video'
        content = message.video
    elif message.file:
        msg_type = 'file'
        content = message.file
    elif message.map:
        msg_type = 'map'
        content = message.map
    # elif message.timer:
    #     msg_type = 'timer'
    # elif message.button:
    #     msg_type = 'button'
    return msg_type, content


@app.task
def send_telegram_bot_message(msg_pk, api_key, bot_pk, chat_id, user_pk):
    from bots.models import BotBase
    from chains.models import Message

    bot_instance = BotBase.objects.get(pk=bot_pk)
    message = Message.objects.get(pk=msg_pk)
    msg_type, content = get_msg_type_and_content(message)

    if bot_instance.chat_id:
        bot = Bot(api_key)

        if msg_type == 'text':
            bot.send_message(chat_id=chat_id, text=content)
        elif msg_type == 'link':
            bot.send_message(
                chat_id=chat_id,
                text='[{content}]({content})'.format(content=content), parse_mode='markdown')
        elif msg_type == 'image':
            bot.send_photo(chat_id=chat_id, photo=content)
        elif msg_type == 'audio':
            bot.send_audio(chat_id=chat_id, audio=content)
        elif msg_type == 'video':
            bot.send_video(chat_id=chat_id, video=content)
        elif msg_type == 'file':
            bot.send_document(chat_id=chat_id, document=content)
        elif msg_type == 'map':
            bot.send_location(chat_id=chat_id, latitude=str(content[0]), longitude=str(content[1]))
        # elif msg_type == 'timer':
        #     pass
        # elif msg_type == 'button':
        #     pass

        message.sent_to.add(user_pk)


@app.task
def send_viber_bot_message(msg_pk, api_key, bot_pk, chat_id, user_pk):
    pass
