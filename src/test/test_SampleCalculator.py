from unittest import TestCase,skip
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

    def test_string_input(self):
        with self.assertRaises(ValueError):
            result = self.smapleCalculator.cohran("1.96", "0.5","0.95")
        with self.assertRaises(ValueError):
            result = self.smapleCalculator.marginOfError("1.96", "0.5","0.95")
        with self.assertRaises(ValueError):
            result = self.smapleCalculator.confidenceIntervalSmaple('0.9','0.8','0.6')


    @skip("waiting to be implement")
    def test_marginOfError(self):
        result = self.smapleCalculator.marginOfError(20,40,1.96)
        self.assertAlmostEqual(result,6.2,places=2)

