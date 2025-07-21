import unittest
from hash_password import hash_password
from verify_password import verify_password

class Test_Password_Hashing(unittest.TestCase):
    def test_hash_and_verify_password(self):
        password="bhargav@123"
        hashed=hash_password(password)
        self.assertTrue(verify_password(hashed,password))
        self.assertFalse(verify_password(hashed,"wrong_password"))
if __name__=="__main__":
    unittest.main()