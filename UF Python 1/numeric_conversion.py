def hex_char_decode(char):
    if char == 'a':
        return 10
    elif char == 'b':
        return 11
    elif char == 'c':
        return 12
    elif char == 'd':
        return 13
    elif char == 'e':
        return 14
    elif char == 'f':
        return 15
    else:
        return int(char)


def hex_string_decode(hex_str):
    hex_str = hex_str.lower()  # Added for ZyBook unit testing of specific functions
    if '0x' in hex_str:
        hex_str = hex_str[2:]
    hex_len = len(hex_str)
    result = 0
    for i in range(hex_len):
        char = hex_str[hex_len - i - 1]
        digit = hex_char_decode(char)
        result += (digit * (16 ** i))
    return result


def binary_string_decode(binary):
    if '0b' in binary:
        binary = binary[2:]
    binary_len = len(binary)
    result = 0
    for i in range(binary_len):
        char = binary[binary_len - i - 1]
        if char == '1':
            result += 2 ** i
    return result


def binary_to_hex(binary):
    intermediate = binary_string_decode(binary)
    result = ''
    while intermediate > 0:
        hexdigit = intermediate % 16
        if hexdigit < 10:
            result = str(hexdigit) + result
        else:
            result = chr(hexdigit - 10 + ord('a')) + result
        intermediate //= 16
    return result


def main():
    option = '0'
    while option != '4':
        option = input('Decoding Menu\n'
                       '-------------\n'
                       '1. Decode hexadecimal\n'
                       '2. Decode binary\n'
                       '3. Convert binary to hexadecimal\n'
                       '4. Quit\n\n'
                       'Please enter an option: ')

        if option == '1':
            hex_str = input('Please enter the numeric string to convert: ').lower()
            result = hex_string_decode(hex_str)
            print(f'Result: {result}')

        elif option == '2':
            binary = input('Please enter the numeric string to convert: ').lower()
            result = binary_string_decode(binary)
            print(f'Result: {result}')

        elif option == '3':
            binary = input('Please enter the numeric string to convert: ').lower()
            result = binary_to_hex(binary)
            print(f'Result: {result}')

        elif option == '4':
            print('Goodbye!')

if __name__ == '__main__':
    main()