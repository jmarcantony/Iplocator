"""

    NOTE: To use this programme, you are going to need an access token which you can get for free by signing up at https://ipinfo.io/signup
    
    USAGE: python3 iplocate.py [ACCESS TOKEN] [PUBLIC IP OF TARGET] [OPTIONAL ARGUMENT]

    OPTIONAL ARGUMENT:
        --all: Prints all information
    
    Written in Python 3.9.1

    -Joseph Marc Antony

"""

from pprint import pprint
import ipinfo
import sys

def view_details(details, print_all=False):
    if not print_all:
        try:
            print(f"[+] Country: {details.country}")
            print(f"[+] City: {details.city}")
            print(f"[+] Location: {details.loc}")
            print(f"[+] Latitude: {details.latitude}")
            print(f"[+] Longitude: {details.longitude}")
            print(f"[+] Hostname: {details.hostname}")
        except:
            print(f"[-] {IP} was not a valid IP address or it was a private IP, try entering a public one.")
    else:
        pprint(details.all)


if len(sys.argv) < 3:
    if sys.argv[1] != "--help":
        print(f"USAGE: python {sys.argv[0]} [ACCESS TOKEN] [PUBLIC IP OF TARGET]")
    else:
        print(f"""

NOTE: To use this programme, you are going to need an access token which you can get for free by signing up at https://ipinfo.io/signup

USAGE: python {sys.argv[0]} [ACCESS TOKEN] [PUBLIC IP OF TARGET]

OPTIONAL ARGUMENT:
    --all: Prints all information

            """)
else:
    IP = sys.argv[2]
    access_token = sys.argv[1]

    handler = ipinfo.getHandler(access_token)
    ip_details = handler.getDetails(IP) 

    try:
        print_all = sys.argv[3]
        if print_all == "--all":
            view_details(ip_details, True)
        else:
            view_details(ip_details)
    except IndexError:
        view_details(ip_details)