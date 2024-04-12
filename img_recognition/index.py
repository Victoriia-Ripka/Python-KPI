from program import load_image_file, face_locations, face_distance
image = load_image_file("./imgs/person-min.jpeg")
face_locations = face_locations(image)
print(face_locations)

# import face_recognition
# image = face_recognition.load_image_file("./imgs/person-min.jpeg")
# face_locations = face_recognition.face_locations(image)
# print(face_locations)