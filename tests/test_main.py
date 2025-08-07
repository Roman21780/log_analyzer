from unittest.mock import patch

from main import parse_args


def test_parse_args():
    with patch('sys.argv', ['main.py', '--file', 'file1.log', 'file2.log', '--report', 'average']):
        args = parse_args()
        assert args.file == ['file1.log', 'file2.log']
        assert args.report == 'average'