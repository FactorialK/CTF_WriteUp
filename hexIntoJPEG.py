def reverse_4_bytes(data):

    reversed_data = bytearray()
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        if len(chunk) == 4:
            reversed_data.extend(chunk[::-1])
        else:
            reversed_data.extend(chunk)
    return bytes(reversed_data)

# Read the file with reversed byte order
with open("challengefile", "rb") as file:
    file_content = file.read()

# Reverse every 4 bytes
corrected_content = reverse_4_bytes(file_content)

with open("corrected_challengefile","wb") as corrected_file:
    corrected_file.write(corrected_content)

print("file withcorrected byte order created successfully!")

hex_data = corrected_content.hex()

binary_data = bytes.fromhex(hex_data)

with open("challeng_img.jpeg", "wb") as image_file:
    image_file.write(binary_data)


print("JPEG created successfully!")