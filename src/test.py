import unittest
import json
from os import listdir
from os.path import isfile, join, splitext
from c_syntax import get_json


class Test(unittest.TestCase):
    def _test(self, input_filename, expected_output):
        expected_output = json.loads(expected_output)
        produced_output = json.loads(get_json(input_filename))

        self.assertDictEqual(expected_output, produced_output, input_filename)

        print('Test from file ' + input_filename + ' passed!')

    def test_files(self):
        test_files_dir_path = '../tests'
        in_filenames = [join(test_files_dir_path, f) for f in listdir(test_files_dir_path)
                        if isfile(join(test_files_dir_path, f)) and splitext(f)[1] == '.in']

        for in_filename in in_filenames:
            with open(in_filename[:-2] + 'out', 'r') as out_file:
                expected_output = out_file.read()
                self._test(in_filename, expected_output)


if __name__ == '__main__':
    unittest.main()
