import unittest
import os
from diary_tool_main.diary_tool import get_datetime_as_string


class TestAskAndAwaitAnswer(unittest.TestCase):
    def test_ask_and_await_answer(self):
        """
        Tests logic for function ask_and_await_answer
        """

        datetime = get_datetime_as_string()

        # opens file as file object using append parameter
        current_file_path = os.path.realpath(__file__)
        test_file_path = current_file_path.replace(
            'test_ask_and_await_answer.py', 'testfile_for_ask_and_await_answer')

        question_list = ['Question 1', 'Question 2', ]

        for i in range(0, len(question_list)):

            answer = (question_list[i] + '\n\n' +
                      'answer ' + str(i+1) + '\n\n')

            # outputs answer to questions in correct format
            # to log file
            with open(test_file_path, 'a') as file:

                file.write(answer)

        expected_string = ("Question 1\n\nanswer 1"
                           "\n\nQuestion 2\n\nanswer 2\n\n")

        with open(test_file_path) as file:
            self.assertEqual(file.read(), expected_string,
                             msg='pattern matches')

        # clears the test file after writing and assertion
        open(test_file_path, 'w').close()


if __name__ == '__main__':
    unittest.main()
