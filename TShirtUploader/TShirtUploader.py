import os
import time
import json
from typing import Self
import requests
import shutil
import webbrowser
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print("Starting...")

time.sleep(2)
if os.path.isfile('credentials.json'):
    print("Loading credentials.json.")
else:
    print("Your credentials.json Doesnt exist.")
    exit(1)

time.sleep(1.5)
print("Quick TShirt Uploader, Made By Trillum.")


default_path = r"C:\Images" 
TEMP_FOLDER = os.path.join(os.getenv('TEMP'), 'roblox_uploads')
os.makedirs(TEMP_FOLDER, exist_ok=True)

while True:
    user_path = input(r"Enter a path (or press Enter to use the default 'C:\Images' ): ")

    MONITOR_FOLDER = user_path if user_path else default_path

    if os.path.exists(MONITOR_FOLDER):
        print(f"Monitoring folder set to: {MONITOR_FOLDER}")
        break
    else:
        print(f"The path '{MONITOR_FOLDER}' is invalid. Please try again.")

def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

class ImageUploadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".png"):
            self.log_message(f"New image detected: {event.src_path}")
            self.upload_image(event.src_path)

    def log_message(self, message):
        print(message)  # Log to console

    def upload_image(self, image_path):
        temp_file_path = os.path.join(TEMP_FOLDER, os.path.basename(image_path))
        time.sleep(2)
        # Move the file to the temp directory
        shutil.move(image_path, temp_file_path)
        self.log_message(f"Moving to temp: {temp_file_path}")

        try:
            operation_id = self.send_upload_request(temp_file_path)
            if operation_id:
                self.poll_upload_status(operation_id)
        except Exception as ex:
            self.log_message(f"Error during upload: {ex}")
        finally:
            # Delete the temp file after upload
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
                self.log_message("Temporary file deleted.")

    def send_upload_request(self, image_path):
        url = "https://apis.roblox.com/assets/v1/assets"
        credentials = load_credentials()
        headers = {
            "accept": "*/*",
            "x-api-key": credentials["apikey"]
        }

        file = open(image_path, 'rb')


        files = {
                'fileContent': (image_path, file, 'image/png'),
                'request': ('', json.dumps({
                "displayName": "tshirt",
                "description": "T-Shirt",
                "assetType": "Tshirt",
                "creationContext": {
                 "creator": {
                   "userId": credentials["UserId"]
                 },
                 "expectedPrice": 0
                }   
            }), 'application/json')
         }

        self.log_message("Uploading image...")
        response = requests.post(url, headers=headers, files=files)
        
        if response.status_code == 200:
            response_data = response.json()
            operation_id = response_data.get("operationId")
            self.log_message(f"Upload initiated, Operation ID: {operation_id}")
            return operation_id
        else:
            self.log_message(f"Upload failed: {response.status_code} - {response.text}")
            return None

    def poll_upload_status(self, operation_id):
        operation_url = f"https://apis.roblox.com/assets/v1/operations/{operation_id}"
        credentials = load_credentials()
        Headers = {
           "x-api-key": credentials["apikey"]
        }

        while True:
            time.sleep(5)  
            response = requests.get(operation_url, headers=Headers)

            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("done"):
                    asset_id = response_data['response']['assetId']
                    self.log_message(f"Upload complete! Asset ID: {asset_id}")
                    webbrowser.open(f"https://www.roblox.com/catalog/{asset_id}")
                    break
            else:
                self.log_message(f"Error checking upload status: {response.status_code}")
                break

def main():
    print(f"Monitoring {MONITOR_FOLDER} for new images...")
    
    # Set up the observer
    event_handler = ImageUploadHandler()
    observer = Observer()
    observer.schedule(event_handler, MONITOR_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
