from unittest import TestCase
from src.project.SampleCalculator import SampleCalculator

class TestSampleCalculator(TestCase):
    @classmethod
    def setUpClass(self):
        self.smapleCalculator = SampleCalculator()

    @classmethod
    def tearDownClass(self):
        if self.smapleCalculator is not None:
            self.smapleCalculator = None

    def test_cohran(self):
        result =  self.smapleCalculator.cohran(1.96,0.5,0.95)
        self.assertAlmostEqual(result,385)

