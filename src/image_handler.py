import cv2

class ImageHandler():
    def __init__(self):
        pass

    def resize_photo(self, image):
        scale_percent = 30  # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        return resized

    def read_photo_and_write_it_on_right_folder(self, photo_path, folder_path):
        photo = cv2.imread(photo_path)
        photo_name = photo_path.split('/')[-1]
        cv2.imwrite(folder_path + '/' + photo_name, photo)


