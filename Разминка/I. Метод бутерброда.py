def decrypt_sandwich(encoded):
    encoded = encoded[:-1]
    half = len(encoded) // 2
    original = [''] * len(encoded)

    for i in range(half):
        original[i] = encoded[i * 2]
        original[-(i + 1)] = encoded[i * 2 + 1]

    if len(encoded) % 2 == 1:
        original[half] = encoded[-1]

    return ''.join(original)


encoded_word = input().strip()
print(decrypt_sandwich(encoded_word))
