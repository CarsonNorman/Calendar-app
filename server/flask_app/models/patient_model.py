from flask_app.config.mysqlconnection import connectToMySQL


db = 'calendar'
class Patient:
    def __init__(self, data):
        self.username = data.username
        self.email = user.email
        self.password = data.password
        self.create_time = data.create_time
    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO patient (first_name, last_name, dob, email, password)
        VALUES(%(first_name)s, %(last_name)s, %(dob)s, %(email)s, %(password)s)
        """

        result = connectToMySQL(db).query_db(query, data)
        
        return result
    @classmethod
    def readAll(cls):
        query ="""
        SELECT * FROM patient
        """

        result = connectToMySQL(db).query_db(query)

        return result