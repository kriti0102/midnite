import unittest
from unittest.mock import patch, MagicMock

# Assuming your modules are in the `src` folder, import BetFileHandler from the correct path
from main import BetFileHandler

class TestBetFileHandler(unittest.TestCase):
    @patch('main.process_bet_file')  # Mock process_bet_file
    def test_on_created(self, mock_process_bet_file):
        # Create a mock event that mimics a file being created
        event = MagicMock()
        event.is_directory = False  # Simulate a file, not a directory
        event.src_path = "/opt/src/landed_files/test_bet_file.csv"  # Simulate a file path

        # Instantiate the BetFileHandler
        handler = BetFileHandler()

        # Trigger the on_created method
        handler.on_created(event)

        # Assert that process_bet_file was called with the correct file path
        mock_process_bet_file.assert_called_once_with("/opt/src/landed_files/test_bet_file.csv")


if __name__ == '__main__':
    unittest.main()
