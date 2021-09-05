import unittest
import pathlib
from diary_tool_main.diary_tool import set_questions_file_path


class TestSetQuestionsFilePath(unittest.TestCase):
    def test_set_questions_file_path(self):
        """
        Tests that function sets file path for questions
        correctly
        """
        # actual path to function
        main_path = set_questions_file_path()

        current_directory = str(pathlib.Path(__file__).parent.resolve())

        # our fabricated path to test against actual path in main
        func_path = current_directory.replace(
            'tests', 'diary_tool_main/questions')

        self.assertEqual(main_path, func_path)


if __name__ == '__main__':
    unittest.main()
