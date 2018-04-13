import sys
import os
import urllib.request
import re

from PyQt5 import QtGui

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout

from PyQt5.QtWidgets import QAction, qApp, QMainWindow


class IpFinder(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()

        self.link_ac = QPushButton("Link Aç")
        self.ac = QPushButton("Dosya Aç")
        self.ip = QPushButton("IP Bul")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.link_ac)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.ip)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("IP Finder in Text")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'logo.png'))
        self.link_ac.clicked.connect(self.yaziyi_link_ac)
        self.ac.clicked.connect(self.dosya_ac)
        self.ip.clicked.connect(self.ip_bul)
        self.kaydet.clicked.connect(self.dosya_kaydet)

    def yaziyi_link_ac(self):
        dosya_url = self.yazi_alani.toPlainText()
        dosya_ismi = str(urllib.request.urlopen(dosya_url).readlines())
        self.yazi_alani.setText(dosya_ismi)

    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))

        with open(dosya_ismi[0], "r") as file:
            self.yazi_alani.setText(file.read())

    def ip_bul(self):
        ip = re.findall("[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}", self.yazi_alani.toPlainText())
        str1 = "\n".join(ip)
        self.yazi_alani.setText(str1)

    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Kaydedilecek Dosya", os.getenv("HOME"))

        with open(dosya_ismi[0], "w") as file:
            file.write(self.yazi_alani.toPlainText())


class Menu(QMainWindow):

    def __init__(self):

        super().__init__()

        self.pencere = IpFinder()

        self.setCentralWidget(self.pencere)

        self.menuleri_olustur()

    def menuleri_olustur(self):

        menubar = self.menuBar()

        dosya = menubar.addMenu("Menü")

        dosya_ac = QAction("Dosya Aç", self)
        dosya_ac.setShortcut("Ctrl+O")

        link_ac = QAction("Link Aç", self)
        link_ac.setShortcut("Ctrl+L")

        ip_bul = QAction("IP Bul", self)
        ip_bul.setShortcut("Ctrl+K")

        kaydet = QAction("Kaydet", self)
        kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Çıkış", self)

        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(link_ac)
        dosya.addAction(ip_bul)
        dosya.addAction(kaydet)
        dosya.addAction(cikis)

        dosya.triggered.connect(self.response)

        self.setWindowTitle("IP Finder in Text")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'ipfinder.ico'))

        self.show()

    def response(self, action):

        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()

        elif action.text() == "Link Aç":
            self.pencere.yaziyi_link_ac()

        elif action.text() == "IP Bul":
            self.pencere.ip_bul()

        elif action.text() == "Kaydet":
            self.pencere.kaydet()


        elif action.text() == "Çıkış":
            qApp.quit()


app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())

# Mehmet Fatih Okuyan
