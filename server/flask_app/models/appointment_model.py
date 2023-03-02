from flask_app.config.mysqlconnection import connectToMySQL


db = 'calendar'
class Appointment:
    def __init__(self, data):
        self.date = data['date']
        self.client_name = data['client_name']
        self.admin_name = data['admin_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def createAppointment(cls, data):
        query="""
        INSERT INTO appointment(date, client_name, admin_name)
        VALUE(%(date)s, %(client_name)s, %(admin_name)s)
        """
        return connectToMySQL(db).query_db(query, data)