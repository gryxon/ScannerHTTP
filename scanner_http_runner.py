import argparse

def get_parsed_args():
    parser = argparse.ArgumentParser("Argsparser for Http scanner.")
    parser.add_argument("--url", help="Url of server", default="localhost",
                        type=str)
    parser.add_argument("-o", action="store_true",
                        help="Scan of version http server and OS of machine")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_parsed_args()
    print args.o
    print args.url
