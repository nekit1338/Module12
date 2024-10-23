import unittest
from module_12_01_changed import RunnerTest
from module_12_03_changed import Tournament_Test

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tournament_Test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
