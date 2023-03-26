from console_gfx import *

def option_menu():
    print("\n\nRLE Menu\n"
          "--------\n"
          "0. Exit\n"
          "1. Load File\n"
          "2. Load Test Image\n"
          "3. Read RLE String\n"
          "4. Read RLE Hex String\n"
          "5. Read Data Hex String\n"
          "6. Display Image\n"
          "7. Display RLE String\n"
          "8. Display Hex RLE Data\n"
          "9. Display Hex Flat Data\n")
    return int(input("Select a Menu Option: "))


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


def hex_char_encode(char):
    if char == 10:
        return 'a'
    elif char == 11:
        return 'b'
    elif char == 12:
        return 'c'
    elif char == 13:
        return 'd'
    elif char == 14:
        return 'e'
    elif char == 15:
        return 'f'
    elif char < 10:
        return str(char)


def to_hex_string(data):
    data_len = len(data)
    data_to_hex_string = ""
    for i in range(data_len):
        char = data[i]
        digit = hex_char_encode(char)
        data_to_hex_string += digit
    return data_to_hex_string


def count_runs(flat_data): 
    tempvalue = flat_data[0]
    runs = 1
    repetitions = 0
    for i in flat_data:
        if i != tempvalue:
            runs += 1
        else:
            repetitions += 1
            if repetitions == 15:
                runs += 1
                repetitions = 0
        tempvalue = i
    return runs


def encode_rle(flat_data):
    tempvalue = flat_data[0]
    rle_quantity = 1
    output = []
    for i in flat_data[1:]:
        if i == tempvalue:
            rle_quantity += 1
            if rle_quantity == 15:
                output.append(rle_quantity)
                output.append(tempvalue)
                rle_quantity = 0
        else:
            output.append(rle_quantity)
            output.append(tempvalue)
            rle_quantity = 1
            tempvalue = i
    if output[-1] != tempvalue or output[-2] != rle_quantity:
        output.append(rle_quantity)
        output.append(tempvalue)
    return output


def get_decoded_length(rle_data):
    decoded_length = 0
    for i in rle_data[0::2]:
        decoded_length += i
    return decoded_length


def decode_rle(rle_data):
    decoded_data = []
    for i in range(0, len(rle_data), 2):
        run_length = rle_data[i]
        run_value = rle_data[i+1]
        decoded_data += [run_value] * run_length
    return decoded_data


def decode_rle_string_to_Hex_RLE_Data(rle_string):
    decoded_data = ""
    rle_string = rle_string.split(":")
    for i in range(0, len(rle_string)):
        length_part = hex_char_encode(int(rle_string[i][:-1]))
        value_part = rle_string[i][-1]
        decoded_data += str(length_part)
        decoded_data += str(value_part)
    return decoded_data


def hex_RLE_Data_to_rle_string(hex_rle_data):
    output = ""
    for i in range(0, len(hex_rle_data), 2):
        output += str(hex_char_decode(hex_rle_data[i]))
        output += str(hex_rle_data[i+1])
        output += ":"
    output = output[:-1]
    return output


def rle_string_to_hex_flat_data(rle_string):
    output = ""
    rle_string = rle_string.split(":")
    for i in range(len(rle_string)):
        length_part = int(rle_string[i][:-1])
        value_part = str(rle_string[i][-1])
        output += value_part * length_part
    return output 

def string_to_data(data_string):
    data_len = len(data_string)
    hex_string_to_data = []
    for i in range(data_len):
        char = data_string[i]
        digit = hex_char_decode(char)
        hex_string_to_data.append(digit)
    return hex_string_to_data


def to_rle_string(rle_data):
    result = ""
    for i in range(0, len(rle_data), 2):
        run_length = rle_data[i]
        run_value = rle_data[i+1]
        result += f"{run_length:02d}{hex(run_value)[-1]}:"
    return result[:-1]


def string_to_rle(rle_string):
    rle_data = []
    for s in rle_string.split(":"):
        run_length = int(s[:2])
        run_value = int(s[2:], 16)
        rle_data.extend([run_length, run_value])
    return rle_data


# Some extra functions were made just to pass ZyBooks grading criteria
# and were unnecessary in the following option menu.
def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    option = 10
    image_data = []

    while option != 0:
        option = option_menu()
        if option == 0:
            break
        elif option == 1:
            file_to_load = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(file_to_load)
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.')
        elif option == 3:
            rle_string = input("Enter an RLE string to be decoded: ")
        elif option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data: ")
        elif option == 5:
            flat_hex_string = input("Enter the hex string holding flat data: ")
        elif option == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(image_data)
        elif option == 7:
            rle_string = hex_RLE_Data_to_rle_string(rle_hex_string)
            print(f"RLE representation: {rle_string}")
        elif option == 8:
            rle_hex_string = decode_rle_string_to_Hex_RLE_Data(rle_string)
            print(f"RLE hex values: {rle_hex_string}")
        elif option == 9:
            flat_hex_string = rle_string_to_hex_flat_data(rle_string)
            print(f"Flat hex values: {flat_hex_string}")
        else:
            print("Please choose an option from 0 through 9.")


if __name__ == '__main__':
    main()