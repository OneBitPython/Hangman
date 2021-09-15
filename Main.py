from PyQt5 import QtWidgets
import PyQt5
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QInputDialog,
    QFileDialog,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtCore import QThread
from PyQt5.uic import loadUi
import sys
import threading
import time as t
from nltk.corpus import words
from all_images import *
import time
import pyttsx3
from scores import *
from pygame import mixer
import random


class hangman(QMainWindow):
    def __init__(self):
        super(hangman, self).__init__()
        loadUi("hangman_gui.ui", self)

        self.textedit.setText(seventh)
        self.InitUi()
        self.words_guessed = []

        length = len(self.text)
        if length <= 4:
            self.completed = 40
        elif 5 <= length <= 8:
            self.completed = 100
        else:
            self.completed = 16

        self.lcdNumber.display(self.completed)
        self.player1_score.setText(str(player1))
        self.player2_score.setText(str(player2))

    def speak(self, text):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")

        self.engine.setProperty("voice", self.voices[0].id)

        self.engine.say(text)
        self.engine.runAndWait()

    def InitUi(self):
        self.play_mus.setEnabled(False)
        self.play_mus.setStyleSheet("background-color:grey")
        time.sleep(3)
        self.play_mus.setStyleSheet("background-color:#00007f")
        self.play_mus.setEnabled(True)

        self.A.clicked.connect(self.a)
        self.B.clicked.connect(self.b)
        self.C.clicked.connect(self.c)
        self.D.clicked.connect(self.d)
        self.E.clicked.connect(self.e)
        self.F.clicked.connect(self.f)
        self.G.clicked.connect(self.g)
        self.H.clicked.connect(self.h)
        self.I.clicked.connect(self.i)
        self.J.clicked.connect(self.j)
        self.K.clicked.connect(self.k)
        self.L.clicked.connect(self.l)
        self.M.clicked.connect(self.m)
        self.N.clicked.connect(self.n)
        self.O.clicked.connect(self.o)
        self.P.clicked.connect(self.p)
        self.Q.clicked.connect(self.q)
        self.R.clicked.connect(self.r)
        self.S.clicked.connect(self.s)
        self.T.clicked.connect(self.t)
        self.U.clicked.connect(self.u)
        self.V.clicked.connect(self.v)
        self.W.clicked.connect(self.w)
        self.X.clicked.connect(self.x)
        self.Y.clicked.connect(self.y)
        self.Z.clicked.connect(self.z)

        self.close_hang.clicked.connect(self.close_program)

        self.my_thread = threading.Thread(target=self.play_music)
        self.start.clicked.connect(self.start_program)

        self.reset.clicked.connect(self.reset_score)
        self.play_mus.clicked.connect(self.play_music)
        self.stop_mus.clicked.connect(self.stop_music)

        self.starting()

    def play_music(self):
        self.songs = [
            "C:\\Users\\acham\\Favorites\\Downloads\\Godzilla (feat. Juice WRLD) [Official Audio].mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Avicii - The Nights.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Avicii - Wake Me Up.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Eminem - Lose Yourself.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Avicii, Aloe Blacc – SOS 🎵.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Eminem - The Real Slim Shady [HD & HQ].mp3.crdownload.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Pitbull - Feel This Moment ft. Christina Aguilera.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Ed Sheeran - Beautiful People (feat. Khalid) [Official].mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Axwell Λ Ingrosso - More Than You Know (Official Video).mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Eminem - The Real Slim Shady [HD & HQ]Eminem - The Real Slim Shady [HD & HQ]",
            "C:\\Users\\acham\\Favorites\\Downloads\\DJ Khaled - I m The One ft. Justin Bieber, Quavo, Chance the Rapper, Lil Wayne.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Congratulations.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Sing - I m Still Standing Taron Egerton.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Maroon 5 - Wait.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Maroon 5 - What Lovers Do ft. SZA (Official Music Video).mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Lil Tecca - Ransom.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Ed Sheeran - Galway Girl [Official Video].mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Ed Sheeran, Camila Cabello - South of the Border ft. Cardi B.mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Ed Sheeran & Justin Bieber - I Don t Care [Official].mp3",
            "C:\\Users\\acham\\Favorites\\Downloads\\Axwell Λ Ingrosso - Renegade.mp3",
        ]
        self.song = random.choice(self.songs)

        mixer.init()

        self.play_mus.setEnabled(False)
        self.play_mus.setStyleSheet("background-color:grey")

        mixer.music.set_volume(0.4)
        mixer.music.load(self.song)
        mixer.music.play()

    def stop_music(self):
        mixer.music.stop()

        self.play_mus.setStyleSheet("background-color:#00007f")
        self.play_mus.setEnabled(True)

    def reset_score(self):
        with open("scores.py", "w+") as f:
            f.write(f"player1 = {0}")
            f.write("\n")
            f.write(f"player2 = {0}")
        self.player1_score.setText(str(0))
        self.player2_score.setText(str(0))

    def starting(self):
        self.text, ok = QInputDialog.getText(
            self, "Player 1", "What do you want the word to be?"
        )
        if ok:
            if " " in self.text.strip():
                print("*No spaces!")
                self.text, ok = QInputDialog.getText(
                    self, "Player 1", "What do you want the word to be?"
                )

            while len(self.text) > 12:
                print("*Too long!")
                self.text, ok = QInputDialog.getText(
                    self, "Player 1", "What do you want the word to be?"
                )

            while self.text.strip() == "":
                print("*Invalid!")
                self.text, ok = QInputDialog.getText(
                    self, "Player 1", "What do you want the word to be?"
                )

            # if self.text not in words.words():
            #     self.msg = QMessageBox()
            #     self.msg.setWindowTitle("Info")
            #     self.msg.setText(
            #         "This is not an actual word, is this what you actually meant?"
            #     )
            #     self.msg.setIcon(QMessageBox.Warning)
            #     self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            #     self.msg.setDefaultButton(QMessageBox.Yes)

            #     self.msg.setDetailedText(
            #         "This might be because of a spelling mistake or because you have two words merged together."
            #     )

            #     self.msg.buttonClicked.connect(self.answer)

            #     x = self.msg.exec_()

            self.start_program()
            self.info.setText("")
            self.text = self.text.lower()
            self.text = str(self.text)
            self.text = self.text.strip()
        else:
            sys.exit()

    def answer(self, i):
        # if i.text() == "&Yes":
        #     pass
        # else:
        # self.msg.done(1)
        self.starting()

    def start_program(self):
        my_thread = threading.Thread(target=self.main_program)

        my_thread.start()

    def main_program(self):

        self.start.setEnabled(False)

        my_list = []
        for i in range(len(self.text)):
            my_list.append("_")

        for_fun = ""
        for i in my_list:
            for_fun += i
            for_fun += " "
        self.word_so_far.setText(for_fun)

        the_list = []

        thread = threading.Thread(target=self.show_time)
        thread.start()
        while True:
            try:
                if self.completed <= 0:
                    self.info.setText(
                        f"Congrats {self.player1_name.text()} has won the game."
                    )
                    self.speak("Time up!")
                    self.speak(f"Congrats {self.player1_name.text()} has won the game.")

                    with open("scores.py", "w+") as f:
                        f.write(f"player1 = {player1 + 1}")
                        f.write("\n")
                        f.write(f"player2 = {player2}")

                    score = player1 + 1

                    self.player1_score.setText(str(score))
                    self.player2_score.setText(str(player2))
                    break

                for i in self.words_guessed:
                    if i not in self.text and i not in the_list:
                        the_list.append(i)

                chances = 7 - len(the_list)
                self.you_got_chance.setText(str(chances))

                letter = self.letter
                letter = letter.lower()
                letter = letter.strip()

                for i in range(len(self.text)):
                    if self.text[i] == letter:
                        my_list[i] = letter
                        self.info.setText("")

                if letter not in self.text:
                    self.info.setText(f"LETTER {letter} was not there in the word.")

                final = ""
                for i in my_list:
                    final += i.upper()
                    final += " "

                self.word_so_far.setText(final)

                if "_" not in my_list:
                    self.info.setText(
                        f"Congrats {self.player2_name.text()} has won the game."
                    )
                    self.speak(f"Congrats {self.player2_name.text()} has won the game.")

                    with open("scores.py", "w+") as f:
                        f.write(f"player1 = {player1}")
                        f.write("\n")
                        f.write(f"player2 = {player2 + 1}")

                    self.player1_score.setText(str(player1))

                    score = player2 + 1
                    self.player2_score.setText(str(score))
                    break

                if chances == 0:
                    self.textedit.setText(zero)
                    self.info.setText(
                        f"{self.player1_name.text()} won, the word was {self.text.upper()}"
                    )
                    self.speak(
                        f"{self.player1_name.text()} won, the word was {self.text.upper()}"
                    )

                    with open("scores.py", "w+") as f:
                        f.write(f"player1 = {player1+1}")
                        f.write("\n")
                        f.write(f"player2 = {player2}")

                    score = player1 + 1

                    self.player1_score.setText(str(score))
                    self.player2_score.setText(str(player2))

                    break

                if chances == 6:
                    self.textedit.setText(sixth)

                if chances == 5:
                    self.textedit.setText(fifth)

                if chances == 4:
                    self.textedit.setText(fourth)

                if chances == 3:
                    self.textedit.setText(third)

                if chances == 2:
                    self.textedit.setText(two)

                if chances == 1:
                    self.textedit.setText(one)
            except:
                pass

        mixer.music.stop()

    def show_time(self):
        while self.completed >= 0:
            self.lcdNumber.display(self.completed)
            self.completed -= 1
            QThread.sleep(1)

    def close_program(self):
        window.close()

    def a(self):
        self.letter = "a"
        self.A.setStyleSheet("background-color:grey")
        self.A.setEnabled(False)

        self.words_guessed.append(self.letter)

    def b(self):
        self.letter = "b"
        self.B.setStyleSheet("background-color:grey")
        self.B.setEnabled(False)
        self.words_guessed.append(self.letter)

    def c(self):
        self.letter = "c"
        self.C.setStyleSheet("background-color:grey")
        self.C.setEnabled(False)
        self.words_guessed.append(self.letter)

    def d(self):
        self.letter = "d"
        self.D.setStyleSheet("background-color:grey")
        self.D.setEnabled(False)
        self.words_guessed.append(self.letter)

    def e(self):
        self.letter = "e"
        self.E.setStyleSheet("background-color:grey")
        self.E.setEnabled(False)
        self.words_guessed.append(self.letter)

    def f(self):
        self.letter = "f"
        self.F.setStyleSheet("background-color:grey")
        self.F.setEnabled(False)
        self.words_guessed.append(self.letter)

    def g(self):
        self.letter = "g"
        self.G.setStyleSheet("background-color:grey")
        self.G.setEnabled(False)
        self.words_guessed.append(self.letter)

    def h(self):
        self.letter = "h"
        self.H.setStyleSheet("background-color:grey")
        self.H.setEnabled(False)
        self.words_guessed.append(self.letter)

    def i(self):
        self.letter = "i"
        self.I.setStyleSheet("background-color:grey")
        self.I.setEnabled(False)
        self.words_guessed.append(self.letter)

    def j(self):
        self.letter = "j"
        self.J.setStyleSheet("background-color:grey")
        self.J.setEnabled(False)
        self.words_guessed.append(self.letter)

    def k(self):
        self.letter = "k"
        self.K.setStyleSheet("background-color:grey")
        self.K.setEnabled(False)
        self.words_guessed.append(self.letter)

    def l(self):
        self.letter = "l"
        self.L.setStyleSheet("background-color:grey")
        self.L.setEnabled(False)
        self.words_guessed.append(self.letter)

    def m(self):
        self.letter = "m"
        self.M.setStyleSheet("background-color:grey")
        self.M.setEnabled(False)
        self.words_guessed.append(self.letter)

    def n(self):
        self.letter = "n"
        self.N.setStyleSheet("background-color:grey")
        self.N.setEnabled(False)
        self.words_guessed.append(self.letter)

    def o(self):
        self.letter = "o"
        self.O.setStyleSheet("background-color:grey")
        self.O.setEnabled(False)
        self.words_guessed.append(self.letter)

    def p(self):
        self.letter = "p"
        self.P.setStyleSheet("background-color:grey")
        self.P.setEnabled(False)
        self.words_guessed.append(self.letter)

    def q(self):
        self.letter = "q"
        self.Q.setStyleSheet("background-color:grey")
        self.Q.setEnabled(False)
        self.words_guessed.append(self.letter)

    def r(self):
        self.letter = "r"
        self.R.setStyleSheet("background-color:grey")
        self.R.setEnabled(False)
        self.words_guessed.append(self.letter)

    def s(self):
        self.letter = "s"
        self.S.setStyleSheet("background-color:grey")
        self.S.setEnabled(False)
        self.words_guessed.append(self.letter)

    def t(self):
        self.letter = "t"
        self.T.setStyleSheet("background-color:grey")
        self.T.setEnabled(False)
        self.words_guessed.append(self.letter)

    def u(self):
        self.letter = "u"
        self.U.setStyleSheet("background-color:grey")
        self.U.setEnabled(False)
        self.words_guessed.append(self.letter)

    def v(self):
        self.letter = "v"
        self.V.setStyleSheet("background-color:grey")
        self.V.setEnabled(False)
        self.words_guessed.append(self.letter)

    def w(self):
        self.letter = "w"
        self.W.setStyleSheet("background-color:grey")
        self.W.setEnabled(False)

        self.words_guessed.append(self.letter)

    def x(self):
        self.letter = "x"
        self.X.setStyleSheet("background-color:grey")
        self.X.setEnabled(False)
        self.words_guessed.append(self.letter)

    def y(self):
        self.letter = "y"
        self.Y.setStyleSheet("background-color:grey")
        self.Y.setEnabled(False)
        self.words_guessed.append(self.letter)

    def z(self):
        self.letter = "z"
        self.Z.setStyleSheet("background-color:grey")
        self.Z.setEnabled(False)
        self.words_guessed.append(self.letter)


app = QApplication(sys.argv)
window = hangman()
window.show()
app.exec_()
