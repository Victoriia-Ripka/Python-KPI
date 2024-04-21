from program import load_image_file, face_locations
import face_recognition


image = load_image_file("./imgs/stuard-min.jpg")
face_locations = face_locations(image)
print("program: ", face_locations)


image = face_recognition.load_image_file("./imgs/stuard-min.jpg")
face_locations = face_recognition.face_locations(image)
print("face_recognition: ", face_locations)