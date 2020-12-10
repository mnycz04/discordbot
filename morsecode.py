"""Converts a string to morse code"""

morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
              'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


def convert_to_morse_code(phrase):
    """
    Converts :param phrase to morse code
    :returns morse code of phrase
    """

    phrase_list = []
    phrase = phrase.strip(""",./<>?;':"[]{}-_=+/*`~!@#$%^&*()""")
    translation_list = []

    for letter in range(len(phrase)):
        phrase_list.append(phrase[letter])

    for letter in phrase_list:
        try:
            translation_list.append(morse_code[letter])
        except Exception:
            continue

    translation = ' '.join(translation_list[:]).strip()

    return translation
