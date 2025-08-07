from collections import defaultdict


def generate_average_report(logs):
    endpoint_stats = defaultdict(lambda: {'count': 0, 'total_time': 0.0})

    for log in logs:
        url = log['url'].split('...')[0]  # Remove variable parts of URL
        endpoint_stats[url]['count'] += 1
        endpoint_stats[url]['total_time'] += log['response_time']

    report = []
    for endpoint, stats in sorted(endpoint_stats.items()):
        avg_time = stats['total_time'] / stats['count']
        report.append((endpoint, stats['count'], round(avg_time, 3)))

    return report