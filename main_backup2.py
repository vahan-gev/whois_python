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
        
        # Robert Downey Jr

        image_of_robert1 = face_recognition.load_image_file('./test_imgs/Robert Downey Jr/Robert Downey Jr 1.jpg')
        robert_face_encoding1 = face_recognition.face_encodings(image_of_robert1)[0]

        image_of_robert2 = face_recognition.load_image_file('./test_imgs/Robert Downey Jr/Robert Downey Jr 2.jpg')
        robert_face_encoding2 = face_recognition.face_encodings(image_of_robert2)[0]

        image_of_robert3 = face_recognition.load_image_file('./test_imgs/Robert Downey Jr/Robert Downey Jr 3.jpg')
        robert_face_encoding3 = face_recognition.face_encodings(image_of_robert3)[0]

        image_of_robert4 = face_recognition.load_image_file('./test_imgs/Robert Downey Jr/Robert Downey Jr 4.jpg')
        robert_face_encoding4 = face_recognition.face_encodings(image_of_robert4)[0]

        image_of_robert5 = face_recognition.load_image_file('./test_imgs/Robert Downey Jr/Robert Downey Jr 5.jpg')
        robert_face_encoding5 = face_recognition.face_encodings(image_of_robert5)[0]


        # Chris Hemsworth

        image_of_thor1 = face_recognition.load_image_file('./test_imgs/Chris Hemsworth/Chris Hemsworth 1.jpg')
        thor_face_encoding1 = face_recognition.face_encodings(image_of_thor1)[0]

        image_of_thor2 = face_recognition.load_image_file('./test_imgs/Chris Hemsworth/Chris Hemsworth 2.jpg')
        thor_face_encoding2 = face_recognition.face_encodings(image_of_thor2)[0]

        image_of_thor3 = face_recognition.load_image_file('./test_imgs/Chris Hemsworth/Chris Hemsworth 3.jpg')
        thor_face_encoding3 = face_recognition.face_encodings(image_of_thor3)[0]

        image_of_thor4 = face_recognition.load_image_file('./test_imgs/Chris Hemsworth/Chris Hemsworth 4.jpg')
        thor_face_encoding4 = face_recognition.face_encodings(image_of_thor4)[0]

        image_of_thor5 = face_recognition.load_image_file('./test_imgs/Chris Hemsworth/Chris Hemsworth 5.jpg')
        thor_face_encoding5 = face_recognition.face_encodings(image_of_thor5)[0]

        # Vahan Gevorgyan
        image_of_vahan1 = face_recognition.load_image_file('./test_imgs/Vahan Gevorgyan/Vahan Gevorgyan 1.jpg')
        vahan_face_encoding1 = face_recognition.face_encodings(image_of_vahan1)[0]

        image_of_vahan2 = face_recognition.load_image_file('./test_imgs/Vahan Gevorgyan/Vahan Gevorgyan 2.jpg')
        vahan_face_encoding2 = face_recognition.face_encodings(image_of_vahan2)[0]

        image_of_vahan3 = face_recognition.load_image_file('./test_imgs/Vahan Gevorgyan/Vahan Gevorgyan 3.jpg')
        vahan_face_encoding3 = face_recognition.face_encodings(image_of_vahan3)[0]

        image_of_vahan4 = face_recognition.load_image_file('./test_imgs/Vahan Gevorgyan/Vahan Gevorgyan 4.jpg')
        vahan_face_encoding4 = face_recognition.face_encodings(image_of_vahan4)[0]

        image_of_vahan5 = face_recognition.load_image_file('./test_imgs/Vahan Gevorgyan/Vahan Gevorgyan 5.jpg')
        vahan_face_encoding5 = face_recognition.face_encodings(image_of_vahan5)[0]

        # Chris Evans
        image_of_evans1 = face_recognition.load_image_file('./test_imgs/Chris Evans/Chris Evans 1.jpg')
        evans_face_encoding1 = face_recognition.face_encodings(image_of_evans1)[0]

        image_of_evans2 = face_recognition.load_image_file('./test_imgs/Chris Evans/Chris Evans 2.jpg')
        evans_face_encoding2 = face_recognition.face_encodings(image_of_evans2)[0]

        image_of_evans3 = face_recognition.load_image_file('./test_imgs/Chris Evans/Chris Evans 3.jpg')
        evans_face_encoding3 = face_recognition.face_encodings(image_of_evans3)[0]

        image_of_evans4 = face_recognition.load_image_file('./test_imgs/Chris Evans/Chris Evans 4.jpg')
        evans_face_encoding4 = face_recognition.face_encodings(image_of_evans4)[0]

        image_of_evans5 = face_recognition.load_image_file('./test_imgs/Chris Evans/Chris Evans 5.jpg')
        evans_face_encoding5 = face_recognition.face_encodings(image_of_evans5)[0]







        known_face_encodings1 = [
            robert_face_encoding1,
            thor_face_encoding1,
            vahan_face_encoding1,
            evans_face_encoding1
        ]

        known_face_encodings2 = [
            robert_face_encoding2,
            thor_face_encoding2,
            vahan_face_encoding2,
            evans_face_encoding2
        ]

        known_face_encodings3 = [
            robert_face_encoding3,
            thor_face_encoding3,
            vahan_face_encoding3,
            evans_face_encoding3
        ]

        known_face_encodings4 = [
            robert_face_encoding4,
            thor_face_encoding4,
            vahan_face_encoding4,
            evans_face_encoding4
        ]

        known_face_encodings5 = [
            robert_face_encoding5,
            thor_face_encoding5,
            vahan_face_encoding5,
            evans_face_encoding5
        ]

        known_face_names = [
            "Robert Downey Jr",
            "Chris Hemsworth",
            "Vahan Gevorgyan",
            "Chris Evans"
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

        test1 = 0
        test2 = 0
        test3 = 0
        test4 = 0
        test5 = 0
        acc = 0

        # Loop through faces 1

        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings1, face_encoding)
                name = "Unknown Person"
                test1 = 0
                acc = 0
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    test1 = 1
                    


        # Loop through faces 2
        if test1 == 1:
            for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings2, face_encoding)
                name = "Unknown Person"
                test2 = 0
                acc = 0
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    test2 = 1
                # draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

                # text_width, text_height = draw.textsize(name)
                # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
                # draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

        # Loop through faces 3

        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings3, face_encoding)
                name = "Unknown Person"
                test3 = 0
                acc = 0
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    test3 = 1
                # draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

                # text_width, text_height = draw.textsize(name)
                # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
                # draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

        # Loop through faces 4


        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings4, face_encoding)
                name = "Unknown Person"
                test4 = 0
                acc = 0
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    test4 = 1
                # draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

                # text_width, text_height = draw.textsize(name)
                # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
                # draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

        # Loop through faces 5

        for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(known_face_encodings5, face_encoding)
                name = "Unknown Person"
                test5 = 0
                acc = 0
                if True in matches:
                    first_match_index = matches.index(True) 
                    test5 = 1
                    
                    if(test1 + test2 + test3 + test4 + test5 >= 3):
                        name = known_face_names[first_match_index]
                        acc = ((test1 + test2 + test3 + test4 + test5) * 100) / 5
                    
                    print("=================================")
                    print("[SUCCESS] Found: " + name + " with: " + str(acc) + "% Accuracy")
                # draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

                # text_width, text_height = draw.textsize(name)
                # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
                # draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))
            

        del draw
        
        # pil_image.show()    
        
        os.remove("IMG_{}.png".format(timestr))
        print("[SUCCESS] Captured: " + name)
        try:
            os.mkdir("database")
        except:
            print("[DATABASE] Folder Exists. No need to create another!")
        
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