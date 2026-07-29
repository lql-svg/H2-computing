#Task 4.3
import sqlite3
from flask import *

app = Flask(__name__)

@app.route('/')
def home():

    conn = sqlite3.connect("school.db")

    data = conn.execute("select People.ScreenName from People").fetchall()

    #Get identity
    file = open("people.txt", 'r')

    result = []
    count = 0 #To iterate for screenName

    for line in file:
        line = line.strip().split(",")

        name = line[0]
        identity = line[2]
        
        screenName = data[count][0] #Get screenName from data
        
        result.append([name, screenName, identity])

        count += 1

    file.close()
    #print(result)

    return render_template("task4_3.html", data = result)

if __name__ == "__main__":
    app.run()
