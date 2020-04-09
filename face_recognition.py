import cv2
import numpy as np
import prepare_data
# Face recognition tutorial  - https://www.superdatascience.com/blogs/opencv-face-recognition


def detect_face_train(img, subject_name, index):
    """
    :param img: (numpy array) the subjects photo
    :param subject_name: (str) the subjects name
    :param index: (int) the subjects photo index
    :return: (numpy array) only the face
    """
    # convert the test image to gray scale as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # detect all the faces in the image (some images may be closer to camera than others) result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    if len(faces) == 0:
        return None, None
    if len(faces) > 1:
        raise RuntimeError('There is more then one face in photo number {0} in {1} photos'.format(index,subject_name))
    (x, y, w, h) = faces[0]
    # return only the face part of the image
    return gray[y:y + w, x:x + h], faces[0]


def detect_face(img):
    """
    :param img: (numpy array) the subjects photo
    :return: (list) faces list that are in the photo
    """
    # convert the test image to gray scale as opencv face detector expects gray images
    faces_list = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # detect all the faces in the image (some images may be closer to camera than others) result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    if len(faces) == 0:
        return None, None
    for (x, y, w, h) in faces:
        only_the_face_part = gray[y:y + w, x:x + h]
        #cv2.imshow('test', only_the_face_part)
        #cv2.waitKey(0)
        faces_list.append(only_the_face_part)
    return faces_list


def train_face_recognition_model(face_dict):
    """
    This func train the face recognition model
    :param face_dict: (dict) keys - subjects name, values - subjects face photos
    :return: trained model
    """
    faces = []
    labels = []
    index = 1
    labels_dict = {}
    for name, face_photos in face_dict.items():
        labels_dict[index] = name
        for photo in face_photos:
            labels.append(index)
            faces.append(photo)
        index += 1
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(labels))
    return face_recognizer, labels_dict


def find_friend_in_image(image, face_recognizer):
    """
    :param image: (numpy array) the image to be labeled
    :param face_recognizer: the pre-trained model
    :return: (str) the label the model found as the most fit
    """
    label_list = []
    img = image.copy()
    faces = detect_face(img)
    for face in faces:
        if face is None:
            #cv2.imshow('None Photo', img)
            continue
        label = face_recognizer.predict(face)
        label_list.append(label)
    return label_list


def get_labeled_photos(path, face_recognizer, labels_dict):
    """
    :param path: (str) photos dir path
    :param face_recognizer: the pre- trained model
    :param labels_dict: (dict) labels dict, so the index will get his meaning
    :return: (dict) key - friend name, value - photos list
    """
    photos_dict = {}
    photos = prepare_data.get_photos(path)
    for photo in photos:
        labels = find_friend_in_image(photo, face_recognizer)
        for label in labels:
            name = labels_dict[label[0]]
            if name not in photos_dict.keys():
                photos_dict[name] = []
            photos_dict[name].append(photo)
    return photos_dict



