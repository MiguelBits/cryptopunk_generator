from PIL import Image
import random

#variables
faces = ["./images/face_0.png","./images/face_1.png"]
mouths = ["./images/mouth_0.png","./images/mouth_1.png"]
eyes_R = ["./images/eye_right_0.png","./images/eye_right_1.png"]
eyes_L = ["./images/eye_left_0.png","./images/eye_left_1.png"]
hairs = []

#random weights (rarity implementation) 80%chance for 1st in array, 20%chance for second ...
face = random.choices(faces,weights=(80,20))[0]
mouth = random.choices(mouths,weights=(80,20))[0]
eye_R = random.choices(eyes_R,weights=(80,20))[0]
eye_L = random.choices(eyes_L,weights=(80,20))[0]


def join_images(img1,img2):
    img1_rgba = img1.convert('RGBA')
    img2_rgba = img2.convert('RGBA')
    intermediate = Image.alpha_composite(img1_rgba,img2_rgba)
    
    return intermediate

def create_person(face,mouth,eye_R,eye_L):
    face_img = Image.open(face)
    mouth_img = Image.open(mouth)
    eye_R_img = Image.open(eye_R)
    eye_L_img = Image.open(eye_L)

    face_mouth_img = join_images(face_img,mouth_img)
    face_mouth_eye_R_img = join_images(face_mouth_img,eye_R_img)
    face_mouth_eye_R_eye_L_img = join_images(face_mouth_eye_R_img,eye_L_img)
    face_mouth_eye_R_eye_L_img.save("final.png")

create_person(face,mouth,eye_R,eye_L)
    


