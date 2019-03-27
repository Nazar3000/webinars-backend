from telegram.ext import CommandHandler, Updater

from bots.constants import BotTypes
from .tasks import send_bot_message


def bot_init(api_key, bot_pk, active):
    updater = Updater(api_key)
    if active:
        from bots.models import BotBase
        bot_instance = BotBase.objects.get(pk=bot_pk)

        if bot_instance.telegram_chat_id:
            def start(tg_bot, update):
                print('start command')
                bot_instance.telegram_chat_id = update.message.chat_id
                bot_instance.save()

            updater.dispatcher.add_handler(CommandHandler('start', start))

            updater.start_polling()
            # updater.idle()
    else:
        updater.stop()


def start_telegram_chain(chain, bot):
    messages = chain.chains_message.all().order_by('order')
    for message in messages:
        if bot.user not in message.sent_to.all():
            send_bot_message.apply_async(
                [message.pk, bot.api_key, bot.pk, bot.telegram_chat_id, bot.user.pk],
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
