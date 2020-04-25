import argparse
import sys

from sadaf import socket_bind

def bind_command(args):
    socket_bind.bind_port(args.port)

def list_command(args):
    print('list: %s'%args)

def main(argv=sys.argv):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd")

    parser_list = subparsers.add_parser('ls', help='List all active sockets')
    parser_list.set_defaults(func=list_command)

    parser_bind = subparsers.add_parser('bind', help='Creates a socket a binds it to listen on a port')
    parser_bind.add_argument('port', type=int, action='store', help='Port to listen on')
    parser_bind.set_defaults(func=bind_command)

    args = parser.parse_args()

    if len(argv) == 1:
        parser.print_help()
    else:
        args.func(args)
        
if __name__ == "__main__":
    main()
