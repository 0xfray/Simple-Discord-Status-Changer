import time
import requests


url = "https://discord.com/api/v8/users/@me/settings"


with open("messages.txt", "r") as file:
    lines = file.readlines()

def changestatus(message):

    header = {
        "authorization": "ADD_YOUR_HEADER_HERE" 
    }


    jsonData = {
        "status": "dnd", 
        "custom_status": {
            "text": message 
        }
    }

    try:

        response = requests.patch(url, headers=header, json=jsonData)
        if response.status_code == 200:
            print(f"Status changed to: {message}")
        else:
            print(f"Failed to change status: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error: {e}")


while True:
    for line in lines:
        message = line.strip()  
        if message:  
            changestatus(message)
            time.sleep(4)
