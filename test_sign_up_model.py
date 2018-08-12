import unittest
import re
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
            self.assertIn(rider.get(i[0]) == self.firstName, self.uberUsers)
    
            
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
            self.authenticate_user.register()
            
        def test_check_email_contains(self):
            self.assertIn("@", self.email)
            self.assertIn(".", self.email)
            self.assertNotIn("@.", self.email)
            self.assertNotIn(".@", self.email)
            self.assertGreater(len(self.email), 6)
        
        def test_verify(self):
            self.assertTrue(self.firstName)
            self.assertTrue(self.lastName)
            self.assertTrue(self.phoneNumber)
            self.assertTrue(self.email)
            self.assertTrue(self.password)

            for i, rider in enumerate(self.uberUsers):
                self.assertIsInstance(rider.get(i[3]) == self.email and rider.get(
                    i[2]) == self.phoneNumber, self.uberUsers)
        
        def test_check_password(self):
            self.assertNotEqual(self.password, None)
            self.assertGreater(len(self.password), 6)
            
        def test_check_phone_number(self):
            self.assertTrue(self.phoneNumber.isdigit())
            self.assertNotEqual(self.password, None)
            self.assertGreaterEqual(len(self.password), 10)
        
        def test_name(self):
            regex = re.compile(r'[@_!#$%^&*()123456789<>?/\|}{~:]')
            self.assertNotRegex(self.firstName, regex)
            self.assertNotEqual(self.firstName, None)
            


if __name__ == "__main__":
    unittest.main()
