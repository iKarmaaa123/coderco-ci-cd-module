import unitest

from hello import say_hello

class TestHello(unitest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, World!")