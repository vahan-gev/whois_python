import time, os, re, numpy, sys, pickle
import face_recognition
nameFound = ""
KNOWN_FACES_DIR = "test_imgs"
UNKNOWN_FACES_DIR = "database"
TOLERANCE = 0.6
MODEL = "cnn"

all_face_encodings = {}

print("[ONGOING] Processing Known Celebrities")
for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        all_face_encodings[name] = face_recognition.face_encodings(image)[0]
        
print("[DONE] Processing Known Celebrities")



with open('dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)