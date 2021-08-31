import unittest


class TestGetQuestionsFromUser(unittest.TestCase):
    def test_get_questions_from_user(self):
        """
        Tests logic for function gets_questions_from_user
        """

        flag = True
        question_list = []
        test_questions = ['Question 1', 'Question 2', 'Question 3', 'QUIT']
        i = 0

        while flag:

            users_question = test_questions[i]

            if users_question == 'QUIT':
                print('\n')
                flag = False
            else:
                question_list.append(users_question)
                i += 1

        return question_list


if __name__ == '__main__':
    unittest.main()
