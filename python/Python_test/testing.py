import unittest
import BankAccount

my_account=ex1(160)

class Text_ext(unittest.TestCase):
    my_account = ex1(160)

    def testdeposit(self):
        self.assertTrue(self.my_account.deposit(90))

    def withdrawtest(self):
        self.assertTrue(self.my_account.withdraw(40))
        self.assertFalse(self.my_account.withdraw(25))

if __name__=="__main__":
    unittest.main()

