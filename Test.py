import pickle
import csv
import random
import datetime
import string

from Year import Year
from Participant import Participant

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

YEAR_DATA = "Years.csv"
PLAYERS_DATA = "config.csv"

Form, Window = uic.loadUiType("GUI.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def id_player(id):
    for i in range(1):
        rand_part = pad(random.randint(0, 99999), 5)
        unique_part = pad(random.randint(0, 9999), 4)
        id = rand_part + unique_part
        #print("Added new player with ID: " + id)
        return id

def pad(num, length):
    num_string = str(num)
    while len(num_string) < length:
        num_string = "0" + num_string
    return num_string

def save_to_file():
    global name1, email1, year_number1, id_number1, address1, city1, country1, state1, zip1, phone1
    with open("config.csv", "a", newline="") as file:
        columns = ['name', 'email', 'year_number', 'id_number', 'address', 'city', 'country', 'state', 'zip', 'phone']
        writer = csv.DictWriter(file, fieldnames=columns)

        while True:
            name1 = form.plainTextEdit.toPlainText()
            if name1 == "":
                break
            email1 = form.plainTextEdit_2.toPlainText()
            if email1 == "":
                break
            year_number1 = form.plainTextEdit_3.toPlainText()
            if year_number1 == "":
                break
            id_number1 = id_player(id)
            if id_number1 == "":
                break
            address1 = form.plainTextEdit_4.toPlainText()
            if address1 == "":
                break
            city1 = form.plainTextEdit_5.toPlainText()
            if city1 == "":
                break
            country1 = form.plainTextEdit_6.toPlainText()
            if country1 == "":
                break
            state1 = form.plainTextEdit_7.toPlainText()
            if state1 == "":
                break
            zip1 = form.plainTextEdit_8.toPlainText()
            if zip1 == "":
                break
            phone1 = form.plainTextEdit_9.toPlainText()
            if phone1 == "":
                break
            writer.writerow({'name': name1, 'email': email1, 'year_number': year_number1, 'id_number': id_number1,
                             'address': address1, 'city': city1, 'country': country1, 'state': state1, 'zip': zip1,
                             'phone': phone1})
            print("Added new player to the list of " + str(year_number1) + " year, with ID: " + id_number1)
            break


def play():
    booking()
    form.textBrowser.setText("Name: " + str(booking()) + " with ID")


def booking():
    book = {}
    with open(PLAYERS_DATA) as file:
        reader = csv.DictReader(file)

        for line in reader:
            player_name = str(line['name'])
            id_number = int(line['id_number'])
            book[player_name] = id_number
        player_name, id_number = random.choice(list(book.items()))
    return random.choice(list(book.items()))


def on_click():
    #print("Clicked!!!")
    save_to_file()


form.pushButton_2.clicked.connect(on_click)
form.pushButton.clicked.connect(play)


app.exec()