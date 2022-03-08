import vk_api
from vk_api.utils import get_random_id

# get your token here - https://vkhost.github.io/
token = "token"

def vk_auth(token):
        try:
            vk_session = vk_api.VkApi(token=token)
            return vk_session.get_api()
        except Exception as error:
            print(error)
            return None

vk_api_access = vk_auth(token)    
