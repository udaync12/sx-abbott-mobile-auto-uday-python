import sys
import os
#sys.path.append(sys.path[0] + "/...")
#sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from TestCases.test_LaunchApp import TestGeneralStoreHomePage

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((test_loader.loadTestsFromTestCase(TestGeneralStoreHomePage)))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
