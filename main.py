from pydrive.drive import GoogleDrive #API application programming interface: allows people to access funct, ppl who arent in the company can access, security feature
#can control what people can use from code, need token for every API, so API that allows us to access these libraries
#pydrive: python library that allows us to use the google drive API, wrapper that includes API's covers code
from pydrive.auth import GoogleAuth #likea key to make sure youre not a bot
from picamera2 import Picamera2, Preview
import datetime
import time


MINS_OF_VIDEO = 240
camera = Picamera2()
config = camera.create_preview_configuration({'format': 'RGB888'})
camera.configure(config)


def capture_video(): #
    file = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S') #gets current date and time for drive
    file = file + '.mp4'
    print(file)
    camera.start_and_record_video(file, duration=10) #pi cam funct, camera. is inst of pi camera class
    #camera.start_preview()
    #camera.start_recording(file)
    #sleep(5)
    #camera.stop-recording()
    #camera.stop_preview()
    #insert here the one Picamera2 function to take a video and save to 'file' with time MINS_OF_VIDEO
    return file #name
    
#def video():
    


def upload(filename):
    gauth = authenticate()
    drive = GoogleDrive(gauth) #gdrive auth

    file1 = drive.CreateFile({'title': filename, 'mimeType':'video/mp4'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentFile(filename)  # Set content of the file from given string.
    file1.Upload()


def authenticate(): #loads all funct first so this funct is alr loaded
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("mycreds.txt") #where token pass is stored, file in comput, dont upload mycreds.txt!! only on comput
    if gauth.credentials is None: #using gauth. class funct, making token if none when mycreds.txt is empty
        gauth.LocalWebserverAuth() #opens browser window to login, shouldnt need monitor to run code
    elif gauth.access_token_expired: #pass needs to keep reloading like once a week bc of google policy, buggy???
        print("Google Drive Token Expired, Refreshing")
        gauth.Refresh() #this part doesnt work as it should
    else:
        gauth.Authorize() #this is auth file telling goog
    gauth.SaveCredentialsFile("mycreds.txt") # saves cred file into mycreds.txt
    return gauth


if __name__ == '__main__': #where it starts, calls all above funct
    filename = capture_video()
    upload(filename)
