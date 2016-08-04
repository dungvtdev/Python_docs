from app.module.database.db_connection import get_db
from app.module.user import User

class User_Service:
    def __init__(self):
        self.db = get_db()
        self.db_cursor = self.db.cursor()

    def check_user(self,username):
        query = "SELECT * FROM users WHERE users.user_username = '" + username +"' LIMIT 1;"
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        if rows:
            #user = User(rows['user_firstName'],rows['user_lastName'],rows['user_username'],rows['user_email'],
             #           rows['user_password'],rows['user_phone'],rows['user_role'])
            for row in rows:
                user = User(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                print(user)
            return user
        print("not user")
        return None
    def add_user(self,user):
        query = """ INSERT INTO users (user_firstName, user_lastName, user_username, user_email
                , user_password, user_phone, user_role) VALUES ('"""+user.firstName+"""', '"""+user.lastName+"""',
                '"""+user.username+"""','"""+user.email+"""','"""+user.password+"""','"""+user.phone+"""',"""+user.role+"""
                );"""
        self.db_cursor.execute(query)
        self.db.commit()
        print("add successful")




