import argparse
from datetime import datetime
from tabulate import tabulate
from log_analyzer.reports import generate_average_report
from log_analyzer.utils import read_logs_from_files


def parse_args():
    parser = argparse.ArgumentParser(description='Process log files and generate reports.')
    parser.add_argument('--file', required=True, nargs='+', help='Log file(s) to process')
    parser.add_argument('--report', required=True, choices=['average'], help='Type of report to generate')
    parser.add_argument('--date', help='Filter logs by date (format: YYYY-MM-DD)')
    return parser.parse_args()


def main():
    args = parse_args()

    # Read and filter logs
    logs = read_logs_from_files(args.file)

    if args.date:
        try:
            filter_date = datetime.strptime(args.date, '%Y-%m-%d').date()
            logs = [log for log in logs
                    if datetime.strptime(log['@timestamp'], '%Y-%m-%dT%H:%M:%S%z').date() == filter_date]
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD")
            return

    # Generate report
    if args.report == 'average':
        report_data = generate_average_report(logs)
        headers = ['Endpoint', 'Request Count', 'Average Response Time']
        print(tabulate(report_data, headers=headers, tablefmt='grid'))


if __name__ == '__main__':
    main()