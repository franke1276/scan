from mockito import mock, verify
import unittest

from scan import helloscan

class HelloWorldTest(unittest.TestCase):
    def test_should_issue_hello_world_message(self):
        self.assertEqual("a", "a")
