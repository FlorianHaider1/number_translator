# This program is an encoder, that can translate binary, decimal, hexadecimal and roman numbers.
import pyinputplus as pyip

first_input = pyip.inputNum("Bitte Zahl eingeben: ")


# translate decimal to binary


def dec_bit_func(num):
    print("Binär (Funktion):\t\t", bin(num)[2:].zfill(8))


bit_horizontal = []


def dec_bit_manually(num):
    while num > 0:
        bit_horizontal.append(num % 2)
        num = num // 2
    return bit_horizontal
# save list and reverse


binary = dec_bit_manually(first_input)
reverse = binary[::-1]
binary_final = "".join([str(x) for x in reverse])


# translate hexadecimal


def dec_hex_func(num):
    print("Hexadezimal (Funtion):\t", hex(num)[2:])


hex_horizontal = []


def dec_hex_manually(num):
    while num > 0:
        hex_horizontal.append(num % 16)
        num = num // 16
    return hex_horizontal


hexamal = dec_hex_manually(first_input)
hexamal_reverse = hexamal[::-1]
dec_list = range(16)
hex_list = [hex(i)[2:] for i in range(16)]
hexamal_translation_table = dict(zip(dec_list, hex_list))


def hexamal_translate():
    hexamal_format = str()
    for i in hexamal_reverse:
        hexamal_format += str(hexamal_translation_table[i])
    print("Hexadezimal (Manuell):\t", hexamal_format)


# translate roman

decimal_roman_dictionary = {
    "A": {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX"},
    "B": {
        0: "",
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC"},
    "C": {
        0: "",
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM"},
    "D": {
        0: "",
        1: "M",
        2: "MM",
        3: "MMM"
    }

}


def dec_rom(num):
    if num > 3999:
        print("Römisch:\t\t\t\t Römische Zahlen gehen nur bis 3999")
        return
    num_str = str(num)
    counter = 64 + len(str(num))
    roman_str = ""
    for i in num_str:
        key = chr(counter)
        roman_str += decimal_roman_dictionary[key][int(i)]
        counter -= 1
    print("Römisch:\t\t\t\t", roman_str)


# print

dec_bit_func(first_input)
print("Binär (Manuell):\t\t", binary_final.zfill(8))
dec_hex_func(first_input)
dec_hex_manually(first_input)
hexamal_translate()
dec_rom(first_input)
