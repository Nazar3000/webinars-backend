import requests


class TelegramBotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    @staticmethod
    def get_updates_json(request):
        response = requests.get(request + 'getUpdates')
        return response.json()

    @staticmethod
    def last_update(data):
        results = data['result']
        total_updates = len(results) - 1
        return results[total_updates]

    @staticmethod
    def get_chat_id(update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def send_message(self, text):
        chat_id = self.get_chat_id(self.last_update(self.get_updates_json(self.api_url)))
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(self.api_url + 'sendMessage', data=params)
        return response
