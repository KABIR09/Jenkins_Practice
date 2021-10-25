import unittest

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.a=10
        self.b=20
    
    def test_sum_func(self):
        print("Test 1 called...")
        #Act
        result = sum(self.a ,  self.b)
        #Assert
        self.assertEqual(result,self.a + self.b)


if __name__ == "__main__":
    unittest.main()