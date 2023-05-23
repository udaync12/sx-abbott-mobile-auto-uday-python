# Press the green button in the gutter to run the script.
import unittest
from TestCases.test_GeneralStore_App import TestGeneralStoreApp

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneralStoreApp)
    unittest.TextTestRunner(verbosity=2).run(suite)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
