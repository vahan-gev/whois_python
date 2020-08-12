from __future__ import print_function
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from PIL import Image, ImageDraw
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
import time, os, re, sys, pickle
import numpy as np
import click
import face_recognition.api as face_recognition
import multiprocessing
import itertools
nameFound = ""
KNOWN_FACES_DIR = "test_imgs"
UNKNOWN_FACES_DIR = "database"
TOLERANCE = 0.6
MODEL = "cnn"

def scan_known_people(known_people_folder):

    with open('dataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)

    known_names = list(all_face_encodings.keys())
    known_face_encodings = np.array(list(all_face_encodings.values()))

    # for file in image_files_in_folder(known_people_folder):
    #     basename = os.path.splitext(os.path.basename(file))[0]
    #     img = face_recognition.load_image_file(file)
    #     encodings = face_recognition.face_encodings(img)

    #     if len(encodings) > 1:
    #         click.echo("WARNING: More than one face found in {}. Only considering the first face.".format(file))

    #     if len(encodings) == 0:
    #         click.echo("WARNING: No faces found in {}. Ignoring file.".format(file))
    #     else:
    #         known_names.append(basename)
    #         known_face_encodings.append(encodings[0])

    return known_names, known_face_encodings


def print_result(filename, name, distance, show_distance=False):
    if False:
        print(name)
        f = open("database/name.log", "w+")
        f.write(name)
        f.close() 
    else:
        print(name)
        f = open("database/name.log", "w+")
        f.write(name)
        f.close() 
        


def test_image(image_to_check, known_names, known_face_encodings, TOLERANCE=0.6, show_distance=False):
    unknown_image = face_recognition.load_image_file(image_to_check)

    if max(unknown_image.shape) > 1600:
        pil_img = PIL.Image.fromarray(unknown_image)
        pil_img.thumbnail((1600, 1600), PIL.Image.LANCZOS)
        unknown_image = np.array(pil_img)

    unknown_encodings = face_recognition.face_encodings(unknown_image)

    for unknown_encoding in unknown_encodings:
        distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
        result = list(distances <= TOLERANCE)

        if True in result:
            [print_result(image_to_check, name, distance, False) for is_match, name, distance in zip(result, known_names, distances) if is_match]
        else:
            print_result(image_to_check, "unknown_person", None, False)

    if not unknown_encodings:
        print_result(image_to_check, "no_persons_found", None, False)

def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]


def process_images_in_process_pool(images_to_check, known_names, known_face_encodings, number_of_cpus, TOLERANCE, show_distance):
    if number_of_cpus == -1:
        processes = None
    else:
        processes = number_of_cpus

    # macOS will crash due to a bug in libdispatch if you don't use 'forkserver'
    context = multiprocessing
    if "forkserver" in multiprocessing.get_all_start_methods():
        context = multiprocessing.get_context("forkserver")

    pool = context.Pool(processes=processes)

    function_parameters = zip(
        images_to_check,
        itertools.repeat(known_names),
        itertools.repeat(known_face_encodings),
        itertools.repeat(TOLERANCE),
        itertools.repeat(False)
    )

    pool.starmap(test_image, function_parameters)


@click.command()
@click.argument('known_people_folder')
@click.argument('image_to_check')
@click.option('--cpus', default=6)
@click.option('--tolerance', default=0.6)
@click.option('--show-distance', default=False, type=bool)

class MainWindow(Screen):    
    def capture(self):
        match = ""
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("database/IMG_FOUND.png")        

        known_names, known_face_encodings = scan_known_people(KNOWN_FACES_DIR)
        if (sys.version_info < (3, 4)) and cpus != 1:
            click.echo("WARNING: Multi-processing support requires Python 3.4 or greater. Falling back to single-threaded processing!")
        cpus = 1
        if os.path.isdir("database/IMG_FOUND.png"):
            if cpus == 1:
                [test_image(image_file, known_names, known_face_encodings, TOLERANCE, False) for image_file in image_files_in_folder(image_to_check)]
            else:
                process_images_in_process_pool(image_files_in_folder("database/IMG_FOUND.png"), known_names, known_face_encodings, cpus, TOLERANCE, False)
        else:
            test_image("database/IMG_FOUND.png", known_names, known_face_encodings, TOLERANCE, False)

        
        print("=================================")         
        os.remove("database/IMG_FOUND.png")
        try:
            os.mkdir("database")
        except:
            print("[DATABASE] Folder Exists. No need to create another!")
        
        

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