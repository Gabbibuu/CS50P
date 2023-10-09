import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        bytes = ip.split(".")
        for ip_byte in bytes:
            if int(ip_byte) < 0 or int(ip_byte) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()