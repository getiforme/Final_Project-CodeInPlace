import pickle
import csv
import random
import datetime
import string

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

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
    data_to_save = {'name': name1, 'email': email1, 'year_number': year_number1, 'id_number': id_number1, 'address': address1, 'city': city1, 'country': country1, 'state': state1, 'zip': zip1, 'phone': phone1}
    file1 = open("config.csv", "ab")
    pickle.dump(data_to_save, file1)
    file1.close()


def read_from_file():
    global name1, email1, year_number1, id_number1, address1, city1, country1, state1, zip1, phone1
    file1 = open("config.csv", "rb")
    data_to_load = pickle.load(file1)
    file1.close()
    winner = "Name: " + data_to_load['name'] + " with ID: " + data_to_load['id_number']
    print(winner)
    form.textBrowser.setText(winner)



def on_click():
    global name1, email1, year_number1, id_number1, address1, city1, country1, state1, zip1, phone1
    name1 = form.plainTextEdit.toPlainText()
    email1 = form.plainTextEdit_2.toPlainText()
    year_number1 = form.plainTextEdit_3.toPlainText()
    id_number1 = id_player(id)
    address1 = form.plainTextEdit_4.toPlainText()
    city1 = form.plainTextEdit_5.toPlainText()
    country1 = form.plainTextEdit_6.toPlainText()
    state1 = form.plainTextEdit_7.toPlainText()
    zip1 = form.plainTextEdit_8.toPlainText()
    phone1 = form.plainTextEdit_9.toPlainText()
    #print(form.plainTextEdit.toPlainText())
    print("Clicked!!!")
    save_to_file()

name1 = form.plainTextEdit.toPlainText()
email1 = form.plainTextEdit_2.toPlainText()
year_number1 = form.plainTextEdit_3.toPlainText()
id_number1 = id_player(id)
address1 = form.plainTextEdit_4.toPlainText()
city1 = form.plainTextEdit_5.toPlainText()
country1 = form.plainTextEdit_6.toPlainText()
state1 = form.plainTextEdit_7.toPlainText()
zip1 = form.plainTextEdit_8.toPlainText()
phone1 = form.plainTextEdit_9.toPlainText()

form.pushButton_2.clicked.connect(on_click)
form.pushButton.clicked.connect(read_from_file)


app.exec()
