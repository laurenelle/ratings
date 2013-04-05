from flask import Flask, render_template, redirect, request, session, escape, url_for, g, flash
import model
app = Flask(__name__)

@app.route("/")
def index():
	user_list = model.session.query(model.User).limit(10).all()
	return render_template("beginning.html", users=user_list)


@app.route("/authenticate", methods=["POST"])
def authenticate():
	#insert sqlalchemy line
	return render_template("authenticate.html")
	# instantiate the user class to create an object
	U = User()
	# assign user columns to jinja variables
	U.user_id = request.form['user_id']
	U.password = request.form['password']
	U.age = request.form['age']
	U.gender = request.form['gender']
	U.occupation = request.form['occupation']
	U.zipcode = request.form['zipcode']
	session.add(U)
	session.commit()
	session.refresh(U)


# @app.route("/register", methods=["POST"])
# def register():
#     email = request.form['email']
#     password = request.form['password']
#     existing = db_session.query(User).filter_by(email=email).first()
#     if existing:
#         flash("Email already in use", "error")
#         return redirect(url_for("index"))

#     u = User(email=email, password=password)
#     db_session.add(u)
#     db_session.commit()
#     db_session.refresh(u)
#     session['user_id'] = u.id 
#     return redirect(url_for("display_search"))

if __name__ == "__main__":
    app.run(debug = True)
#    