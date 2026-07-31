import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect("2022_LIBRARY.db")

    sql = """select Member.FamilyName, Member.GivenName, Book.Title
            from Book, Loan, Member
            where Member.MemberNumber = Loan.MemberNumber
            and Loan.BookID = Book.BookID
            and Loan.Returned = 'FALSE'"""

    results = conn.execute(sql).fetchall()
    print(results)

    return render_template("task4_4.html", results = results)

if __name__ == "__main__":
    app.run()
