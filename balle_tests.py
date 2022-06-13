import unittest
import balle_locators as locators
import balle_methods as methods


class BalleMediaAppPositiveTestCases(unittest.TestCase):  # create class

    @staticmethod  # signal to Unittest that this is a static method
    def test_create_new_user():
        methods.setUp()
        methods.grow_your_clinic()
        methods.page_one()
        methods.page_two()
        methods.page_three()
        methods.page_four()
        methods.page_five()
        methods.tearDown()
