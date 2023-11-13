import unittest
from xmax_gcode_process import *


class TestRead(unittest.TestCase):
    def test_get_gcode_list_just_gcode(self):
        test_list = read_file_to_list('../xmax_supported_commands.gcode', just_gcode=True)
        self.assertGreater(len(test_list), 0)

    def test_prefix_supported_prefixes(self):
        test_list = read_file_to_list('../xmax_supported_commands.gcode', just_gcode=True)
        test_pass = True
        failed_line = ''
        for line in test_list:
            if (not line.startswith('G')) and (not line.startswith('M')):
                failed_line = line
                test_pass = False
                break
        self.assertTrue(test_pass, f'Failed on line {failed_line}')


if __name__ == '__main__':
    unittest.main()