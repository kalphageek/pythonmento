import user_email as ue
import user_password as up

class User:
    """
    This class keeping user's email address and password
    """

    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd
        self.check_validation()

    def check_validation(self):
        """
        checking email & password validate
        :return:
        """
        ue.email_validation_check(self.email)
        up.password_validation_check(self.pwd)

if __name__ == '__main__':
    user1 = User('isi.cho@gmail.com','3jkMf8Eed')
    print('==================================================')
    user2 = User('i#i.cho@gmail.com','3#kMex9-3')
    print('==================================================')