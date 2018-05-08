import unittest

from user import User

class TestUser(unittest.TestCase):
    '''
    TestUser is a subclass of the parent class
    unittest.TestCase enables to create test cases
    '''

    def setUp(self): #SetUp method defines instructions to be executed before each test method
        self.new_account = User("GitHub", "Imma", "1234")

    # def test_init(self):
    #     self.assertEqual(self.new_account.account_name, "GitHub")
    #     self.assertEqual(self.new_account.username, "Imma")
    #     self.assertEqual(self.new_account.password, "1234")

    



    






