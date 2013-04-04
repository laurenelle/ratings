import model
import csv
from datetime import date, datetime
import time


def load_users(session):
    #open the file
    open_file=open("seed_data/u.user")
    # read_file = open_file.read()
    # line = read_file.split('\n')
    lines = open_file.readlines()

    for item in lines:
        item_list = item.split('|')
    #create a list out of each line
    # enumerate over each row as a list and assign to appropriate variables by index
        user_id= item_list[0]
        age = item_list[1]
        gender = item_list[2]
        occupation = item_list[3]
        zipcode = item_list[4]
        email = "null"
        password = "null" # ?

        new_user = model.User(user_id = user_id, email = email, password = password, gender = gender, occupation = occupation, age = age, zipcode = zipcode)

        session.add(new_user) 
    session.commit()


def load_movies(session):
    #open the file
    open_file=open("seed_data/u.item")
    # read_file = open_file.read()
    # line = read_file.split('\n')
    lines = open_file.readlines()

    for item in lines:
        item_list = item.split('|')
    #create a list out of each line
    # enumerate over each row as a list and assign to appropriate variables by index
        movie_id= item_list[0]
        movie_title = item_list[1]
        movie_title = movie_title.decode("latin-1")
        release_date = item_list[2]
        if release_date == '':
            release_date = None
        else:    
            release_date = datetime.strptime(item_list[2], '%d-%b-%Y')
        empty = item_list[3]
        imdb_url = item_list[4]

        new_item = model.Movie(movie_id = movie_id, movie_title = movie_title, release_date = release_date, imdb_url = imdb_url)

        session.add(new_item) 
    session.commit()

def load_ratings(session):
    # use u.data
    open_file=open("seed_data/u.data")
    lines = open_file.readlines()

    for movie in lines:
        movie_list = movie.split('\t')
        user_id= movie_list[0]
        movie_id = movie_list[1]
        rating = movie_list[2]
        timestamp0 = movie_list[3].strip('\n')
        timestamp1 = time.gmtime(float(timestamp0))
        timestamp = datetime.fromtimestamp(time.mktime(timestamp1))

        new_item = model.Rating(user_id = user_id, movie_id = movie_id, rating = rating, timestamp = timestamp)

        session.add(new_item) 
    session.commit()



# user id | item id | rating | timestamp



def main(session):
    # You'll call each of the load_* functions with the session as an argument
    # load_users(session)
    load_movies(session)
    load_ratings(session)
    load_users(session)

if __name__ == "__main__":
    s = model.connect()
    main(s)

