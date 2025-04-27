from hello import say_hello

class TestHello(unitest.TestCase):
    def say_hello(self):
        self.assertEqual(say_hello(), "Hello, World!")