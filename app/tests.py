from django.test import TestCase

import unittest

from .laskin import plus, sana


class LaskinTests(TestCase):
    def test_plus(self):
        # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual
        self.assertEqual(plus(7, 2), 9)


    def test_sana(self):
        # testaa että numerot lasketaan yhteen oikein, TestCasen metodi assertEqual
        self.assertEqual(sana(), "hei")


    def test_plus_string(self):
        # Testaa että merkkijononumeroita ei voi laskea yhteen
        self.assertNotEqual(plus("700", "200"), 900)
   

    @unittest.expectedFailure
    def test_plus_should_fail(self):
        self.assertEqual(plus(7, 3), "10")
