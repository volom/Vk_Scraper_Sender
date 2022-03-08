from auth_info import *

# groupd_id - идентификатор или короткое имя сообщества
def get_members(group_id) -> list:
    return vk_api_access.groups.getMembers(group_id=group_id)["items"]

# set list of groups to scrap
groups_list = []
for group in groups_list:
    for i in get_members(group_id=group):
        with open("users_db.txt", "a") as w:
            w.write(f"{i}\n")