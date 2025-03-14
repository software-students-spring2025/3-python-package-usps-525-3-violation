import pytest
from packagepackage import package


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

    def test_play_vocab(self):
        pass

    def test_play_science(self):
        pass