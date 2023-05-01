import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Retrieve information of a GitHub User')
    parser.add_argument('username', type=str, help='GitHub username')
    parser.add_argument('domain', type=str, help='Freshdesk domain')
    args = parser.parse_args()
    return args.username, args.domain



