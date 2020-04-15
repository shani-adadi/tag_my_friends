import face_recognition
import prepare_data
from files_handler import FolderHandler

class MainAlg():
    def __init__(self):
        self.face_dict = {}
        self.face_recognizer = None
        self.labels_dict = {}

    def prepare_data(self):
        """
        Calling the functions that organize the data
        :return: the debugging text
        """

        print("Preparing data...")
        names_and_photos_dict = prepare_data.get_subjects_names_and_photos("friends")
        none_photos, self.face_dict = prepare_data.get_faces_list(names_and_photos_dict)
        print("Data prepared")
        return "Data prepared", none_photos

    def train_the_model(self):
        self.face_recognizer, self.labels_dict = face_recognition.train_face_recognition_model(self.face_dict)
        print("Predicting images...")
        return "Predicting images..."

    def start_prediction(self, photos_path):
        predicted_photos_dict = face_recognition.get_labeled_photos(photos_path, self.face_recognizer, self.labels_dict)
        folder_obj = FolderHandler()
        folder_obj.write_tagged_photos(photos_path, predicted_photos_dict)


