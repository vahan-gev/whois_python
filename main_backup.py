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
import time
import os

nameFound = ""
class CameraClick(BoxLayout):
    pass

class MainWindow(Screen):
    
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        
        image_of_bill = face_recognition.load_image_file('./img/Bill Gates.jpg')
        bill_face_encoding = face_recognition.face_encodings(image_of_bill)[0]

        image_of_steve = face_recognition.load_image_file('./img/Steve Jobs.jpg')
        steve_face_encoding = face_recognition.face_encodings(image_of_steve)[0]

        image_of_vahan = face_recognition.load_image_file('./img/Vahan Gevorgyan.jpg')
        vahan_face_encoding = face_recognition.face_encodings(image_of_vahan)[0]

        image_of_anna = face_recognition.load_image_file('./img/Anna Gevorgyan.jpg')
        anna_face_encoding = face_recognition.face_encodings(image_of_anna)[0]

        known_face_encodings = [
            bill_face_encoding,
            steve_face_encoding,
            vahan_face_encoding,
            anna_face_encoding
        ]

        known_face_names = [
            "Bill Gates",
            "Steve Jobs",
            "Vahan Gevorgyan",
            "Anna Gevorgyan"
        ]

        # Load test image

        test_image = face_recognition.load_image_file("IMG_{}.png".format(timestr))


        # Find faces in test image

        face_locations = face_recognition.face_locations(test_image)
        face_encodings = face_recognition.face_encodings(test_image, face_locations)

        # Convert to PIL format

        pil_image = Image.fromarray(test_image)

        # Create a ImageDraw instance

        draw = ImageDraw.Draw(pil_image)

        # Loop through faces
        
        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown Person"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                nameFound = name
            draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))
            

        del draw
        
        # pil_image.show()    
        
        os.remove("IMG_{}.png".format(timestr))
        print("Captured: " + name)
        try:
            os.mkdir("database")
        except:
            print("[Database folder exists] No need to create another!")
        
        f = open("database/name.log", "a+")
        f.write(name)
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
        print("Created with text: " + nameFound)
        print("Created with font size: " + str(fontS))
    
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
    icon = 'icons/main.png'
    #Config.set('kivy','window_icon','icons/main.ico')
    def build(self):
        return kv



TestCamera().run()