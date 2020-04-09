import os
import cv2

class FolderHandler:
    def __init__(self):
        pass

    def create_folder(self, folder_name):
        """
        Creates folder for each friend in friends folder
        :param folder_name: (str) the friend name
        :return:
        """
        try:
            folder_path = './friends/{0}'.format(folder_name)
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
                return folder_path
            return folder_path
        except OSError as error:
            return error

    def write_tagged_photos(self, photos_path, photos_dict):
        """
        Writes the tagged photos in a new folder under the friend name
        :param photos_path: (str) the path for the photos needs to be tagged
        :param photos_dict: (dict) key - the friend name, value - friends photos list
        """
        for name, photos in photos_dict.items():
            index = 0
            folder_path = photos_path + '/' + name
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
            for photo in photos:
                photo_name = folder_path + '/' + str(index) + '.jpg'
                cv2.imwrite(photo_name, photo)
                index += 1


