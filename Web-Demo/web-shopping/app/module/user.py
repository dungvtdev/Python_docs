class User:

    def __init__(self, firstName, lastName, username, email, password, phone, role):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.role = role

    def check_password(self,password):
        if password == self.password :
            return True
        return False

