import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5 import QtGui
from viewer import Ui_Form
import cv2
import time
import funcions as f


class ApplicationWindow(QtWidgets.QWidget):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.received_img = []
        self.rows = 0
        self.cols = 0
        self.counter = 0
        self.counter_2 = 0
        self.flag1 = bool
        self.flag2 = 0
        self.loop_flag = bool
        self.increment = 0

        self.ui.Browse_button.clicked.connect(self.img_browsing)
        self.ui.Play_button.clicked.connect(self.start_button)
        self.ui.Pause_button.clicked.connect(self.pause_button_)
        self.ui.Count_button.clicked.connect(self.line_edit_count)

    def img_browsing(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "","Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file

        if file_name:                              # If the user gives a file
            self.ui.progressBar.setProperty("value", 0)
            self.ui.TransImagelbl.clear()

            self.flag1 = False
            self.flag2 = 0
            self.loop_flag = True

            try:
                img = cv2.imread(file_name, 0)
                rows, cols = img.shape
                self.rows = rows
                self.cols = cols

                print(rows)

                self.received_img = img

                pixmapimage = f.array_to_pixmap(self.received_img)
                pixmapimage = QtGui.QPixmap.scaled(pixmapimage, self.ui.Imagelbl.width(), self.ui.Imagelbl.height(), QtCore.Qt.KeepAspectRatio)
                self.ui.Imagelbl.setPixmap(pixmapimage)

                if self.cols != self.rows or self.cols > 128 or self.rows > 128:
                    print("Enter a valid image size")
                    QMessageBox.about(self, "Invalid Image Size", "Please enter a valid Image")
                    self.ui.Imagelbl.clear()
                    sys.exit(-1)

            except:
                QMessageBox.about(self, "Invalid Image", "Please enter a valid Image")
                self.img_browsing()

        else:
            QMessageBox.about(self,"No Image Received", "Please Enter a Valid Image")
            self.img_browsing()


    def start_button(self):

        if self.flag2 % 2 == 0:             # sanity check to make sure every play click has an equivalent pause click
            self.flag2 = self.flag2 + 1

        if self.flag1 is False:
            self.counter = 0
            self.counter_2 = 0

        if self.flag1 and self.flag2 % 2 == 1:
            self.flag1 = False

        if self.loop_flag is True:

            while self.counter < self.cols // 2:

                # print("Top_Counter_1", self.counter)

                magnitude_spectrum = f.Bluring_FourierTransform(self.received_img, self.counter, self.cols, self.rows)

                pixmapimage = f.array_to_pixmap(magnitude_spectrum)
                pixmapimage = QtGui.QPixmap.scaled(pixmapimage, self.ui.Imagelbl.width(), self.ui.Imagelbl.height(),
                                                   QtCore.Qt.KeepAspectRatio)

                self.ui.TransImagelbl.setPixmap(pixmapimage)

                img_back = f.Bluring_InverseFourierTransform(self.received_img, self.counter, self.cols, self.rows)

                ipixmapimage = f.array_to_pixmap(img_back)
                ipixmapimage = QtGui.QPixmap.scaled(ipixmapimage, self.ui.Imagelbl.width(), self.ui.Imagelbl.height(),
                                                    QtCore.Qt.KeepAspectRatio)

                self.ui.Imagelbl.setPixmap(ipixmapimage)

                if self.flag1:
                    self.loop_flag = True
                    break

                # Sanity Check

                if self.counter + self.increment < 0:

                    self.pause_button_()

                    QMessageBox.about(self, "Invalid Increment", "Please enter positive values")

                elif self.increment == -1:

                    self.pause_button_()
                    QMessageBox.about(self, "Invalid Decrement", "Initial Increment Value will Be Restored , "
                                                                 "Press Play to continue")
                    self.increment = 0
                    self.counter = self.counter + 1
                    self.ui.Count_entry.setText(str(0))

                elif self.counter + self.increment >= self.cols // 2:

                    self.pause_button_()

                    QMessageBox.about(self, "Excess Increment", "Initial Increment Value will Be Restored , "
                                                                "Press Play to continue")
                    self.increment = 0
                    self.ui.Count_entry.setText(str(0))


                elif self.counter + self.increment > 0 or self.counter + self.increment < self.cols // 2:

                    print("i will increment \n")
                    self.counter += self.increment

                self.counter += 1

                self.ui.progressBar.setMaximum(self.cols//2)
                self.ui.progressBar.setProperty("value", self.counter)

                # print("Loop_1")
                # print("Counter", self.counter)
                # print("sum1 ", self.counter + self.increment)
                # print("slider value", self.ui.progressBar.value())
                # print("\n")

                QApplication.processEvents()
                time.sleep(0.1)

        if self.counter >= self.cols//2:  # Move to Next loop

            self.loop_flag = False
            self.ui.progressBar.setProperty("value", 0)
            self.counter_2 = 0

        if self.loop_flag is False:

            while self.counter_2 < self.cols // 2:

                # print("Top_Counter_2", self.counter_2)

                magnitude_spectrum = f.Edge_Detection_Fourier_Transform(self.received_img, self.counter_2, self.rows,
                                                                        self.cols)
                pixmapimage = f.array_to_pixmap(magnitude_spectrum)
                pixmapimage = QtGui.QPixmap.scaled(pixmapimage, self.ui.Imagelbl.width(), self.ui.Imagelbl.height(),
                                                   QtCore.Qt.KeepAspectRatio)

                self.ui.TransImagelbl.setPixmap(pixmapimage)

                img_back = f.Edge_Detection_Inverse_Fourier_Transform(self.received_img, self.counter_2, self.rows,
                                                                      self.cols)
                ipixmapimage = f.array_to_pixmap(img_back)
                ipixmapimage = QtGui.QPixmap.scaled(ipixmapimage, self.ui.Imagelbl.width(), self.ui.Imagelbl.height(),
                                                    QtCore.Qt.KeepAspectRatio)

                self.ui.Imagelbl.setPixmap(ipixmapimage)

                if self.flag1:
                    self.loop_flag = False
                    break

                # sanity check

                if self.counter_2 + self.increment < 0:

                    self.pause_button_()

                    QMessageBox.about(self, "Invalid Increment", "Please enter positive values")

                elif self.increment == -1:

                    self.pause_button_()
                    QMessageBox.about(self, "Invalid Decrement", "Initial Increment Value will Be Restored , "
                                                                 "Press Play to continue")
                    self.increment = 0
                    self.counter_2 = self.counter_2 + 1
                    self.ui.Count_entry.setText(str(0))

                elif self.counter_2 + self.increment >= self.cols // 2:

                    self.pause_button_()

                    QMessageBox.about(self, "Excess Increment",
                                      "Initial Increment Value Will Be Restored , Press Play to continue")
                    self.increment = 0
                    self.ui.Count_entry.setText(str(0))

                elif self.counter_2 + self.increment > 0 or self.counter_2 + self.increment < self.cols // 2:

                    self.counter_2 += self.increment

                self.counter_2 = self.counter_2 + 1

                self.ui.progressBar.setMaximum(self.cols // 2)
                self.ui.progressBar.setProperty("value", self.counter_2)

                # print("Loop_2")
                # print("Counter", self.counter_2)
                # print("sum1 ", self.counter_2 + self.increment)
                # print("slider value", self.ui.progressBar.value())
                # print("\n")

                QApplication.processEvents()
                time.sleep(0.1)

        if self.counter_2 >= self.cols//2:

            # print("Finished")
            # print("flag1", self.flag1)
            # print("flag2", self.flag2)
            # print("loop_flag", self.loop_flag)
            # print("counter_1", self.counter)
            # print("counter_2", self.counter_2)
            # print("\n")

            self.loop_flag = True
            self.flag1 = False
            self.counter = 0
            self.counter_2 = 0
            self.flag2 = 0

            # print("Finished_All")
            # print("flag1", self.flag1)
            # print("flag2", self.flag2)
            # print("loop_flag", self.loop_flag)
            # print("counter_1", self.counter)
            # print("counter_2", self.counter_2)



    def pause_button_(self):

        self.flag1 = True

        if self.flag2 % 2 == 1:        # sanity check to make sure every play click has an equivalent pause click
            self.flag2 = self.flag2 + 1

            self.counter = self.counter - 1
            self.counter_2 = self.counter_2 - 1

        # print("pause")
        # print('counter', self.counter)
        # print("counter2", self.counter_2)
        # print("flag1", self.flag1)
        # print("flag2", self.flag2)
        # print("loop_flag", self.loop_flag)
        # print("\n")

    def line_edit_count(self):

        try:
            increment = self.ui.Count_entry.text()
            increment = float(increment)
        except ValueError:
            QMessageBox.about(self, "Invalid Value ", "Please Enter Numbers Only")
            increment = 0
            self.ui.Count_entry.setText(str(0))
            self.line_edit_count()

        self.increment = int(increment)


def main():

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.setWindowTitle("Fourier Viewer")
    application.setWindowIcon(QtGui.QIcon("processing.jpg"))
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
