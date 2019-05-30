# import the libraries
import os
import face_recognition

# make a list of all the available images
list_of_images = os.listdir('images')

# load your test image
image_to_be_matched = face_recognition.load_image_file('my_image.jpg')

# encode the loaded image into a feature vector
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]

# iterate over each image
for image in list_of_images:

    # load the next image in the list
    current_image = face_recognition.load_image_file("images/" + image)
    
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    
    # match your test image with the current image and check if it matches
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
        
    # check if it was a match
    if result[0] == True:
        print ("Matched: " + image)
    else:
        print ("Not matched: " + image)
