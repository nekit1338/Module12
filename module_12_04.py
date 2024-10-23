import unittest
from module_12_01 import RunnerTest
from module_12_03 import Tournament_Test

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(Tournament_Test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)
