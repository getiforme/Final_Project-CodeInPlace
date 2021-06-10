# Import the required libraries
import csv
import random
import datetime
import string

# Import the helpfull classes
from Year import Year
from Participant import Participant

# Simplify the call to the file
YEAR_DATA = "Years.csv"
PLAYERS_DATA = "Players.csv"

# Read data from the file Years.csv and return value year to the dictionary year_data = {}
def year_section():
    year_data = {}

    with open(YEAR_DATA) as file:
        reader = csv.DictReader(file)

        for line in reader:
            year_number = int(line['year_number'])


            year = Year(year_number)

            year_data[year_number] = year

    return year_data

# Read data from the file Players.csv and add the player to the player_names = [] list using class Year
def players_ingame(year_data):


    with open(PLAYERS_DATA) as file:
        reader = csv.DictReader(file)

        for line in reader:
            player_name = str(line['name'])
            player_email = str(line['email'])
            year_number = int(line['year_number'])
            id_number = int(line['id_number'])

            new_player = Participant(player_name, player_email, id_number)

            year_for_player = year_data[year_number]
            year_for_player.add_players(new_player)

# Generate two parts of the player id, the first part consists of 5 randomly generated digits and the second part consists of 4 randomly generated digits
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

# If new user want to play, we manually adding data to an existing Excel file
# If user doesn't want to play, he/she can press button "Enter" to skip it
def write_data():
    with open("Players.csv", "a", newline="") as file:
        columns = ['name', 'email', 'year_number', 'id_number', 'address', 'city', 'country', 'state', 'zip', 'phone']
        writer = csv.DictWriter(file, fieldnames=columns)

        while True:
            name1 = str(input("Enter Name: "))
            if name1 == "":
                break
            email1 = str(input("Enter Email: "))
            if email1 == "":
                break
            year_number1 = int(input("Enter Year(2021 or 2022): "))
            if year_number1 == "":
                break
            id_number1 = id_player(id)
            if id_number1 == "":
                break
            address1 = str(input("Enter Address: "))
            if address1 == "":
                break
            city1 = str(input("Enter City: "))
            if city1 == "":
                break
            country1 = str(input("Enter Country: "))
            if country1 == "":
                break
            state1 = str(input("Enter State: "))
            if state1 == "":
                break
            zip1 = str(input("Enter Zip: "))
            if zip1 == "":
                break
            phone1 = int(input("Enter Phone: "))
            if phone1 == "":
                break
            writer.writerow({'name': name1, 'email': email1, 'year_number': year_number1, 'id_number': id_number1, 'address': address1, 'city': city1, 'country': country1, 'state': state1, 'zip': zip1, 'phone': phone1})
            print("Added new player to the list of " + str(year_number1) + " year, with ID: " + id_number1)


def main():
    print("Welcome to the Lottery!\nJackpot is currently - $1000000\nCurrent date: " + datetime.datetime.today().strftime("%A %d %B %Y") + "\nIf you want to play, please follow registration steps below, or press 'Enter' to skip it and see results of game.")
    write_data()
    year_data = year_section()
    players_ingame(year_data)


    for year_number in year_data:
        year = year_data[year_number]
        print("=============================================================================================================")
        print("Year: " + str(year.year_number))
        print("Total nubmer of players: " + str(len(year.get_player_names())))
        #print("Players: " + str(year.get_player_names()))
        #print("The winner is " + random.choice(year.get_player_names()))
        print("The winner is " + str(booking()))
        print("Congratulations you won the Jackpot: $1000000")
        print("-------------------------------------------------------------------------------------------------------------")

# Randomly selects the winner from the file.
# Display username and user ID
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


if __name__ == '__main__':
    main()
