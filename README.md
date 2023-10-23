# Python-Keylogger
This repository contains a simple keylogger implemented in Python that uses https://webhook.site to receive the captured keystrokes from a remote machine.

## Installation
1. Clone the repository to your local machine or download the zip file and extract it.
   ```
   git clone https://github.com/Th3Th1nk3r/Python-Keylogger.git
   ```
2. Make sure you have Python installed on your system. This code has been tested on Python 3.11 and above.
3. Navigate to the project directory.
   ```
   cd Python-Keylogger
   ```
4. Install the required dependencies by running the following command in your terminal:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Sign up for a free account or just visit on https://webhook.site and obtain a unique URL for your webhook endpoint.
2. Open the Keylogger.py file in a text editor and update the WEBHOOK_URL variable with your unique URL.
   ```
   WEBHOOK_URL = 'https://webhook.site/your-unique-url-token'
   ```
3. Update the WAITING_TIME variable in the script to set the desired time interval (in seconds) for receiving the keylogs.
   ```
   WAITING_TIME = 60
   ```
5. Save the file and run the script using the following command:
   ```
   python Keylogger.py
   ```

The Keylogger will start capturing all keystrokes immediately.
After the specified WAITING_TIME, the captured keystrokes will be sent to the provided webhook URL.

**Note:** Make sure the terminal remains open until you receive the keylogs at the webhook URL.
To stop the Keylogger, press **`Ctrl+C`** in the terminal.

## Disclaimer
This keylogger is provided for educational purposes only. The use of this code for malicious activities is strictly prohibited. The author is not responsible for any consequences that may arise from the misuse of this code.
