from flask import *
import sqlite3


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("task4_1.html")


@app.route("/scores", methods=["POST"])
def scores():
    data = request.form #get data
    option = data["option"]

    #sql
    conn = sqlite3.connect("Task4.db")
    sql = """select competitor.name, scores.score
            from competitor, scores
            where competitor.id = scores.id
            and scores.round = ?
            order by scores.score desc"""
    result = conn.execute(sql, (option,)).fetchall()
    conn.close()
    
    return render_template("task4_2.html", result = result, option = option)
        

@app.route("/mean", methods=["POST"])
def mean():
    #sql
    conn = sqlite3.connect("Task4.db")
    sql = """select competitor.name, round(avg(scores.score), 2)
            from competitor, scores
            where competitor.id = scores.id
            group by competitor.id, competitor.name
            order by competitor.name asc"""

    result = conn.execute(sql).fetchall()
    conn.close()

    return render_template("task4_3.html", result = result)
    
@app.route("/qualify", methods=["POST"])
def qualify():
    #sql
    conn = sqlite3.connect("Task4.db")
    sql = """select competitor.name, sum(scores.score),
            total(scores.score) > 250
            from competitor, scores
            where competitor.id = scores.id
            group by competitor.id, competitor.name
            order by sum(scores.score) desc"""
    result = conn.execute(sql).fetchall()
    conn.close()

    return render_template("task4_4.html", result = result)


    
if __name__ == "__main__":
    app.run()
