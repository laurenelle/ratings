from datetime import date, datetime
import time


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
    print timestamp
    #new_item = model.Rating(user_id = user_id, movie_id = movie_id, rating = rating, timestamp = timestamp)

            # release_date = datetime.strptime(item_list[2], '%d-%b-%Y')