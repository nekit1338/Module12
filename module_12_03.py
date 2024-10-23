import unittest
import runner_and_tournament


class Tournament_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(value)

    def setUp(self):
        self.runner_01 = runner_and_tournament.Runner("Husein", 10)
        self.runner_02 = runner_and_tournament.Runner("Andrei", 9)
        self.runner_03 = runner_and_tournament.Runner("Nick", 3)

    def test_01(self):
        tour_01 = runner_and_tournament.Tournament(90, self.runner_01, self.runner_03)
        result = tour_01.start()
        self.all_results[1] = result
        result = list(result.values())
        self.assertTrue(result[-1] == "Nick")

    def test_02(self):
        tour_02 = runner_and_tournament.Tournament(90, self.runner_02, self.runner_03)
        result = tour_02.start()
        self.all_results[2] = result
        result = list(result.values())
        self.assertTrue(result[-1] == "Nick")

    def test_03(self):
        tour_03 = runner_and_tournament.Tournament(90, self.runner_01, self.runner_02, self.runner_03)
        result = tour_03.start()
        self.all_results[3] = result
        result = list(result.values())
        self.assertTrue(result[-1] == "Nick")


if __name__ == '__main__':
    unittest.main()