from flask import Flask
import datetime as dt

now = dt.datetime.now() # because it is (datetime Module, then datetime Class), to distinguish them from each other, we will rename the datetime Module as 'dt' or datetimeClass


app = Flask(__name__)
# print(f"The __name__ is now: {__name__}")
# Re: The __name__ is now: __main__

@app.route("/")
def hello_world():
    return f"<p>Hello, Flask! It is currently {now} </p>"

# remove below if unneeded:
if __name__ == "__main__":
    app.run(debug=True)   # can toggle this: True or False, depending on your needs
