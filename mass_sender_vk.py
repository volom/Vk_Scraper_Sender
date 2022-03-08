from send_msg_vk import send_message
import time
import os

lst_receivers = list(open("users_db.txt", "r"))
lst_receivers = [x.replace("\n", "") for x in lst_receivers]
lst_receivers = list(dict.fromkeys(lst_receivers))

txt_msg = open(f"{os.getcwd()}//txt_msg.txt", 'r').read()

# check already sent
sent_msg = list(open("sent_msg.txt", "r"))
sent_msg = [x.replace('\n', '') for x in sent_msg]


lst_receivers = [x for x in lst_receivers if x not in sent_msg]


def run():
    for receiver in lst_receivers:
        try:
            send_message(receiver, txt_msg)
            print(f"Message was sent to id {receiver}")

            with open("sent_msg.txt", "a") as w:
                w.write(f"{receiver}\n")

            time.sleep(60)
        except Exception as e:
            print("-----------------")
            print(f"The error is occurred with id - {receiver}")
            print(str(e))
            print("-----------------")

if __name__ == "__main__":
    run()