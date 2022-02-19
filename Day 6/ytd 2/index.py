from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from pytube import YouTube
from pytube import Playlist
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog)

MainUI, _ = loadUiType('main.ui')


class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handlebuttons()
        self.setdefault()
        self.tabWidget.setCurrentIndex(0)

    def handlebuttons(self):
        self.pushButton.clicked.connect(self.openVdownload)
        self.pushButton_2.clicked.connect(self.openPlaylistdown)
        self.pushButton_3.clicked.connect(self.aboutus)
        self.pushButtonGo.clicked.connect(self.go)

    def setdefault(self):
        self.tabWidget.tabBar().setVisible(False)
        q = ['High Quality', 'Low Quality']
        self.comboBox.addItems(q)
        self.comboBoxq.addItems(q)
        self.lblMsg.setText("")
        self.lblMsg2.setText("")
        self.lblCount.setText("")
        self.lblTitle.setText("")
        self.lblViews.setText("")
        self.lblRating.setText("")
        self.lblDuration.setText("")
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)

    def go(self):
        if self.lineEdit.text().strip() == "":
            self.lblMsg.setText("Please Enter a URL...")
        else:
            try:
                link = self.lineEdit.text()
                self.lblMsg.setText("")
                self.lblTitle.setText("")
                self.lblViews.setText("")
                self.lblRating.setText("")
                self.lblDuration.setText("")

                video = YouTube(link)
                self.lblTitle.setText(str(f"Title: [video.title]"))

                self.lblViews.setText(str(f"Views: [video.views]"))
                self.lblRating.setText(str(f"Rating: [video.rating]"))
                self.lblDuration.setText(str(f"Duration: [video.length/60] Minutes"))

            except:
                pass

    def go2(self):
        pass

    def downloadV(self):
        pass

    def downloadP(self):
        pass

    def browse(self):
        pass

    def browse2(self):
        pass

    def openVdownload(self):
        self.tabWidget.setCurrentIndex(1)

    def openPlaylistdown(self):
        self.tabWidget.setCurrentIndex(1)

    def aboutus(self):
        self.tabWidget.setCurrentIndex(2)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
