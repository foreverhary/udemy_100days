import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QLabel


class MileToKM(QWidget):
    def __init__(self):
        super(MileToKM, self).__init__()
        self.setLayout(layout := QGridLayout())
        layout.addWidget(miles := QLineEdit(), 0, 1)
        layout.addWidget(QLabel('Miles'), 0, 2)
        layout.addWidget(QLabel('is equal to'), 1, 0)
        layout.addWidget(km := QLabel(), 1, 1)
        layout.addWidget(QLabel('Km'), 1, 2)
        self.miles = miles
        self.km = km
        self.connect_event()
        self.show()

    def connect_event(self):
        self.miles.textChanged.connect(self.calculate_miles_to_km)

    def calculate_miles_to_km(self):
        miles = int(self.miles.text())
        km = int(miles * 1.609344)
        self.km.setText(str(km))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MileToKM()
    sys.exit(app.exec_())
