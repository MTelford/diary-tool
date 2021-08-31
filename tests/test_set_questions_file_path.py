import unittest
import os
import pathlib



from diary_tool import set_questions_file_path

class TestSetQuestionsFilePath(unittest.TestCase):
    def test_get_questions_from_user(self):
        """
        Tests that function sets file path for questions
        correctly
        """

        result = set_questions_file_path()
        current_test_directory = str(pathlib.Path(__file__).parent.resolve())
        actual_function_directory = current_test_directory.replace('tests', 'questions')
        
        self.assertEqual(result, actual_function_directory)

        
    
if __name__ == '__main__':
    unittest.main()
