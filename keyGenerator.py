import random
import string

punctuations = "!,-./:;_"
chars = string.ascii_letters + string.digits + punctuations


key = "".join(random.choices(chars, k=18))

print(key)

