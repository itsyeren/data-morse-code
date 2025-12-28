from morse.mapping import MORSE

REVERSE_MORSE = {value: key for key, value in MORSE.items()}

def decode_word(morse_word):
    """
    Decodes a single Morse code word into English text.
    """
    letters = morse_word.split(" ")
    decoded_letters = []
    
    for code in letters:
        decoded_letters.append(REVERSE_MORSE[code]
                               )
    return "".join(decoded_letters)


def decode(morse_text):
    """
    Decodes a Morse code text into English.
    Words are separated by a pipe (|) and letters by a space.
    """
    words = morse_text.split("|")
    decoded_words = []

    for morse_word in words:
        decoded_words.append(decode_word(morse_word))
    
    return " ".join(decoded_words)


if __name__ == "__main__":
 # Example usage for one word
    MORSE_WORD = ".... .."
    print(decode_word(MORSE_WORD))

    # Example usage for one sentence
    MORSE_TEXT = ".... ..|--. ..- -.-- ..."
    print(decode_word(MORSE_TEXT))
