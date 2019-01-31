from django.views import generic
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json, requests
from pprint import pprint


PAGE_ACCESS_TOKEN = 'EAALZARfySpU4BAKAnGyRJkX1PNOYhdBEEKeXtyAzLHjEsxGvZBTvQAxJhLZB99RAmkbmARKoZCkdIOp7zx3F8OmZA5yt5xTYxBadvni2LKwkt0vZAOzVCO7QI5F8o5UB5mGYJI0FHhYGFlDQ2aNgYPPURdkiDZCgYsJV0trC4ULHgZDZD'


class FacebookBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '2318934571':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        pprint(incoming_message)
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    post_facebook_message(message['sender']['id'])
        return HttpResponse()


def post_facebook_message(fbid):

    user_details_url = "https://graph.facebook.com/v2.6/{}".format(fbid)
    user_details_params = {'fields': 'first_name,last_name,profile_pic', 'access_token': PAGE_ACCESS_TOKEN}
    user_details = requests.get(user_details_url, user_details_params).json()

    message_to_response = 'Hi, {0}. Welcome!'

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token={}'.format(PAGE_ACCESS_TOKEN)
    response_msg = json.dumps({"recipient": {"id": fbid}, "message": {"text": message_to_response}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"}, data=response_msg)
    pprint(status.json())
