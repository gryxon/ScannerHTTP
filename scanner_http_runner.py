import argparse
from http_scanner.wrapper_scanner_http import WrapperBlackScannerHttp
from http_scanner.black_box_modules.getting_server_version import GetServerVersionModule
from http_scanner.black_box_modules.other_http_method import OtherHttpMethodModule
from http_scanner.black_box_modules.idle_scan import BotRecognitionModule
from http_scanner.black_box_modules.slowloris_module import SlowlorisModule
from http_scanner.black_box_modules.url_force import ForceAttackModule
from http_scanner.black_box_modules.url_dict import DictAttackModule
import time

def get_parsed_args():
    parser = argparse.ArgumentParser("Argsparser for Http scanner.")
    parser.add_argument("--url", help="Url of server", default="localhost",
                        type=str)
    parser.add_argument("--ip", help="IP Address of scanned server", default="localhost",
                        type=str)
    parser.add_argument("--port", help="Scanned server's port number", default=80,
                        type=int)
    parser.add_argument("--ip_bot", help="IP Address of zombie host", default="localhost",
                        type=str)
    parser.add_argument("--dict_path", help="Path to  url dictionary",
                        default="dict_path", type=str)
    parser.add_argument("-os", "--check_server_os", action="store_true",
                        help="Scan of http server version and OS of machine")
    parser.add_argument("-uc", "--update_content", action="store_true",
                        help="Check possibility of other http requests")
    parser.add_argument("-ssl", action="store_true",
                        help="Encrypt requests with ssl")
    parser.add_argument("-up", "--use_proxy", action="store_true",
                        help="Scan server through proxy")
    parser.add_argument("-pd", "--perform_dos", action="store_true",
                        help="Check server vulnerability for DoS attack")
    parser.add_argument("-f", "--find_hidden_files", action="store_true",
                        help="Find hidden files with url dictionary")
    parser.add_argument("-b", "--perform_brute", action="store_true",
                        help="Find hidden files with brute force")
    parser.add_argument("--bot", action="store_true",
                        help="Check if server filters ip of zombie host")
    return parser.parse_args()


if __name__ == "__main__":
    wrapper = WrapperBlackScannerHttp()

    args = get_parsed_args()
    ip = args.ip
    ip_bot = args.ip_bot
    port = args.port
    dict_path = args.dict_path

    if args.check_server_os:
        wrapper.add_module(GetServerVersionModule())
    if args.update_content:
        wrapper.add_module(OtherHttpMethodModule(path_to_link_dict=dict_path))
    if args.bot:
        wrapper.add_module(BotRecognitionModule())
    if args.perform_dos:
        wrapper.add_module(SlowlorisModule())
    if args.perform_brute:
        wrapper.add_module(ForceAttackModule())
    if args.find_hidden_files:
        wrapper.add_module(DictAttackModule(dict_name=dict_path))

    d = (ip, int(port), ip_bot)
    wrapper.scan(args.url, data=d)

    print(wrapper.get_result())
