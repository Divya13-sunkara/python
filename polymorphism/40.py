class GoogleLogin:
    def login(self):
        print("Logged in using Google")

class FacebookLogin:
    def login(self):
        print("Logged in using Facebook")

class EmailLogin:
    def login(self):
        print("Logged in using Email")

def authenticate_user(user):
    user.login()

authenticate_user(GoogleLogin())
authenticate_user(FacebookLogin())
authenticate_user(EmailLogin())