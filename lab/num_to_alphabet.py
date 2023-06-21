def num_to_alpha(num):
    num = num + 96
    return chr(num)


def num_to_alphabet(code):
    alpha_code = ""
    length = len(code)
    i = 0
    while i < length:
        if code[i + 2] == "#":
            alpha_code += num_to_alpha(int(code[i] + code[i + 1]))
            i += 3
        elif code[i] != "#":
            alpha = num_to_alpha(int(code[i]))
            alpha_code += alpha
            i += 1

    return alpha_code


print(num_to_alphabet("1213#4517#"))
