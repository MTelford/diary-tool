import unittest

from diary_tool import get_file_path

class TestGetFilePath(unittest.TestCase):
    def test_getting_filepath(self):
        """
        Test that the function returns a valid file path
        """

        result = get_file_path()
        self.assertEqual(result, "/home/michael-engineer/projects/diary_tool/diary_log", 'Should be /home/michael-engineer/projects/diary_tool/diary_log')

if __name__ == '__main__':
    unittest.main()