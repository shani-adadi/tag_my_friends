import os
import cv2
from image_handler import ImageHandler
import face_recognition

def get_photos(path):
    """
    :param path:(str) the photos dir
    :return: (list) the photos list
    """
    photos_list = []
    subject_images_names = os.listdir(path)
    image_op = ImageHandler()
    for image_name in subject_images_names:
        if image_name.startswith("."):
            continue
        image_path = path + "/" + image_name
        try:
            image_normal_size = cv2.imread(image_path)
            image = image_op.resize_photo(image_normal_size)
            photos_list.append(image)
        except:
            continue
    return photos_list

def get_subjects_names_and_photos(path):
    """
    This func gets the names and the train photos of all friends
    :param path: (str) the name of the directory in which the user will upload the subjects photos as train data
    :return: (dict) keys - subjects name, values - the subjects photos list
    """
    train_data_dict = {}
    dirs = os.listdir(path)
    for dir_name in dirs:
        if dir_name.startswith("."):
            continue
        subject_dir_path = path + "/" + dir_name
        photos = get_photos(subject_dir_path)
        train_data_dict[dir_name] = photos
    return train_data_dict

def get_faces_list(train_data_dict):
    """
    This func gets only the faces from the training photos
    :param train_data_dict: (dict) keys - subjects names, values - the subjects photos list
    :return: dict in which the key is the subject name and the value is his faces photos list
    """
    train_faces_dict = {}
    none_photos = []
    for name, photos in train_data_dict.items():
        train_faces_dict[name] = []
        for index, photo in enumerate(photos):
            face, rect = face_recognition.detect_face_train(photo, name, index + 1)
            if face is not None:
                train_faces_dict[name].append(face)
            else:
                text = "Photo number {0} of {1} was't good!".format(index + 1, name)
                none_photos.append(text)
    return none_photos, train_faces_dict

if __name__ == '__main__':
    x = get_subjects_names_and_photos('friends')
    y = get_faces_list(x)