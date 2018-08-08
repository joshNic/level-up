import unittest
from sign_up_model import SignUp
from sign_up_model import Authentication

class TestSignUp(unittest.TestCase):
    """Tests for class SignUp"""

    def setUp(self):
        """Create a SignUp object and a set of variables to use on all
        test methods
        """
        self.firstName = "Joshua"
        self.lastName = "Mugisha"
        self.phoneNumber = "0700542063"
        self.email = "256jomu@gmail.com"
        self.password = "joshua1234"
        self.uberUsers = []
        self.register_user = SignUp(self.firstName, self.lastName,
                                    self.phoneNumber, self.email, self.password) 
    def test_register(self):
        self.register_user.register()
        for i, rider in enumerate(self.uberUsers):
            self.assertEqual(rider.get(i[0]), "Joshua")
        # user = [rider for rider in self.uberUsers if rider.get("lastName") == self.lastName]
        # self.assertFalse(user)
    # def tearDown(self):
    #     self.register_user
            
class TestAuthentication(unittest.TestCase):
        def setUp(self):
            """Create a SignUp object and a set of variables to use on all
            test methods
            """
            self.firstName = "Joshua"
            self.lastName = "Mugisha"
            self.phoneNumber = "0700542063"
            self.email = "256jomu@gmail.com"
            self.password = "joshua1234"
            self.uberUsers = []
            self.authenticate_user = Authentication(self.firstName, self.lastName,
                                        self.phoneNumber, self.email, self.password)
            
        def test_check_email_contains(self):
            pass
        
        def test_verify(self):
            self.assertTrue(self.firstName)
            self.assertTrue(self.lastName)
            self.assertTrue(self.phoneNumber)
            self.assertTrue(self.email)
            self.assertTrue(self.password)
        
        def test_check_password(self):
            pass
            
        def test_check_phone_number(self):
            pass
        
        def test_name(self):
            pass


if __name__ == "__main__":
    unittest.main()
