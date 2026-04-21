import sys
import unittest
from unittest.mock import patch, MagicMock
import os

# We import it after mocks if needed, but here we can just import it
try:
    import openf
except ImportError:
    pass

class TestOpenf(unittest.TestCase):
    @patch('sys.platform', 'win32')
    @patch('os.startfile', create=True)
    @patch('os.path.exists', return_value=True)
    def test_open_windows(self, mock_exists, mock_startfile):
        import openf
        openf.open_file("test.txt")
        mock_startfile.assert_called_with("test.txt")

    @patch('sys.platform', 'linux')
    @patch('subprocess.call')
    @patch('os.path.exists', return_value=True)
    def test_open_linux(self, mock_exists, mock_call):
        import openf
        openf.open_file("test.txt")
        mock_call.assert_called_with(["xdg-open", "test.txt"])

    @patch('sys.platform', 'linux')
    @patch('subprocess.call')
    @patch('os.path.exists', return_value=True)
    def test_open_multiple_files(self, mock_exists, mock_call):
        import openf
        from unittest.mock import call
        with patch('sys.argv', ['openf', 'file1.txt', 'file2.txt']):
            openf.main()
            mock_call.assert_has_calls([
                call(["xdg-open", "file1.txt"]),
                call(["xdg-open", "file2.txt"])
            ])

if __name__ == '__main__':
    unittest.main()
