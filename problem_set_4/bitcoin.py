import sys
import requests


if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
        try:
            request = requests.get(
                f"https://api.coindesk.com/v1/bpi/currentprice.json"
            ).json()
            price = request["bpi"]["USD"]["rate_float"]
            print(f"${(price * n):,.4f}")
        except requests.RequestException:
            sys.exit(None)
    except ValueError:
        sys.exit("Argument is not a number")
else:
    sys.exit("Argument missing")
