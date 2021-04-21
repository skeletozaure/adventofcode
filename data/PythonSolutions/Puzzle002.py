import re
message = "LET-ME-IN"

def to_unary(my_string):
    bin_conv=''
    unary = ''

    for c in my_string:
        #formattage en binaire sur 7 positions
        bin_conv += f'{ord(c):07b}'

    for group in re.findall("(0+|1+)", bin_conv):
        if '0' in group:
            unary+= '00 ' + '0' * len(group) + ' '
        else:
            unary+= '0 ' + '0' * len(group) + ' '

    return unary[0:len(unary)-1]

print(to_unary(message))