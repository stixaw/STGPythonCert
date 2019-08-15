# Number to String module


def get_num(number):
    three_digit_num = ""
    s_number = "{0}".format(number)

    digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
              'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if len(s_number) < 3 and number < 20:
        three_digit_num = digits[number]

    else:

        # get hundred value
        if len(s_number) == 3:
            num: int = s_number[len(s_number)-3: 1]
            if num > 0:
                three_digit_num = three_digit_num + digits[num] + " hundred"
            else:
                three_digit_num = three_digit_num

        # get tens value
        tens_num: int = s_number[len(s_number)-2: 3]
        if tens_num == 00:
            three_digit_num = three_digit_num

        if tens_num > 0:
            if tens_num >= 20:
                three_digit_num = three_digit_num + " " + tens[tens_num[0]]

            if tens_num > 1 and tens_num <= 19:
                three_digit_num = three_digit_num + " " + digits[tens_num]
            else:
                one_num = tens_num[1]
                three_digit_num = three_digit_num + " " + digits[one_num]
