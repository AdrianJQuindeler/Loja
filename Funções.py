from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtGui

class Funcoes:
    def createImage(self, parent, leftDistance, topDistance, path, width = 100, height = 100):
        image = QLabel(parent)
        image.move(leftDistance, topDistance)
        image.resize(width, height)
        image.setPixmap(QtGui.QPixmap(path))
        return image

    def createLabel(self, parent, text, leftDistance, topDistance, width, height, style):
        label = QLabel(parent)
        label.setWordWrap(True)
        label.setText(text)
        label.move(leftDistance, topDistance)
        label.resize(width, height)
        label.setStyleSheet(style)

    def createButton(self, parent, text, leftDistance, topDistance, width, height, style):
        button = QPushButton(text, parent)
        button.move(leftDistance, topDistance)
        button.resize(width, height)
        button.setStyleSheet(style)
        return button

    def createItemToAdd(self, parent, leftDistance, topDistance, path, description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        image = self.createImage(parent, leftDistance, topDistance, path)
        label = self.createLabel(parent, description, leftDistance+110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        addToCart = self.createButton(parent, "+", leftDistance+90, topDistance+90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return addToCart

    def createItemToAddRemove(self, parent, leftDistance, topDistance, path, description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        image = self.createImage(parent, leftDistance, topDistance, path)
        label = self.createLabel(parent, description, leftDistance+110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        addToCart = self.createButton(parent, "+", leftDistance+90, topDistance+90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return addToCart
    
    def createItemInCart(self, parent, leftDistance, topDistance, path, quantity, description = "R$ 00,00"):
        fundo = self.createLabel(parent, description, leftDistance+110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        image = self.createImage(parent, leftDistance, topDistance, path)
        label = self.createLabel(parent, description, leftDistance+110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        quantity = self.createLabel(parent, quantity, leftDistance+90, topDistance+90, 25, 25, 
                            ("QLabel {font: bold; background: black; font-size: 45px; color: white;  padding: 10px}"))