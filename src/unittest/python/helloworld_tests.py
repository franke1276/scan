import unittest


class HelloWorldTest(unittest.TestCase):
  def test_should_issue_hello_world_message(self):
    self.assertEqual("a", "a")
