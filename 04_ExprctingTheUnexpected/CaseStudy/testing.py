import AuthenticationAndAuthorization as auth

auth.authenticator.add_user('joe','joepassword')
auth.authorizor.add_permission('test program')
auth.authorizor.add_permission('chancge program')
auth.authorizor.permit_user('test program','joe')

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            'login' : self.login,
            'test' : self.test,
            'change' : self.change,
            'quit' : self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("Username: ")
            password = input("Password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print('Sorry, That username does not exit.')
            except auth.InvalidPassword:
                print('Sorry, Incorrect Pasword')
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print('{} is not logged in'.format(e.username))
            return False
        except auth.NotPermittedError as e:
            print('{} cannot {}'.format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted('test program'):
            print('Testing program now...')
    
    def change(self):
        if self.is_permitted('change program'):
            print('Changing Program now...')

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print("""
                Please enter a command:
                \tlogin\tLogin\ttest\tTest The Program
                \tchange\tChange the program\tquit\tQuit""")

                answer = input('Enter a Command: ').lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print('{} is not a valid option'.format(answer))
                else:
                    func()
        finally:
            print('Thank you for testing the auth module')

Editor().menu()