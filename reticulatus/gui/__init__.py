from PySide.QtGui import QMainWindow, QPushButton, QApplication
from .reticulate_main import Ui_MainWindow



class App(QApplication):
    pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
