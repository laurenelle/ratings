from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session



ENGINE = None
Session = None
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, TIMESTAMP, DATETIME, ForeignKey

ENGINE = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=ENGINE,
						autocommit = False,
						autoflush = False)) 

Base = declarative_base()
Base.query = session.query_property()

class User(Base):
	__tablename__ = "users"

	user_id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)
	age = Column(Integer, nullable = True)
	gender = Column(String(6), nullable = True)
	occupation = Column(String(64), nullable = True)
	zipcode = Column(String(15), nullable = True)


	def __repr__(self):
		return"<User('%s', '%s', '%s', '%s', '%s')>" % (self.user_id, self.email, self.password, self.age, self.gender, self.occupation, self.zipcode)

def create_user(email, password, age, gender, occupation, zipcode)
	new_user = User(email = "email", password = "password", gender = "gender", occupation = "occupation", zipcode = "zipcode")


class Movie(Base):
	__tablename__ = "movies"

	movie_id = Column(Integer, primary_key = True)
	movie_title = Column(String(64))
	release_date = Column(DATETIME, nullable = True)
	imdb_url = Column(String)

	def __repr__(self):
		return"<Movie('%s', '%s', '%s', '%s')>" % (self.movie_id, self.movie_title, self.release_date, self.imdb_url)

class Rating(Base):
	__tablename__ = "ratings"

	rating_id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey("users.user_id"))
	movie_id = Column(Integer, ForeignKey("movies.movie_id"))
	rating = Column(Integer)
	timestamp = Column(DATETIME)

	#adds an attribute on ratings objects called user
	user = relationship("User", backref=backref("ratings", order_by=user_id))
	#adds an attribute on ratings objects called movie
	movie = relationship("Movie", backref=backref("ratings", order_by=movie_id))

	def __repr__(self):
		return"<Rating('%s', '%s', '%s', '%s', '%s')>" % (self.rating_id, self.user_id, self.movie_id, self.rating, self.timestamp)


### End class declarations

def connect():
	global ENGINE
	global Session



	return Session()

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
