from django.urls import reverse
from telegram.ext import CommandHandler, Updater
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import viber_request

from bots.constants import BotTypes
from .tasks import send_telegram_bot_message, send_viber_bot_message


def telegram_bot_init(api_key, bot_type, bot_pk, active):
    updater = Updater(api_key)
    if active:
        from bots.models import BotBase
        bot_instance = BotBase.objects.get(pk=bot_pk)

        def start(tg_bot, update):
            print('start command')
            bot_instance.chat_id = update.message.chat_id
            bot_instance.save()

        updater.dispatcher.add_handler(CommandHandler('start', start))

        updater.start_polling()
        # updater.idle()
    else:
        updater.stop()


def viber_bot_init(api_key, bot_type, bot_pk, active):
    bot_configuration = BotConfiguration(
        name='PythonSampleBot',
        avatar='http://viber.com/avatar.jpg',
        auth_token=api_key
    )
    viber = Api(bot_configuration)
    viber.set_webhook('http://127.0.0.1:8000' + reverse('bots:viber_handler'))
    print('here')
    # viber_request = viber.parse_request(request.get_data())
    # viber.send_messages(to=viber_request.get_sender().get_id(),
    #                     messages=[TextMessage(text="sample message")])


def bot_init(api_key, bot_type, bot_pk, active):
    if bot_type == BotTypes.TELEGRAM:
        telegram_bot_init(api_key, bot_type, bot_pk, active)
    elif bot_type == BotTypes.WHATS_UP:
        pass
    elif bot_type == BotTypes.VIBER:
        viber_bot_init(api_key, bot_type, bot_pk, active)
    elif bot_type == BotTypes.FACEBOOK:
        pass


def start_bot_chain(chain, bot):
    if bot.bot_type == BotTypes.TELEGRAM:
        bot_function = send_telegram_bot_message
    elif bot.bot_type == BotTypes.WHATS_UP:
        pass
    elif bot.bot_type == BotTypes.VIBER:
        bot_function = send_viber_bot_message
    elif bot.bot_type == BotTypes.FACEBOOK:
        pass

    messages = chain.chains_message.all().order_by('order')
    for message in messages:
        if bot.user not in message.sent_to.all():
            bot_function.apply_async(
                [message.pk, bot.api_key, bot.pk, bot.chat_id, bot.user.pk],
                countdown=message.delay)
