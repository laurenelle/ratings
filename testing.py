import sys
import model

# def load_users(session):


open_file=open("seed_data/u.user")

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
    password = "null"

    new_user = User(user_id = user_id, email = email, password = password, age = age, zipcode = zipcode)

    session.add(new_user) 
    session.commit()

if __name__ == "__main__":
    s = model.connect()
    main(s)
