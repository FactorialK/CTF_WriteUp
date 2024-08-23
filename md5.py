import hashlib
import os

text = "cockroaches"
hashed_text = hashlib.md5(text.encode()).hexdigest()
print(hashed_text)
