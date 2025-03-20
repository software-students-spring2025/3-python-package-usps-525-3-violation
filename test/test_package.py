import pytest
from packagepackage import package
import random
import re


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

    def test_play_geo(self, monkeypatch, capsys):
        num_questions = 8
    
        questions = {
            "easy": {
                1: "What is the capital of Germany?",
                2: "Which continent is home to the Sahara Desert?",
                3: "Which country has the largest population in the world?",
                4: "Which U.S. state is known for having the Grand Canyon?",
                5: "What is the name of the mountain range that separates Europe and Asia?",
                6: "Which ocean borders the eastern coast of the United States?",
                7: "What is the capital of Argentina?",
                8: "Which country is known for the ancient ruins of Machu Picchu?",
                9: "Which major river flows through the city of London?",
                10: "What is the name of the coldest continent on Earth?",
                11: "Which African country is famous for its pyramids?",
                12: "What is the capital of Japan?",
                13: "Which U.S. state is famous for its large potato production?",
                14: "Which country is home to the Taj Mahal?",
                15: "What is the name of the sea located between Europe and Africa?"
            }
        }
    
        answers = {
            "easy": {
                1: "Berlin",
                2: "Africa",
                3: "China",
                4: "Arizona",
                5: "Ural Mountains",
                6: "Atlantic",
                7: "Buenos Aires",
                8: "Peru",
                9: "Thames",
                10: "Antarctica",
                11: "Egypt",
                12: "Tokyo",
                13: "Idaho",
                14: "India",
                15: "Mediterranean Sea"
            }
        }
    
        selected_questions = random.sample(list(questions["easy"].keys()), num_questions)
        simulated_answers = iter([answers["easy"][q] for q in selected_questions])
    
        monkeypatch.setattr('builtins.input', lambda _: next(simulated_answers))
    
        correct_answers = package.play_geo(numOfQuestions=num_questions, difficulty="easy")
        captured = capsys.readouterr()
    
        question_count = captured.out.count("?")
        assert question_count == num_questions, f"Expected {num_questions} questions, got {question_count}"
    
        match = re.search(r"Your final score: (\d+)/(\d+) \((\d+)%\)", captured.out)
        assert match, "Could not identify final score output"
    
        correct_count = int(match.group(1))
        total_questions = int(match.group(2))
        percentage_score = int(match.group(3))
    
        assert total_questions == num_questions, f"Expected {num_questions} total questions, got {total_questions}"
        assert correct_count == correct_answers, f"Expected {correct_answers} correct answers, got {correct_count}"
        assert percentage_score == int((correct_count / total_questions) * 100), f"Expected {int((correct_count / total_questions) * 100)}% score, got {percentage_score}%"
    
        assert "Correct!" in captured.out or "Incorrect!" in captured.out, "Expected at least one correct or incorrect message"
    
        package.play_geo(numOfQuestions=8, difficulty="invalid")
        captured = capsys.readouterr()
        print(captured.out)
        print("this is where captured out is located")
        assert "Please choose either easy, medium, or hard in difficulty level." in captured.out, "Expected error message for invalid difficulty level."

    def test_play_vocab_invalid_args(self, monkeypatch, capsys):
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

        # test invalid answers
        inputs = iter(["acsjcoiaj", "A", "B"])  # mock user choices
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

        package.play_vocab("easy", "synonyms", 2)  # start vocab quiz with sample parameters

        captured = capsys.readouterr()
        assert "Invalid option" in captured.out, f"Expected invalid option detection, did not detect"



    def test_play_vocab_levels(self, monkeypatch, capsys):
        '''
        Test that question words and answer options come from wordbank
        Test that words come from correct level
        '''
        wordbank = {
   "easy": [
      ("Love", "Like", "Hate"),
      ("Happy", "Joyful", "Sad"),
      ("Fast", "Quick", "Slow"),
      ("Big", "Large", "Small"),
      ("Easy", "Simple", "Difficult"),
      ("Loud", "Noisy", "Quiet"),
      ("Hot", "Warm", "Cold"),
      ("Dark", "Dim", "Bright"),
      ("Strong", "Powerful", "Weak"),
      ("Clean", "Tidy", "Messy"),
      ("Friendly", "Kind", "Mean"),
      ("Soft", "Gentle", "Rough"),
      ("Smart", "Clever", "Dumb"),
      ("Fun", "Enjoyable", "Boring"),
      ("Shout", "Yell", "Whisper"),
      ("Wet", "Damp", "Dry"),
      ("Brave", "Courageous", "Fearful"),
      ("Thin", "Slim", "Thick"),
      ("New", "Fresh", "Old"),
      ("Safe", "Secure", "Dangerous")
   ],
   "medium": [
      ("Muted", "Faint", "Blaring"),
      ("Sturdy", "Robust", "Frail"),
      ("Vivid", "Radiant", "Subdued"),
      ("Lazy", "Idle", "Energetic"),
      ("Sharp", "Pointed", "Dull"),
      ("Brisk", "Lively", "Sluggish"),
      ("Famous", "Renowned", "Obscure"),
      ("Shy", "Timid", "Bold"),
      ("Smooth", "Even", "Bumpy"),
      ("Lucky", "Fortunate", "Hapless"),
      ("Heavy", "Weighty", "Light"),
      ("Precise", "Exact", "Vague"),
      ("Curious", "Inquisitive", "Indifferent"),
      ("Deep", "Profound", "Shallow"),
      ("Proud", "Confident", "Ashamed"),
      ("Polite", "Courteous", "Rude"),
      ("Elusive", "Evasive", "Obvious"),
      ("Precise", "Exact", "Vague"),
      ("Tough", "Sturdy", "Fragile"),
      ("Eager", "Keen", "Reluctant")
   ],
   "hard": [
      ("Ephemeral", "Transient", "Perpetual"),
      ("Maelstrom", "Turmoil", "Tranquil"),
      ("Obsequious", "Sycophantic", "Contemptuous"),
      ("Eloquent", "Articulate", "Incoherent"),
      ("Diligent", "Industrious", "Indolent"),
      ("Frugal", "Thrifty", "Wasteful"),
      ("Conceited", "Imperious", "Humble"),
      ("Elucidate", "Clarify", "Obfuscate"),
      ("Intrepid", "Dauntless", "Pusillanimous"),
      ("Exultant", "Jubilant", "Melancholic"),
      ("Antediluvian", "Obsolete", "Voguish"),
      ("Ostentatious", "Flamboyant", "Austere"),
      ("Meticulous", "Punctilious", "Negligent"),
      ("Gregarious", "Convivial", "Reticent"),
      ("Impartial", "Nonpartisan", "Prejudiced"),
      ("Perspicacious", "Astute", "Barmy"),
      ("Clandestine", "Surreptitious", "Overt"),
      ("Phlegmatic", "Placid", "Mercurial"),
      ("Lethargic", "Torpid", "Zestful"),
      ("Amicable", "Cordial", "Hostile")
   ]
   }

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
    
    def test_num_questions_science(self, capsys):
        package.play_science(num_questions=11)
        captured = capsys.readouterr()
        assert "Maximum of 10 questions\n" == captured.out
    
    def test_difficulty_science(self, capsys):
        package.play_science(difficulty="invalid")
        captured = capsys.readouterr()
        assert "Invalid Difficulty\n" == captured.out
        
    def test_sample_play_science(self, monkeypatch, capsys):
        # test easy
        monkeypatch.setattr("builtins.input", lambda _: "A")
        package.play_science(num_questions=10, difficulty="easy")
        captured = capsys.readouterr()
        num_correct = captured.out.count("Correct!")
        num_incorrect = captured.out.count("Incorrect!")
        assert isinstance(num_correct, int)
        assert isinstance(num_incorrect, int)
        assert 0 <= num_correct <= 10
        assert 0 <= num_incorrect <= 10
        assert num_correct + num_incorrect == 10
        
        # test hard
        monkeypatch.setattr("builtins.input", lambda _: "A")
        package.play_science(num_questions=10, difficulty="hard")
        captured = capsys.readouterr()
        num_correct = captured.out.count("Correct!")
        num_incorrect = captured.out.count("Incorrect!")
        assert isinstance(num_correct, int)
        assert isinstance(num_incorrect, int)
        assert 0 <= num_correct <= 10
        assert 0 <= num_incorrect <= 10
        assert num_correct + num_incorrect == 10
        
        # test mix
        monkeypatch.setattr("builtins.input", lambda _: "A")
        package.play_science(num_questions=10, difficulty="mix")
        captured = capsys.readouterr()
        num_correct = captured.out.count("Correct!")
        num_incorrect = captured.out.count("Incorrect!")
        assert isinstance(num_correct, int)
        assert isinstance(num_incorrect, int)
        assert 0 <= num_correct <= 10
        assert 0 <= num_incorrect <= 10
        assert num_correct + num_incorrect == 10
        