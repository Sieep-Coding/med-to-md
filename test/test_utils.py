import unittest
from unittest.mock import patch, MagicMock
import os
import utils

class TestUtilsMethods(unittest.TestCase):

    @patch('utils.subprocess.run')
    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_run_bash(self, mock_exists, mock_makedirs, mock_run):
        mock_exists.return_value = False
        mock_makedirs.return_value = None
        mock_run.return_value = MagicMock(returncode=0, stderr='', stdout="Success")

        filename = 'test.md'

        utils.Utility.run_bash(filename)

if __name__ == "__main__":
    unittest.main()