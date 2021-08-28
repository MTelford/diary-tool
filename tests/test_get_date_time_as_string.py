import unittest
import datetime


from diary_tool import get_datetime_as_string

class TestGetFilePath(unittest.TestCase):
    def test_get_datetime_as_string(self):
        """
        Test function returns current date time as string
        """

        result = get_datetime_as_string()
        time = datetime.datetime.now()
        time = time.strftime("%c")
        self.assertEqual(result, time) 

if __name__ == '__main__':
    unittest.main()