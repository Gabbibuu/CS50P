import sys
import random
from pyfiglet import Figlet

FONTS = Figlet().getFonts()
f = Figlet()

if len(sys.argv) == 1:
    input = input("Input: ").strip()
    f.setFont(font=random.choice(FONTS))
    print(f.renderText(input))

elif len(sys.argv) == 3:
    if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in FONTS:
        input = input("Input: ").strip()
        f.setFont(font=str(sys.argv[2]))
        print(f.renderText(input))
    else:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
