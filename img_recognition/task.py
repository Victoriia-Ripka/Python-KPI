from PIL import Image, ImageDraw
from program import load_image_file, face_locations
import face_recognition

# Load image
image_path = "./imgs/stuard.jpg"
image = Image.open(image_path)

# Detect faces using your program
face_locations_program = face_locations(load_image_file(image_path))
print("program: ", face_locations_program)

# Draw red rectangles around detected faces
draw_program = ImageDraw.Draw(image)
for top, right, bottom, left in face_locations_program:
    draw_program.rectangle([left, top, right, bottom], outline="red", width=2)

# Save the modified image
image.save(f"recognized/p.jpg")

# Load image using face_recognition
image = face_recognition.load_image_file(image_path)

# Detect faces using face_recognition
face_locations_fr = face_recognition.face_locations(image)
print("face_recognition: ", face_locations_fr)

# Draw red rectangles around detected faces
image = Image.open(image_path)
draw_fr = ImageDraw.Draw(image)
for top, right, bottom, left in face_locations_fr:
    draw_fr.rectangle([left, top, right, bottom], outline="red", width=2)

# Save the modified image
image.save(f"recognized/fr.jpg")