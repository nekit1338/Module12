import unittest
from Runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Egor")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Правильно")

    def test_run(self):
        runner = Runner("Igor")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Правильно")

    def test_challenge(self):
        runner1 = Runner("Anton")
        runner2 = Runner("Evgen")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Неправильно")


if __name__ == '__main__':
    unittest.main()
