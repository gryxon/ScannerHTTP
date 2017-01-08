import argparse
from http_scanner.wrapper_scanner_http import WrapperBlackScannerHttp
from http_scanner.wrapper_scanner_http import WrapperWhiteScannerHttp
from http_scanner.black_box_modules.getting_server_version import GetServerVersionModule
from http_scanner.black_box_modules.other_http_method import OtherHttpMethodModule
from http_scanner.black_box_modules.idle_scan import BotRecognitionModule
from http_scanner.black_box_modules.slowloris_module import SlowlorisModule
from http_scanner.black_box_modules.url_force import ForceAttackModule
from http_scanner.black_box_modules.url_dict import DictAttackModule
from http_scanner.black_box_modules.check_ssl import CheckSsl
from http_scanner.enable_ssl import ssl_scan
from http_scanner.white_box_modules.conf_errors import ConfErrors
from http_scanner.white_box_modules.os_rec import OsRecognitionModule
from http_scanner.white_box_modules.permission_check import PermissionCheck
import requests
import time


def get_parsed_args():
    """
    Processing input function.

    :return: Processed Args
    """
    parser = argparse.ArgumentParser("Argsparser for Http scanner.")
    parser.add_argument("--url", help="Url of server", default="localhost",
                        type=str)
    parser.add_argument("--server", help="Server name", default="apache2",
                        type=str)
    parser.add_argument("--conf_path", help="Path to server configuration file", default="conf",
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
    parser.add_argument("-w", "--white_scan", action="store_true",
                        help="")
    parser.add_argument("-ssl", action="store_true",
                        help="Encrypt requests with ssl")
    parser.add_argument("-up", "--use_proxy", action="store_true",
                        help="Scan server through proxy")
    parser.add_argument("-pd", "--perform_dos", action="store_true",
                        help="Check server vulnerability for DoS attack")
    parser.add_argument("-f", "--find_hidden_files", action="store_true",
                        help="Find hidden files with url dictionary")
    parser.add_argument("-b", "--perform_brute",
                        help="Find hidden files with brute force", default=None,
                        type=str)
    parser.add_argument("--bot", action="store_true",
                        help="Check if server filters ip of zombie host")
    parser.add_argument("-pc", "--permission_check", action="store_true",
                        help="Check access permission for important files")
    parser.add_argument("-c", "--check_config_files", action="store_true",
                        help="Check dangerous server configuration")
    parser.add_argument("-osw", "--osw_server_checking", action="store_true",
                        help="Check OS version")
    parser.add_argument("-https", action="store_true", help="Check if ssl certificate is trusted")
    return parser.parse_args()


if __name__ == "__main__":

    args = get_parsed_args()

    if args.white_scan:
        wrapper = WrapperWhiteScannerHttp()
    else:
        wrapper = WrapperBlackScannerHttp()
    ip = args.ip
    ip_bot = args.ip_bot
    port = args.port
    dict_path = args.dict_path

    proxy = None
    if args.use_proxy:
        proxy = {"http": "144.217.162.239:3128"}
    if args.check_server_os:
        wrapper.add_module(GetServerVersionModule(proxies=proxy))
    if args.update_content:
        wrapper.add_module(OtherHttpMethodModule(path_to_link_dict=dict_path,
                                                 proxies=proxy))
    if args.bot:
        wrapper.add_module(BotRecognitionModule())
    if args.perform_dos:
        wrapper.add_module(SlowlorisModule())
    if args.perform_brute:
        brute_attrs = args.perform_brute.split(' ')
        wrapper.add_module(ForceAttackModule(proxies=proxy, start=int(brute_attrs[0]), stop=int(brute_attrs[1]),
                                             capital=bool(int(brute_attrs[2]))))
    if args.find_hidden_files:
        wrapper.add_module(DictAttackModule(dict_name=dict_path, proxies=proxy))
    if args.permission_check:
        wrapper.add_module(PermissionCheck(args.server))
    if args.osw_server_checking:
        wrapper.add_module(OsRecognitionModule())
    if args.check_config_files:
        wrapper.add_module(ConfErrors(args.conf_path))
    if args.https:
        wrapper.add_module(CheckSsl())

    d = (ip, int(port), ip_bot)
    if args.ssl:
        args.url = ssl_scan(args.url)
        try:
            requests.get(args.url)
        except:
            print "Cannot make an ssl scan, certificate problem, aborting..."
            exit()
    if not args.white_scan:
        wrapper.scan(args.url, data=d)
    else:
        wrapper.scan()

    for key, value in wrapper.get_result().iteritems():
        print key + ":"
        print value
