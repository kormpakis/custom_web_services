import MySQLdb


def select_interest_array():
    """
    This function return the interest_array contents
    :return: results
    """
    db = MySQLdb.connect("localhost", "root", "", "wp")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM interest_array""")
    results = cursor.fetchall()
    return results
