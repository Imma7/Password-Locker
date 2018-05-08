import unittest

from user import User

class TestUser(unittest.TestCase):
    '''
    TestUser is a subclass of the parent class
    unittest.TestCase enables to create test cases
    '''

    def setUp(self): #SetUp method defines instructions to be executed before each test method
        self.new_account = User("GitHub", "Imma", "1234")

    def test_init(self):
        self.assertEqual(self.new_account.account_name, "GitHub")
        self.assertEqual(self.new_account.username, "Imma")
        self.assertEqual(self.new_account.password, "1234")

    
# Second class for Credentials
from user import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.user_credential = Credentials("GitHub", "Imma", "1234") 
    
    def test_init(self):
        self.assertEqual(self.user_credential.account_name, "GitHub")
        self.assertEqual(self.user_credential.username, "Imma")
        self.assertEqual(self.user_credential.password, "1234")

if __name__ == '__main__':
    unittest.main()


    



    






