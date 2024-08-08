import base64

encode_str = input("Input message > ")

try:
    decode_bytes = base64.b64decode(encode_str)
    decode_str = decode_bytes.decode('utf-8')
    print("The decode output is > ", decode_bytes)
    print("The decode output is > ", decode_str)
except Exception as e:
    print("Error :", e)