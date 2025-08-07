import pytest

from reports import generate_average_report


@pytest.fixture
def sample_logs():
    return [
        {'url': '/api/endpoint1', 'response_time': 0.1},
        {'url': '/api/endpoint1', 'response_time': 0.2},
        {'url': '/api/endpoint2', 'response_time': 0.3},
    ]


def test_generate_average_report(sample_logs):
    report = generate_average_report(sample_logs)
    assert len(report) == 2
    assert ('/api/endpoint1', 2, 0.15) in report
    assert ('/api/endpoint2', 1, 0.3) in report