import mysql.connector

global f
f = 0

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movie_booking"
)
cursor = db.cursor()

def t_movie():
    global f
    f += 1

    print("Which movie do you want to watch?")
    cursor.execute("SELECT movie_id, title FROM Movies")
    movies = cursor.fetchall()
    for movie in movies:
        print(f"{movie[0]}, {movie[1]}")
    print("1,bigil")
    print("2,soorarai  pottru")
    print("3,oh my kadavule")
    print("4, Back")

    movie_choice = int(input("Choose your movie: "))
    if movie_choice == 4:
        center()
        theater()
        return
    if f == 1:
        theater()

def theater():
    print("Which class do you want to watch movie: ")
    print("1, firstclass")
    print("2, Secondclass")
    print("3, thirdclass")

    screen_choice = int(input("Choose your class: "))
    ticket_count = int(input("Number of tickets do you want?: "))

    timing(screen_choice)

def timing(screen_choice):
    time1 = {
        "1": "10:00-1:00",
        "2": "1:10-4:10",
        "3": "4:20-7:20",
        "4": "7:30-10:30"
    }
    time2 = {
        "1": "10:15-1:15",
        "2": "1:25-4:25",
        "3": "4:35-7:35",
        "4": "7:45-10:45"
    }
    time3 = {
        "1": "10:30-1:30",
        "2": "1:40-4:40",
        "3": "4:50-7:50",
        "4": "8:00-10:45"
    }

    times = [time1, time2, time3]

    print("Choose your time:")
    for k, v in times[screen_choice - 1].items():
        print(f"{k}: {v}")
    time_choice = input("Select your time: ")
    selected_time = times[screen_choice - 1][time_choice]

    print(f"Successful! Enjoy movie at {selected_time}")

def movie(theater_choice):
    if theater_choice in [1, 2, 3]:
        t_movie()
    elif theater_choice == 4:
        city()
    else:
        print("Wrong choice")

def center():
    print("Which theater do you wish to see movie?")
    print("1, Inox")
    print("2, Icon")
    print("3, PVP")
    print("4, Back")

    theater_choice =int(input("Choose your option: "))
    movie(theater_choice)

def city():
    print("Hi, welcome to movie ticket booking!")
    print("Where do you want to watch movie?")
    print("1, thabaram")
    print("2, tnagar")
    print("3, eggmore")

    city_choice = int(input("Choose your option: "))

    if city_choice in [1,2,3]:
        center()
    else:
        print("Wrong choice")

# Start the program
city()