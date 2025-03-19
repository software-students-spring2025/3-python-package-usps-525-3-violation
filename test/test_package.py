import pytest
from packagepackage import package
import random


class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #

    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_coin(self):
        """
        Verify coin() function and make sure it returns a non-empty string.
        Note that for example purposes, we have not used the example_fixture in this test functino.
        """
        # since coin returns a string, run it a bunch of times and verify the output
        for i in range(100):
            actual = package.coin()
            assert isinstance(
                actual, str
            ), f"Expected coin() to return a string. Instead, it returned {actual}"
            assert (
                len(actual) > 0
            ), f"Expected coin() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_content(self):
        """
        Make sure that the text returned by the coin() function is actually from the correct poem.
        """
        # run a bunch of times and verify the output
        for i in range(100):
            actual = package.coin()
            assert (
                actual in ["heads!", "tails!"]
            ), f"Expected the text returned by coin() to either 'heads!' or 'tails!'.  Instead, it returned '{actual}'."

    def test_play_math_predetermined(self, monkeypatch):
        """
        Makes sure that the play_math function works with a predetermined set of questions and answers, while correctly answering all questions correctly
        """
        #testing easy inputs
        fixed_numbers = iter([2, 1, 1, 4, 3, 2, 6, 5, 3, 8, 7, 4])
        monkeypatch.setattr(random, 'randint', lambda x, y: next(fixed_numbers))

        simulated_inputs = iter(["3", "1", "30", "8"])
        monkeypatch.setattr('builtins.input', lambda answer: next(simulated_inputs))

        num_correct = package.play_math("easy", 4)
        assert num_correct == 4

    def gen_questions(self, max):
        """
        used to generate a set of 100 questions for the play_math question
        """
        fixed_numbers = []
        for i in range(100):
            num1 = random.randint(1, max)
            num2 = random.randint(1, max)
            if num1 < num2:
                temp = num1
                num1 = num2
                num2 = temp
            op = random.randint(1, 4)
            fixed_numbers.extend([num1, num2, op])
        return fixed_numbers
        
    def gen_answers(self, fixed_numbers):
        """
        used to generate a set of 100 answers for the play_math question, given a list generated by gen_questions
        """
        simulated_inputs = []
        for i in range(100):
            ans = package.math_ans(fixed_numbers[3*i+2], fixed_numbers[3*i], fixed_numbers[3*i+1])
            simulated_inputs.append(ans)
        return simulated_inputs
    
    def test_play_math_generate(self, monkeypatch):
        """
        Makes sure that the play_math function works with a randomly generated set of questions and answers, while correctly answering all questions correctly
        """
        #testing on easy mode
        fixed_numbers = self.gen_questions(10)
        simulated_inputs = self.gen_answers(fixed_numbers)
        fixed_numbers = iter(fixed_numbers)
        simulated_inputs = iter(simulated_inputs)
        monkeypatch.setattr(random, 'randint', lambda x, y: next(fixed_numbers))
        monkeypatch.setattr('builtins.input', lambda answer: next(simulated_inputs))
        num_correct = package.play_math("easy", 100)

        assert num_correct == 100
        monkeypatch.undo()

        #testing on medium mode
        fixed_numbers = self.gen_questions(20)
        simulated_inputs = self.gen_answers(fixed_numbers)
        fixed_numbers = iter(fixed_numbers)
        simulated_inputs = iter(simulated_inputs)
        monkeypatch.setattr(random, 'randint', lambda x, y: next(fixed_numbers))
        monkeypatch.setattr('builtins.input', lambda answer: next(simulated_inputs))
        num_correct = package.play_math("medium", 100)

        assert num_correct == 100
        monkeypatch.undo()

        #testing on hard mode
        fixed_numbers = self.gen_questions(50)
        simulated_inputs = self.gen_answers(fixed_numbers)
        fixed_numbers = iter(fixed_numbers)
        simulated_inputs = iter(simulated_inputs)
        monkeypatch.setattr(random, 'randint', lambda x, y: next(fixed_numbers))
        monkeypatch.setattr('builtins.input', lambda answer: next(simulated_inputs))
        num_correct = package.play_math("hard", 100)

        assert num_correct == 100

    def test_play_geo(self):
        pass


    def test_play_vocab(self):
        pass


    def test_play_science(self):
        # WIP
        # # test on easy mode with a random number of questions
        # num_questions = random.randint(1, 10)
        # num_correct = package.play_math("easy", num_questions)
        # expected = num_questions
        # actual = num_correct
        # assert expected == actual
        
        # # test on hard mode with a random number of questions
        # num_questions = random.randint(1, 10)
        # num_correct = package.play_math("hard", num_questions)
        # expected = num_questions
        # actual = num_correct
        # assert expected == actual
        
        # # test on mix mode with a random number of questions
        # num_questions = random.randint(1, 10)
        # num_correct = package.play_math("mix", num_questions)
        # expected = num_questions
        # actual = num_correct
        # assert expected == actual
        pass