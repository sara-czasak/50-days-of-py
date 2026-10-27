import hashlib


def different_hash_algorithms(data):
    """Show how to use different hashing algorithms provided by hashlib."""
    print("\n--- Using Different Hashing Algorithms ---")
    print("Original String: ", data)

    encoded_data = data.encode()

    # SHA Family Algorithms
    print("\n--- SHA 2 Family Algorithms ---")
    print('SHA-224: ', hashlib.sha224(encoded_data).hexdigest())
    print('SHA-256: ', hashlib.sha256(encoded_data).hexdigest())
    print('SHA-384: ', hashlib.sha384(encoded_data).hexdigest())
    print('SHA-512: ', hashlib.sha512(encoded_data).hexdigest())

    # SHA-3 Family Algorithms (more secure than SHA-2)
    print("\n--- SHA 3 Family Algorithms ---")
    print('SHA3-224: ', hashlib.sha3_224(encoded_data).hexdigest())
    print('SHA3-256: ', hashlib.sha3_256(encoded_data).hexdigest())
    print('SHA3-384: ', hashlib.sha3_384(encoded_data).hexdigest())
    print('SHA3-512: ', hashlib.sha3_512(encoded_data).hexdigest())

    # SHAKE Algorithms (Extendable Output Functions - XOFs)
    print("\n--- SHAKE Algorithms ---")
    print(f'SHAKE-128 (20 bytes): {hashlib.shake_128(encoded_data).hexdigest(20)}')
    print(f'SHAKE-256 (32 bytes): {hashlib.shake_256(encoded_data).hexdigest(32)}')

    # BLAKE Algorithms (Faster Computation)
    print("\n--- BLAKE Algorithms ---")
    print(f'BLAKE2b (512 bits): {hashlib.blake2b(encoded_data).hexdigest()}')
    print(f'BLAKE2s (256 bits): {hashlib.blake2s(encoded_data).hexdigest()}')

    # MD5 SHA - 1 Algorithms (Deprecated/Insecure Algorithms)
    print("\n--- MD5 and SHA-1 Algorithms ---")
    print(f'MD5: {hashlib.md5(encoded_data).hexdigest()}')
    print(f'SHA-1: {hashlib.sha1(encoded_data).hexdigest()}')

    print("\n--- All Available Algorithms ---")
    print(hashlib.algorithms_available)
    print("\n--- End ---")


different_hash_algorithms("Hello, World!")