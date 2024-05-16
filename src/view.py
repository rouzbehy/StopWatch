from PyQt6.QtWidgets import (
    QDialog,
    QGridLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtCore import Qt
from PyQt6 import QtCore
from math import floor

WINDOW_SIZE_HEIGHT = 400
WINDOW_SIZE_WIDTH = 200

TICK_TIME = 1000


class Window(QDialog):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self._counted_seconds = 0
        self._timer = QtCore.QTimer()
        self._timer.setInterval(TICK_TIME)
        self._timer.timeout.connect(self.tick_forward)

        self.setWindowTitle("Timer")
        self.setFixedSize(WINDOW_SIZE_HEIGHT, WINDOW_SIZE_WIDTH)
        self._layout = QGridLayout()
        self._label = QLabel("00:00:00")
        self._label.setStyleSheet("font-size: 42px; ")
        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._layout.addWidget(self._label, 0, 0, 1, 3)

        self._start = QPushButton("Start")
        self._start.setStyleSheet("background-color: #1A9725")
        self._start.clicked.connect(self.click_start)

        self._pause = QPushButton("Pause")
        self._pause.setStyleSheet("background-color: #084EE5")
        self._pause.clicked.connect(self.click_pause)

        self._reset = QPushButton("Reset")
        self._reset.setStyleSheet("background-color: #F34E2B")
        self._reset.clicked.connect(self.click_reset)

        self._layout.addWidget(self._start, 1, 0)
        self._layout.addWidget(self._pause, 1, 1)
        self._layout.addWidget(self._reset, 1, 2)

        self.setLayout(self._layout)

    def keyPressEvent(self, a0):
        if a0:
            if a0.key() == Qt.Key.Key_Close:
                self.close()
            else:
                super().keyPressEvent(a0)

    def display_stopwatch(self):
        hours = floor(self._counted_seconds / 3600)
        minutes = floor((self._counted_seconds % 3600) / 60)
        seconds = floor(self._counted_seconds % 60)
        self._label.setText(f"{hours:>02}:{minutes:>02}:{seconds:>02}")

    def tick_forward(self):
        self._counted_seconds += 1
        self.display_stopwatch()

    def click_start(self):
        self._timer.start()
        self._start.clicked.disconnect()

    def click_pause(self):
        self._timer.stop()
        self._start.clicked.connect(self.click_start)

    def click_reset(self):
        self._counted_seconds = 0
        self.display_stopwatch()
