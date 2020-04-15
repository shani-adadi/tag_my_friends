# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from files_handler import FolderHandler
from image_handler import ImageHandler
from main_alg import MainAlg

class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(626, 781)
        MainWindow.setMouseTracking(True)
        MainWindow.setToolTipDuration(4)
        MainWindow.setStyleSheet("#MainWindow {\n"
        "background: gray;\n"
        "}\n"
        "\n"
        "\n"
        "#MainWindow {\n"
        "border: 3px solid gray;\n"
        "border-radius: 40px;\n"
        "background: white;\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 300, 631, 160))
        self.textBrowser.setObjectName("textBrowser")
        self.Main = QtWidgets.QLabel(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(0, 0, 651, 761))
        self.Main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Main.setObjectName("Main")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 600, 631, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.photos_file_path = QtWidgets.QLabel(self.centralwidget)
        self.photos_file_path.setGeometry(QtCore.QRect(10, 540, 161, 31))
        self.photos_file_path.setObjectName("photos_file_path")

        self.line_photos_path = QtWidgets.QLineEdit(self.centralwidget)
        self.line_photos_path.setGeometry(QtCore.QRect(195, 550, 261, 21))
        self.line_photos_path.setObjectName("line_photos_path")

        self.upload_photo_tag = QtWidgets.QLabel(self.centralwidget)
        self.upload_photo_tag.setGeometry(QtCore.QRect(10, 510, 180, 31))
        self.upload_photo_tag.setObjectName("upload_photo_tag")

        self.line_upload_photo = QtWidgets.QLineEdit(self.centralwidget)
        self.line_upload_photo.setGeometry(QtCore.QRect(195, 520, 261, 21))
        self.line_upload_photo.setObjectName("line_upload_photo")

        self.browse_photo = QtWidgets.QPushButton(self.centralwidget)
        self.browse_photo.setGeometry(QtCore.QRect(460, 520, 71, 31))
        self.browse_photo.setObjectName("browse_photo")
        self.browse_photo.clicked.connect(self.browse_photo_slot)


        self.browse_path = QtWidgets.QPushButton(self.centralwidget)
        self.browse_path.setGeometry(QtCore.QRect(460, 550, 71, 31))
        self.browse_path.setObjectName("browse_path")
        self.browse_path.clicked.connect(self.browse_photos_file_slot)


        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(540, 520, 71, 31))
        self.upload.setObjectName("upload")
        self.upload.clicked.connect(self.upload_button)

        self.line_friend_name = QtWidgets.QLineEdit(self.centralwidget)
        self.line_friend_name.setGeometry(QtCore.QRect(195, 490, 261, 21))
        self.line_friend_name.setObjectName("line_friend_name")

        self.friend_name_tag = QtWidgets.QLabel(self.centralwidget)
        self.friend_name_tag.setGeometry(QtCore.QRect(10, 490, 161, 31))
        self.friend_name_tag.setObjectName("friend_name_tag")

        self.debuging_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.debuging_text.setGeometry(QtCore.QRect(90, 610, 450, 61))
        self.debuging_text.setObjectName("debuging_text")

        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(260, 690, 113, 32))
        self.start.setObjectName("start")
        self.start.clicked.connect(self.start_def)

        self.debugging_string = ''
        self.Main.raise_()
        self.textBrowser.raise_()
        self.frame.raise_()
        self.photos_file_path.raise_()
        self.line_photos_path.raise_()
        self.upload_photo_tag.raise_()
        self.line_upload_photo.raise_()
        self.browse_photo.raise_()
        self.browse_path.raise_()
        self.upload.raise_()
        self.line_friend_name.raise_()
        self.friend_name_tag.raise_()
        self.debuging_text.raise_()
        self.start.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.current_photo_path = None
        self.photos_folder_path = None

    def get_browse_path(self):
        """
        Get path for photos file
        """
        title = "Choose a destination"
        flags = QtWidgets.QFileDialog.ShowDirsOnly
        folder_path = str(QtWidgets.QFileDialog.getExistingDirectory(None, title, '', flags))
        self.photos_folder_path = folder_path
        self.line_photos_path.setText(folder_path)

    def get_photo(self):
        """
        Gets the photo given the path the user choose before
        """
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        folder_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)
        return folder_path

    def write_debugging(self, text):
        """
        Write text on debugging widget
        :param text: the text we wants to write
        """
        self.debugging_string = text + '\n' + self.debugging_string
        self.debuging_text.hide()
        self.debuging_text.setText(self.debugging_string)
        self.debuging_text.show()


    @pyqtSlot()
    def upload_button(self):
        """
        Activate the algorithm that puts the photos the user wants to upload on the fight folder
        """
        if self.current_photo_path:
            folder_obj = FolderHandler()
            image_op = ImageHandler()
            name = self.line_friend_name.text()
            if not name:
                self.write_debugging('Hey you! :) You must enter friend name first')
                return
            folder_path = folder_obj.create_folder(name)
            if folder_path:
                image_op.read_photo_and_write_it_on_right_folder(self.current_photo_path, folder_path)
            else:
                self.write_debugging("Something went wrong and we can't create a folder")
        self.write_debugging('Photo {0} of {1} was uploaded'.format(self.current_photo_path.split('/')[-1], self.line_friend_name.text()))


    @pyqtSlot()
    def start_def(self):
        """
        Starts the algorithm for face recognition
        """
        if self.photos_folder_path == None:
            self.write_debugging('You must enter a photos path first :)')
            return
        else:
            self.write_debugging('Great! it will take a while, be patient')
        alg = MainAlg()
        self.write_debugging('Preparing data')
        prepare_text, none_photos = alg.prepare_data()
        for line in none_photos:
                self.write_debugging(line)
        self.write_debugging(prepare_text)
        training_text = alg.train_the_model()
        self.write_debugging(training_text)
        alg.start_prediction(self.photos_folder_path)
        self.write_debugging('Finished! :)')

    @pyqtSlot()
    def browse_photo_slot(self):
        """
        Handles user photos upload
        :return:
        """
        photo_path = self.get_photo()
        if photo_path:
            self.current_photo_path = photo_path
            self.line_upload_photo.hide()
            self.line_upload_photo.setText(photo_path)
            self.line_upload_photo.show()

    @pyqtSlot()
    def browse_photos_file_slot(self):
        """
        Handles users photos file location
        """
        folder_path = self.get_browse_path()
        if folder_path:
            self.photos_folder_path = folder_path
            self.line_photos_path.setText(folder_path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Share My Photos "))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">Wellcome ! :)</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">We all want to share those amazing moments with the people we love</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">and now it\'s so easy!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">1. On Friend\'s name line, write the name of the friend to want to share the photos with</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">2. Upload at the Upload 5+ friends test photos line one photo each time. As more you photos upload, the system gets it will learn better</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">3. Choose the folder in which you have the photos you want the share</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#35408c;\">4. Finally, press let\'s do it! give it a few moments and don\'t worry, the system will create on the photos folder new folders to each friend with his photos</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Main.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"./beach-background-with-sunglasses-starfish_1101-313.jpg\"/></p></body></html>"))
        self.photos_file_path.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#eee709; vertical-align:sub;\">Where are all the photos?</span></p><p><br/></p></body></html>"))
        self.upload_photo_tag.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#eee709; vertical-align:sub;\">Upload 5+ friends test photos</span></p></body></html>"))
        self.browse_photo.setText(_translate("MainWindow", "Browse"))
        self.browse_path.setText(_translate("MainWindow", "Browse"))
        self.upload.setText(_translate("MainWindow", "Upload"))
        self.friend_name_tag.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#eee709; vertical-align:sub;\">Friend's name</span></p><p><br/></p></body></html>"))
        self.debuging_text.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.start.setText(_translate("MainWindow", "Let's do it!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
