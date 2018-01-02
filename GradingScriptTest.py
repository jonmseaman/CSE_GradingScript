import unittest
import GradingScript

class MyTestCase(unittest.TestCase):
    def test_get_submissions_path_blank_input(self):
        print("Leave the input blank for this test.")
        path = GradingScript.get_submissions_path()
        self.assertEqual("./submissions.zip", path)


if __name__ == '__main__':
    unittest.main()
