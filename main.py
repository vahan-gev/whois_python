from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import face_recognition
from PIL import Image, ImageDraw
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
import time, os, re, sys, pickle
import numpy as np
nameFound = ""
KNOWN_FACES_DIR = "test_imgs"
UNKNOWN_FACES_DIR = "database"
TOLERANCE = 0.6
MODEL = "cnn"


with open('dataset_faces.dat', 'rb') as f:
    all_face_encodings = pickle.load(f)

known_names = list(all_face_encodings.keys())
known_faces = np.array(list(all_face_encodings.values()))


class MainWindow(Screen):    
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("database/IMG_FOUND.png")        
        for filename in os.listdir(UNKNOWN_FACES_DIR):
            image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{filename}")
            locations = face_recognition.face_locations(image, model=MODEL)
            encodings = face_recognition.face_encodings(image, locations)
            for face_encoding in encodings:
                results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
                match = None
                if True in results:
                    match = known_names[results.index(True)]
                    print("=================================")
                    print("[SUCCESS] Found: " + match)         
                    os.remove("database/IMG_FOUND.png")
                    try:
                        os.mkdir("database")
                    except:
                        print("[DATABASE] Folder Exists. No need to create another!")
                    
                    f = open("database/name.log", "w+")
                    f.write(match)
                    f.close() 

class FoundedWindow(Screen):
    def on_start(self):
        f = open("database/name.log", "r")
        nameFound = f.read()     
        f.close() 
        os.remove("database/name.log")
        fontS = 0
        if(len(nameFound) < 15):
            fontS = 40
        else:
            fontS = 30
        self.submit = Button(text=nameFound, font_size=fontS, on_press=self.goback)  
        self.add_widget(self.submit)
        print("[SUCCESS] Created with text: " + nameFound)
        print("[SUCCESS] Created with font size: " + str(fontS))
        print("=================================")
   
    def goback(self, instance):
        self.parent.current = 'main'
        self.manager.transition.direction = 'right'
        

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("page_manager.kv")
window = Window
Window.size = (320, 600)
class TestCamera(App):
    title = "WhoIs (Mobile)"
    icon = 'icons/icon2.png'
    #Config.set('kivy','window_icon','icons/main.ico')
    def build(self):
        return kv

TestCamera().run()