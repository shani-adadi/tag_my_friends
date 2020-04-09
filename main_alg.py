import face_recognition
import prepare_data
from files_handler import FolderHandler

def main(photos_path, UI):
    print("Preparing data...")
    names_and_photos_dict = prepare_data.get_subjects_names_and_photos("friends")
    face_dict = prepare_data.get_faces_list(names_and_photos_dict)
    print("Data prepared")
    face_recognizer, labels_dict = face_recognition.train_face_recognition_model(face_dict)
    print("Predicting images...")
    predicted_photos_dict = face_recognition.get_labeled_photos(photos_path, face_recognizer, labels_dict)
    folder_obj = FolderHandler()
    folder_obj.write_tagged_photos(photos_path, predicted_photos_dict)


