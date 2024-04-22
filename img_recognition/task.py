from PIL import Image, ImageDraw
from program import load_image_file, face_locations
import face_recognition
import os

image_files = [
    "./imgs/biden.jpeg",
    "./imgs/building.jpg",
    "./imgs/cat.jpg",
    "./imgs/couple.jpeg",
    "./imgs/hourse.jpg",
    "./imgs/hourses.jpg",
    "./imgs/mountain.jpg",
    "./imgs/obama.jpeg",
    "./imgs/people.jpeg",
    "./imgs/person.jpeg",
    "./imgs/stuard.jpg"
]

while True:
    print("\nChoose an image:")
    for i, img_path in enumerate(image_files, start=1):
        print(f"{i}: {img_path}")

    choice = input("Enter the number of the image (1-11) or '0' to exit: ")

    if choice == '0':
        print("Exiting...")
        break

    try:
        choice = int(choice)
        if 1 <= choice <= len(image_files):
            image_path = image_files[choice - 1]
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Load the image
    image = Image.open(image_path)
    file_name, extension = os.path.splitext(os.path.basename(image_path))

    # MY PROGRAM
    image1 = load_image_file(image_path)
    face_locations_program = face_locations(image1)
    print("program: ", face_locations_program)

    # Draw red rectangles around detected faces
    draw_program = ImageDraw.Draw(image)
    for top, right, bottom, left in face_locations_program:
        draw_program.rectangle([left, top, right, bottom], outline="red", width=2)
    image.save(f"recognized/{file_name}_p{extension}")

    # FACE ROCOGNITION
    image2 = face_recognition.load_image_file(image_path)
    face_locations_fr = face_recognition.face_locations(image2)
    print("face_recognition: ", face_locations_fr)

    # Draw red rectangles around detected faces
    image = Image.open(image_path)
    draw_fr = ImageDraw.Draw(image)
    for top, right, bottom, left in face_locations_fr:
        draw_fr.rectangle([left, top, right, bottom], outline="red", width=2)
    image.save(f"recognized/{file_name}_fr{extension}")
