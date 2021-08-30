from typing import List
import unittest


from diary_tool import get_questions_from_user

class TestGetQuestionsFromUser(unittest.TestCase):
    def test_get_questions_from_user(self):
        """
        Tests function gets questions from user
        """

        result = get_questions_from_user('Test')
        self.assertIsInstance(result, List)

if __name__ == '__main__':
    unittest.main()
