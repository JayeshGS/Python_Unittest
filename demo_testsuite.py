import unittest


from unittest_package.demo_unittest1 import TestClassDemo1
from unittest_package.setupteardown_classlevel import TestClassDemo2
from unittest_package.demo_assertionlist import TestCaseDemo3


tc1 = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestClassDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestClassDemo2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestCaseDemo3)


smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)