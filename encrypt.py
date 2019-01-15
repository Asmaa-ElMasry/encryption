import string
import num2words


alpha_dict = dict(zip(string.ascii_uppercase, range(26)))
punctuation_marks = {' ': 26, ',': 27, '.': 28, '?': 29, '(': 30, ')': 31}


def convert_number_to_word(message):
    message_split = message.split()
    caesar_shift = int(message_split[0])
    new_message = []
    for word in message_split[1:]:
        try:
            number_in_word = int(word)
            new_message.append(num2words.num2words(number_in_word).upper())
        except ValueError:
            try:
                number_in_word = float(word)
                new_message.append(num2words.num2words(number_in_word).upper())
            except ValueError:
                new_message.append(word)
    return caesar_shift, ' '.join(new_message)


def caesar_shift_message(caesar_shift, message):
    new_message = ''
    for letter in message:
        if letter in alpha_dict:
            new_letter_val = alpha_dict[letter] + caesar_shift
            new_letter_val = new_letter_val > 25 and new_letter_val - 26 or new_letter_val < 0 and \
                             26 + new_letter_val or new_letter_val
            alpha_key = [alpha for alpha, index in alpha_dict.items() if index == new_letter_val][0]
            new_message += alpha_key
        else:
            new_message += letter
    return new_message


def equivalent_binary(message):
    bin_list = []
    for letter in message:
        if letter in alpha_dict:
            bin_list.append(get_binary_number(alpha_dict[letter]))
        if letter in punctuation_marks:
            bin_list.append(get_binary_number(punctuation_marks[letter]))
    return ''.join(bin_list)


def encode_binary(binary_message):
    binary_message_length = len(binary_message)
    encode_binary_message = ''
    for index in range(binary_message_length):
        if index == 0:
            encode_binary_message += str(int(binary_message[index]) + int(binary_message[index+1]))
        elif index < binary_message_length-1:
            encode_binary_message += str(int(binary_message[index-1]) + int(binary_message[index]) +
                                         int(binary_message[index + 1]))
        else:
            encode_binary_message += str(int(binary_message[index-1]) + int(binary_message[index]))
    return encode_binary_message


def convert_encode_to_bin(encoded_message):
    return ''.join([get_binary_number(int(number)) for number in encoded_message])


def get_binary_number(number):
    return bin(number)[2:].zfill(2)


def convert_to_hex(binary_message):
    return hex(int(binary_message, 2))[2:].upper()


def encrypt_message():
    hex_list = []
    for i in range(int(input())):
        caesar_shift, message = convert_number_to_word(input())
        message = caesar_shift_message(caesar_shift, message)
        binary_message = equivalent_binary(message)
        encoded_message = encode_binary(binary_message)
        binary_message = convert_encode_to_bin(encoded_message)
        hex_list.append(convert_to_hex(binary_message))
    return hex_list
