import unittest 
from io import StringIO
import sys
from hello import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        captured_output = StringIO() #Create StringIO object 
        sys.stdout = captured_output #Redirect stdout
        say_hello()                  #Call the function say_hello
        sys.stdout = sys.__stdout__  #Reset redirect
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()