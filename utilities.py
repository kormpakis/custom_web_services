import MySQLdb

db = MySQLdb.connect("localhost", "root", "", "wp")


def select_interest_array(db):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM interest_array""")
    results = cursor.fetchall()
    return results


print(select_interest_array(db))
