from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from picamera2 import Picamera2, Preview
import datetime
import time


MINS_OF_VIDEO = 240
camera = Picamera2()
config = camera.create_preview_configuration({'format': 'RGB888'})
camera.configure(config)


def capture_video():
    file = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    file = file + '.mp4'
    print(file)
    camera.start_and_record_video(file, duration=10)
    #camera.start_preview()
    #camera.start_recording(file)
    #sleep(5)
    #camera.stop-recording()
    #camera.stop_preview()
    #insert here the one Picamera2 function to take a video and save to 'file' with time MINS_OF_VIDEO
    return file
    
#def video():
    


def upload(filename):
    gauth = authenticate()
    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({'title': filename, 'mimeType':'video/mp4'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentFile(filename)  # Set content of the file from given string.
    file1.Upload()


def authenticate():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        print("Google Drive Token Expired, Refreshing")
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("mycreds.txt")
    return gauth


if __name__ == '__main__':
    filename = capture_video()
    upload(filename)
