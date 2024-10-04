import random,string
print(f"{ "".join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(0,12))} ")