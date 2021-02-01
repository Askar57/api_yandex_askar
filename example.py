import os
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.getImage()
        self.initUI()

    def getImage(self):
        map_request = "https://static-maps.yandex.ru/1.x/?ll=37.677751,55.757718&spn=0.016457,0.00619&l=map"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Полученное изображение конвертируем в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        self.setGeometry(500, 200, 450, 450)
        self.setWindowTitle('Отображение карты')

        # Изображение
        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(450, 450)
        self.image.setPixmap(self.pixmap)

    # Закрываем и удаляем png файл
    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())