### unqork interview question

def simpleEvenLetters(letters: str):
    count = 0
    letter_dict = {}

    for char in letters:
        letter_dict[char] = letter_dict.get(char, 0) + 1

        
    for char in letter_dict:
        if letter_dict[char] % 2 > 0:
            count +=1

    return count

def setToggleEvenLetters(letters: str):
    odd_char = set()

    for char in letters:
        if char in odd_char:
            odd_char.remove(char)
        else:
            odd_char.add(char)

    return len(odd_char)

result = setToggleEvenLetters("aabbccb")
print(f"should be: 1 __ was: {result}")