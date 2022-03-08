from auth_info import *

def send_message(user_id, message):
    vk_api_access.messages.send(user_id=user_id, message=message, random_id=get_random_id())
