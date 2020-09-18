import requests

from pypresence import Client

CLIENT_ID = "207646673902501888"
TOKEN_URL = "https://streamkit.discord.com/overlay/token"


rpc = Client(CLIENT_ID)


def get_code():
    response = rpc.authorize(CLIENT_ID, ["rpc", "messages.read"])
    data = response["data"]

    return data["code"]


def get_access_token(code):
    response = requests.post(url=TOKEN_URL, json={"code": code})
    data = response.json()

    return data["access_token"]


def get_selected_voice_channel():
    response = rpc.get_selected_voice_channel()
    data = response["data"]

    return data

def main():
    try:
        rpc.start()
        rpc.authenticate(get_access_token(get_code()))

        voice_channel = get_selected_voice_channel()
        result = (
            f"\"{voice_channel['name']}\" (ID: {voice_channel['id']})"
            if voice_channel
            else "None"
        )

        print(f"Selected Voice Channel: {result}")
    finally:
        rpc.close()

if __name__ == "__main__":
    main()
