import pytest
from packagepackage import package
import re
from packagepackage.wordbank import wordbank


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
        Verify get() function and make sure it returns a non-empty string.
        Note that for example purposes, we have not used the example_fixture in this test functino.
        """
        # since get returns a random string, run it a bunch of times and verify the output
        for i in range(100):
            actual = package.coin()
            assert isinstance(
                actual, str
            ), f"Expected get() to return a string. Instead, it returned {actual}"
            assert (
                len(actual) > 0
            ), f"Expected get() not to be empty. Instead, it returned a string with {len(actual)} characters"

    def test_content(self):
        """
        Make sure that the text returned by the get() function is actually from the correct poem.
        """
        # since get returns a random string, run it a bunch of times and verify the output
        for i in range(100):
            actual = package.coin()
            assert (
                actual in ["heads!", "tails!"]
            ), f"Expected the text returned by coin() to either 'heads!' or 'tails!'.  Instead, it returned '{actual}'."

    def test_play_math(self):
        pass


    def test_play_geo(self):
        pass

    def test_play_vocab_invalid_args(self):
        '''
        Test invalid inputs
        '''
        # test invalid level
        # test non strings
        with pytest.raises(ValueError, match="Invalid difficulty"):
            package.play_vocab(1405, "synonyms", 5)

        # test invalid strings
        with pytest.raises(ValueError, match="Invalid difficulty"):
            package.play_vocab("asoadon", "synonyms", 5)

        # test invalid gamemode
        # test non strings
        with pytest.raises(ValueError, match="Invalid gamemode"):
            package.play_vocab("easy", 67.2, 5)

        # test invalid strings
        with pytest.raises(ValueError, match="Invalid gamemode"):
            package.play_vocab("easy", "firefighter", 5)

        # test invalid numbers
        
        # test out of range numbers
        with pytest.raises(ValueError, match="Invalid number"):
            package.play_vocab("easy", "synonyms", 25)

        with pytest.raises(ValueError, match="Invalid number"):
            package.play_vocab("easy", "synonyms", 0)
        
        with pytest.raises(ValueError, match="Invalid number"):
            package.play_vocab("easy", "synonyms", -1)

        # test non integers
        with pytest.raises(ValueError, match="Invalid number"):
            package.play_vocab("easy", "synonyms", 4.5)

        # test non numbers
        with pytest.raises(ValueError, match="Invalid number"):
            package.play_vocab("easy", "synonyms", "eleven")



    def test_play_vocab_levels(self, monkeypatch, capsys):
        '''
        Test that question words and answer options come from wordbank
        Test that words come from correct level
        '''
        difficulty_levels = ["easy", "medium", "hard"]
        for level in difficulty_levels:
            valid_q_words = {word[0] for word in wordbank[level]}
            valid_options = {word[0] for word in wordbank[level]} | {word[1] for word in wordbank[level]} | {word[2] for word in wordbank[level]}

            inputs = iter(["A"] * 10)
            monkeypatch.setattr("builtins.input", lambda _: next(inputs))
            
            package.play_vocab(level, "synonyms", 10)  # start vocab quiz with sample parameters
            captured = capsys.readouterr()
            output_words = re.findall(r"Which word is a synonym for (\w+)\?", captured.out)

            # check question words
            for other_level in difficulty_levels: # make sure level words are correct
                if other_level != level:
                    unexpected_words = {word[0] for word in wordbank[other_level]} | {word[1] for word in wordbank[other_level]} | {word[2] for word in wordbank[other_level]}
                    for word in output_words:
                        assert word not in unexpected_words, f"Expected only {level} words, {other_level} word '{word}' appeared in {level} level"

            for word in output_words:  # outside wordbank
                assert word in valid_q_words, f"Received word '{word}' outside {level} wordbank"

            # check answer options
            answer_options = re.findall(r"[A-Z]: (\w+)", captured.out)

            for other_level in difficulty_levels: # make sure level words are correct
                if other_level != level:
                    unexpected_options = {word[0] for word in wordbank[other_level]} | {word[1] for word in wordbank[other_level]} | {word[2] for word in wordbank[other_level]}
                    for option in answer_options:
                        assert option not in unexpected_options, f"Expected only {level} options, {other_level} option '{option}' appeared in {level} level"
            
            for option in answer_options: # outside wordbank
                assert option in valid_options, f"Received word '{option}' outside '{level}' wordbank"


    def test_play_vocab_modes(self, monkeypatch, capsys):
        '''
        Test correct game modes
        '''

        # test synonyms
        inputs = iter(["A", "B"] * 4)  # mock user choices
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        package.play_vocab("easy", "synonyms", 8)  # start vocab quiz with sample parameters

        captured = capsys.readouterr()

        assert "Which word is a synonym" in captured.out, f"Expected synonyms, but got none"
        assert "Which word is an antonym" not in captured.out, f"Expected no antonyms, but got antonyms" # should not ask about antonyms

        # test antonyms
        inputs = iter(["A", "B"])  # Mock user choices
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        package.play_vocab("easy", "antonyms", 2)  # start vocab quiz with sample parameters

        captured = capsys.readouterr()

        assert "Which word is an antonym" in captured.out, f"Expected antonyms, but got none"
        assert "Which word is a synonym" not in captured.out, f"Expected no synonyms, but got synonyms"# should not ask about synonyms

        # test both
        inputs = iter(["A", "B"])  # Mock user choices
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        package.play_vocab("easy", "both", 2)  # start vocab quiz with sample parameters

        captured = capsys.readouterr()

        assert "Which word is a synonym" in captured.out or "Which word is an antonym" in captured.out, f"Expected either antonyms or synonyms, but got neither"


    def test_play_vocab_nums(self, monkeypatch, capsys):
        '''
        Check that the number of questions is correct
        '''
        num_questions = 3  # expected num

        inputs = iter(["A"] * num_questions)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        package.play_vocab("easy", "synonyms", num_questions)  # start vocab quiz with sample parameters

        captured = capsys.readouterr() 

        # check number of questions asked
        question_count = captured.out.count("Which word is a")

        assert question_count == num_questions, f"Expected {num_questions} questions, but got {question_count}"

        # check number in final score
        match = re.search(r"(\d+)/(\d+)", captured.out)
        assert match, "Could not find score in output"
        total_num = int(match.group(2))

        assert num_questions == total_num, f"Expected score out of {num_questions}, but got {total_num}"


    def test_play_vocab_scoring(self, monkeypatch, capsys):
        '''
        Check overall score is correct based on feedback
        '''

        num_questions = 6
        inputs = iter(["A"] * num_questions)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        package.play_vocab("easy", "synonyms", num_questions)  # start vocab quiz with sample parameters

        captured = capsys.readouterr()
        point_count = captured.out.count("Correct!")
        incorrect_count = captured.out.count("Incorrect")
        assert (point_count + incorrect_count) == num_questions, f"Expected {num_questions} total feedback, received {point_count + incorrect_count}"

        match = re.search(r"(\d+)/(\d+)", captured.out)

        assert match, "Could not find score in output"
        
        score_earned = int(match.group(1))
        assert score_earned == point_count, f"Expected score of {point_count}, received {score_earned}"
        assert 0 <= score_earned <= num_questions, f"Invalid score {score_earned} out of {num_questions}"

        match = re.search(r"(\d+)%", captured.out)

        assert int(score_earned/num_questions * 100) == int(match.group(1)), f"Expected calculated score of {int(score_earned * 100/num_questions)}%, received {int(match.group(1))}%"




    def test_play_science(self):
        pass