# from collections import abc

# class MorseMapping(abc.Mapping):
    # def __getitem__(self, key):
    #     return self.morse_alphabet[str(key)]

    # def __iter__(self):
    #     return iter(self.morse_alphabet)

    # def __len__(self):
    #     return len(self.morse_alphabet)


betw_letters = '  '
# words using "   /   " instead of 7 spaces to represent units time 
# as this is the most common text representation - ends up w/7 anyway.
betw_words = '/  ' 
morse_alphabet = {
    'a': '.-' + betw_letters,
    'b': '-...' + betw_letters,
    'c': '-.-.' + betw_letters,
    'd': '-..' + betw_letters,
    'e': '.' + betw_letters,
    'f': '..-.' + betw_letters,
    'g': '- -.' + betw_letters,
    'h': '....' + betw_letters,
    'i': '..' + betw_letters,
    'j': '.- - -' + betw_letters,
    'k': '-.-' + betw_letters,
    'l': '.-..' + betw_letters,
    'm': '- -' + betw_letters,
    'n': '-.' + betw_letters,
    'o': '- - -' + betw_letters,
    'p': '.- -.' + betw_letters,
    'q': '- -.-' + betw_letters,
    'r': '.-.' + betw_letters,
    's': '...' + betw_letters,
    't': '-' + betw_letters,
    'u': '..-' + betw_letters,
    'v': '...-' + betw_letters,
    'w': '.- -' + betw_letters,
    'x': '-..-' + betw_letters,
    'y': '-.- -' + betw_letters,
    'z': '- -..' + betw_letters,
    '1': '.- - - -' + betw_letters,
    '2': '..- - -' + betw_letters,
    '3': '...- -' + betw_letters,
    '4': '....-' + betw_letters,
    '5': '.....' + betw_letters,
    '6': '-....' + betw_letters,
    '7': '- -...' + betw_letters,
    '8': '- - -..' + betw_letters,
    '9': '- - - -.' + betw_letters,
    '0': '- - - - -' + betw_letters,
    '!': '-.-.- -' + betw_letters,
    '?': '..- -..' + betw_letters,
    '&': '.-...' + betw_letters,
    }

# The Mapping subclass has been a bust so far.
# May be simpler to look up directly.
def encode(text):
    text = text.replace('.', '.-.-.-') # special case
    words = text.lower().split(' ')
    output = ''
    i = 0
    for word in words:
        for char in word:
            if char in morse_alphabet:
                word = word.replace(char, morse_alphabet[char])
        output += word
        if i < len(words) - 1:
            output += betw_words
        i += 1
    return output

print (encode('hello world'))