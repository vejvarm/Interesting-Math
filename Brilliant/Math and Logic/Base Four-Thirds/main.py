def decimal2base(num, base_num, base_den, result=tuple()):
    """ Convert a decimal (base 10) number to fractional base (numerator/denominator) number"""

    if num:
        num, remainder = (num // base_num*base_den, num % base_num)
        result = (remainder,) + result

        num, result = decimal2base(num, base_num, base_den, result)

    return num, result


if __name__ == '__main__':
    print(decimal2base(19, 4, 3)[1])
