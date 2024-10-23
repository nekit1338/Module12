import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Повезло")
    def test_walk(self):
        try:
            runner = Runner("Egor", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")
            logging.exception("Произошла ошибка:", exc_info=True)

    @unittest.skipIf(is_frozen, "Повезло")
    def test_run(self):
        try:
            runner = Runner(10, 10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 200)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")
            logging.exception("Произошла ошибка:", exc_info=True)


if __name__ == '__main__':
    unittest.main()
