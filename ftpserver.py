from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import sys
import warnings
warnings.filterwarnings("ignore")
# The port the FTP server will listen on.
# This must be greater than 1023 unless you run this script as root.
FTP_PORT = 21

# The name of the FTP user that can log in.
FTP_USER = "anonymous"

# The FTP user's password.
FTP_PASSWORD = ""

# The directory the FTP user will have full read/write access to.
FTP_DIRECTORY = "./"

def print_user_password():
    if FTP_USER == "":
        user = "None"
    else:
        user = FTP_USER
    if FTP_PASSWORD == "":
        password = "None"
    else:
        password = FTP_PASSWORD
    print("[+] USER: {user}".format(user=user))
    print("[+] PASSWORD: {password}".format(password=password))


def banner():
    print("""
 __________________________
< FTP is Open, Connect me! >
 --------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
    """)

def main(dir=None):
    authorizer = DummyAuthorizer()
    if dir != None:

        ftp_dir = dir
    else:
        ftp_dir = FTP_DIRECTORY
    # Define a new user having full r/w permissions.
    authorizer.add_user(FTP_USER, FTP_PASSWORD, ftp_dir, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Optionally specify range of ports to use for passive connections.
    #handler.passive_ports = range(60000, 65535)

    address = ('', FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

def usage():
    print("""
Usage:
    python3 {script} <DIR>
Option:
    -h      Help message
""".format(script=sys.argv[0]))

if __name__ == '__main__':
    banner()
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        usage()
        exit()
    print_user_password()
    if len(sys.argv) == 2:
        main(sys.argv[1])
    if len(sys.argv) == 1:
        main()
