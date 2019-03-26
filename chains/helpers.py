from telegram.ext import CommandHandler, Updater

from bots.constants import BotTypes
from .tasks import send_bot_message


def bot_init(api_key, bot_pk):
    from bots.models import BotBase
    bot_instance = BotBase.objects.get(pk=bot_pk)
    updater = Updater(api_key)

    def start(tg_bot, update):
        print('start command')
        bot_instance.telegram_chat_id = update.message.chat_id
        bot_instance.save()

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    # updater.idle()


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


def start_telegram_chain(chain, bot):
    messages = chain.chains_message.all().order_by('order')
    for message in messages:
        msg_type, content = get_msg_type_and_content(message)
        if msg_type and content:
            if message.delay == 0:
                print('no delay')
                send_bot_message.delay(content, msg_type, bot.api_key, bot.pk, bot.chat_id)
            else:
                send_bot_message.apply_async(
                    [content, msg_type, bot.api_key, bot.pk, bot.chat_id],
                    countdown=message.delay)


def start_bot_chain(chain, bot):
    if bot.bot_type == BotTypes.TELEGRAM:
        start_telegram_chain(chain, bot)
    elif bot.bot_type == BotTypes.WHATS_UP:
        pass
    elif bot.bot_type == BotTypes.VIBER:
        pass
    elif bot.bot_type == BotTypes.FACEBOOK:
        pass
