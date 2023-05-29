import os, platform

print(50*"-")

print("[>>] FOLLOW MY FACEBOOK ACCOUNT")

print(50*"-")

os.system('xdg-open https://www.facebook.com/H4M11.YOUR.DAD')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from run64 import main

    main()

elif bit == '32bit':

    from run32 import main

    main()
