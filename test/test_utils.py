import unittest
from unittest.mock import patch
import utils

class TestUtilsMethods(unittest.TestCase):

    @patch('utils.subprocess.run')
    @patch('os.makedirs')
    @patch('os.path.exists')
    def test_run_bash(self, mock_run):
        mock_run.return