import unittest
import os


class TestFormatStoredQuestionsForUser(unittest.TestCase):
    def test_format_stored_questions_for_user(self):
        """
        Tests function that formats text
        for user from questions file
        """

        # initialize questions list with characteristics created
        # upon read, when input() was used to write to the
        # data to file

        input_questions = ['', '', 'Question 1', '', 'Question 2', '', '']
        expected_output = ['Question 1', 'Question 2']

        # setup path to testfile (stores test input questions for importing)
        current_file_path = os.path.realpath(__file__)
        testfile_path = current_file_path.replace(
            'test_format_stored_questions_for_user.py',
            'tesfile_for_func_format_stored_questions_for_user')

        # write input to testfile
        with open(testfile_path, 'w') as file:
            for i in input_questions:
                file.write(i + '\n\n')

        # initialize questions file object for reading
        questions_testfile = open(testfile_path, 'r')

        # adds contents of questions file lines to list of questions
        text_lines = questions_testfile.read().split('\n')

        # filters unwanted empty elements from list
        output_question_list = list(filter(None, text_lines))
        questions_testfile.close()

        # asserts newly created list with function logic matches
        # expected output
        self.assertEqual(output_question_list, expected_output)


if __name__ == '__main__':
    unittest.main()
