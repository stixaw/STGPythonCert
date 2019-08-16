# Number to String module

ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}
illions = {
    1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
    6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
    10: 'nonillion', 11: 'decillion'}


def is_number_positive(i):
    """
    Convert an integer in to it's word representation.

    say_number(i: integer) -> string
    """
    if i < 0:
        return _join('negative', _num_to_word(-i))
    if i == 0:
        return 'zero'
    return _num_to_word(i)


def _num_to_word(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')
    for illions_number, illions_name in illions.items():
        if i < 1000 ** (illions_number + 1):
            break
    return _divide(i, 1000 ** illions_number, illions_name)


def _divide(dividend, divisor, magnitude):
    return _join(
        _num_to_word(dividend // divisor),
        magnitude,
        _num_to_word(dividend % divisor),
    )


def _join(*args):
    return ' '.join(filter(bool, args))


def test_say_number(data, expected_output):
    """Test cases for say_number(i)."""
    output = is_number_positive(data)
    assert output == expected_output, \
        "\n    for:      {}\n    expected: {}\n    got:      {}".format(
            data, expected_output, output)
