#BASE64 DECODER

import base64


# Encode
def base64_encoder(data):
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    return encoded_str

# Decode
def base64_decoder(encoded_str):
    encoded_bytes = encoded_str.encode('utf-8')
    decoded_bytes = base64.b64decode(encoded_bytes)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str

# put your data to be encoded after data on the first line
data = "" # data to be encoded
encoded_data = base64_encoder(data)
print("Encoded data:", encoded_data)

decoded_data = base64_decoder(encoded_data)
print("Decoded data:", decoded_data)
