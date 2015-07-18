import argparse
import yaml

import finsky.client

# top level parser
parser = argparse.ArgumentParser(description='Google Play Client')
subparsers = parser.add_subparsers(title="Commands")

# download action
parser_download = subparsers.add_parser("download", help="Download APK")
parser_download.add_argument('profile', action='store',
                             type=argparse.FileType('r'),
                             help='profile configuration in YAML')
parser_download.add_argument('doc', action='store', type=str,
                             help='app identifier')
parser_download.add_argument('--out', action='store',
                             type=argparse.FileType('wb'),
                             help='apk output file (defaults to ./<doc>.apk)')

def download(args):
    profile = yaml.load(args.profile)
    client = finsky.client.Client(**profile)
    details = client.details(args.doc)
    delivery = client.delivery_from_details(details)
    x = client.download_from_delivery(delivery, gzipped=False)
    if not args.out:
        filename = './%s.apk' % (args.doc)
        args.out = open(filename, 'wb')
    args.out.write(x)
    args.out.close()

parser_download.set_defaults(action=download)


def main():
    args = parser.parse_args()
    args.action(args)
