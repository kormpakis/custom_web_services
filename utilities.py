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


def select_interest_by_user(user_id):
    """
    Using that function we provide information from the interest_array for a specific user.
    :param user_id: user id
    :return: interest_array information
    """
    db = MySQLdb.connect("localhost", "root", "", "wp")
    cursor = db.cursor()
    sql_query = """SELECT * FROM interest_array WHERE user_id={}""".format(user_id)
    cursor.execute(sql_query)
    results = cursor.fetchall()
    return results


def select_interest_by_tags(tags_id):
    """
    Return results based on the tags_id
    :param tags_id: tags_id
    :return: interests
    """
    db = MySQLdb.connect("localhost", "root", "", "wp")
    cursor = db.cursor()
    sql_query = """SELECT * FROM interest_array WHERE tags_id={}""".format(tags_id)
    cursor.execute(sql_query)
    results = cursor.fetchall()
    return results


def select_interest_by_user_tag(user_id, tags_id):
    """
    Return result based on both user and tags
    :param user_id: user
    :param tags_id: tag
    :return: interest
    """
    db = MySQLdb.connect("localhost", "root", "", "wp")
    cursor = db.cursor()
    sql_query = """SELECT * FROM interest_array WHERE tags_id={} AND user_id={}""".format(tags_id, user_id)
    cursor.execute(sql_query)
    results = cursor.fetchall()
    return results