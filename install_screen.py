""" Import necessary modules for the program to work """
import sys
import os
import random
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout
from PyQt5.QtGui import QFont, QFontDatabase, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

""" Create a class for the installation UI """
class InstallScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Talon Installer")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowState(Qt.WindowFullScreen | Qt.WindowActive)
        self.load_chakra_petch_font()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        title_label = QLabel("Installing Talon...")
        title_label.setStyleSheet("color: white; font-weight: bold;")
        title_label.setFont(QFont("Chakra Petch", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Joke Label
        self.joke_label = QLabel("")
        self.joke_label.setStyleSheet("color: white; font-style: italic;")
        self.joke_label.setFont(QFont("Chakra Petch", 16))
        self.joke_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.joke_label)

        body_label = QLabel("This may take a few minutes. Do not turn your PC off.")
        body_label.setStyleSheet("color: white;")
        body_label.setFont(QFont("Chakra Petch", 18))
        body_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(body_label)

        layout.addSpacing(30)

        spinner_layout = QHBoxLayout()
        spinner_layout.setAlignment(Qt.AlignCenter)
        self.spinner = LoadingSpinner()
        spinner_layout.addWidget(self.spinner)
        self.spinner.start_spinning()
        layout.addLayout(spinner_layout)

        self.setLayout(layout)

        # List of jokes
        self.jokes = [
            "Why did the computer go to therapy? It had too many Windows.",
            "Installing software is like making a sandwich… it’s all fun until you forget the cheese.",
            "I would tell you a UDP joke, but you might not get it.",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Debugging is like being the detective in a crime movie where you are also the murderer.",
            "Why do Java developers wear glasses? Because they don’t C#!",
            "There are 10 kinds of people in the world: those who understand binary and those who don’t.",
            "My computer suddenly started belting out 'Someone Like You.' Turns out it’s a Dell.",
            "I changed my password to 'incorrect.' So whenever I forget, my computer reminds me: 'Your password is incorrect.'",
            "Artificial intelligence is no match for natural stupidity."
        ]

        # Timer to change jokes
        self.joke_timer = QTimer(self)
        self.joke_timer.timeout.connect(self.show_random_joke)
        self.joke_timer.start(5000)  # Change joke every 5 seconds
        self.show_random_joke()  # Show first joke immediately

    def show_random_joke(self):
        self.joke_label.setText(random.choice(self.jokes))

    """ Load the Chakra Petch font, which is used for the UI """
    def load_chakra_petch_font(self):
        try:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))
            font_path = os.path.join(base_path, "ChakraPetch-Regular.ttf")
            font_id = QFontDatabase.addApplicationFont(font_path)
            if font_id == -1:
                print("Failed to load font.")
            else:
                print("Font loaded successfully.")
        except Exception as e:
            print(f"Error loading font: {e}")

""" Create a class for the loading spinner in the UI """
class LoadingSpinner(QFrame):
    """ Initialization """
    def __init__(self):
        super().__init__()
        self.setFixedSize(100, 100)
        self.setStyleSheet("background-color: transparent;")
        self.angle = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    """ Use QPainter to draw the spinner """
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(255, 255, 255))
        pen.setWidth(6)
        painter.setPen(pen)
        painter.setBrush(Qt.transparent)
        rect = self.rect()
        painter.drawArc(rect.adjusted(10, 10, -10, -10), self.angle * 16, 100 * 16)

    """ Begin spinning """
    def start_spinning(self):
        self.angle = 0
        self.update()
        
    """ Update the spinner to spin """
    def update(self):
        self.angle -= 5
        if self.angle <= -360:
            self.angle = 0
        super().update()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = InstallScreen()
    window.show()
    sys.exit(app.exec_())
