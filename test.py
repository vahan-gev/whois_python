import face_recognition
from PIL import Image, ImageDraw
import cv2

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









known_face_encodings1 = [
    robert_face_encoding1,
    thor_face_encoding1
]

known_face_encodings2 = [
	robert_face_encoding2,
    thor_face_encoding2
]

known_face_encodings3 = [
	robert_face_encoding3,
    thor_face_encoding3
]

known_face_encodings4 = [
	robert_face_encoding4,
    thor_face_encoding4
]

known_face_encodings5 = [
	robert_face_encoding5,
    thor_face_encoding5
]

known_face_names = [
    "Robert Downey Jr",
    "Chris Hemsworth"
]

# Load test image

test_image = face_recognition.load_image_file("test_imgs/avengers.jpg")


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
            if(test1 + test2 + test3 + test4 + test5 == 5):
                acc = 100
            if(test1 + test2 + test3 + test4 + test5 == 4):
                acc = 80 
            if(test1 + test2 + test3 + test4 + test5 == 3):
                acc = 60
            if(test1 + test2 + test3 + test4 + test5 == 2):
                acc = 40
            if(test1 + test2 + test3 + test4 + test5 == 1):
                acc = 20
            print("Found: " + name + " with: " + str(acc) + "% Accuracy")
        # draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

        # text_width, text_height = draw.textsize(name)
        # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
        # draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

print(test1)
print(test2)
print(test3)
print(test4)
print(test5)


del draw

pil_image.show()
