import unittest
from unittest.mock import patch
from io import StringIO
from vehicle2 import Vehicle

class TestVehicle(unittest.TestCase):
    def setUp(self):
        # Create a sample vehicle instance for testing
        self.vehicle = Vehicle("Toyota", 3456, "Blue", "petroleum")

    def test_display_info(self):
        # Test if the display_info method correctly displays vehicle information
        expected_output = "Name: Toyota\nLicense: 3456\nColor: Blue\nFuel: petroleum\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            self.vehicle.display_info()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
