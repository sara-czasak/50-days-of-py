import hashlib


# E.g., use case: storing passwords in databases
def basic_string_hashing(original_string):
    # Encoding data to bytes
    data_to_bytes = original_string.encode('utf-8')
    # Hashing the data
    sha256_hash_object = hashlib.sha256(data_to_bytes)
    # Hash value hex
    hash_hex_value = sha256_hash_object.hexdigest()

    print("Original String: ", original_string)
    print("Hash Value: ", hash_hex_value)
    return hash_hex_value


one = basic_string_hashing(original_string="Let's start 50 days of advanced python!")
two = basic_string_hashing(original_string="Let's start 50 days of advanced python!")
print(one == two)