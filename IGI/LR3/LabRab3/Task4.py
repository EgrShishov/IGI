
def task4():
    """
    a) определить количество заглавных строчных букв;
    б) найти первое слово, содержащее букву 'z' и его номер;
    в) вывести строку, исключив из нее слова, начинающиеся с 'a'
    :return:
    """
    input_text = ("o she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, "
                  "whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, "
                  "when suddenly a White Rabbit with pink eyes ran close by her.")
    up, lower = count_uppercase_and_lowercase_letters(input_text)
    print(f'Amount of uppercase letters: {up}, amount of lowercase letters: {lower}')
    print(f'First word with letter "z" {find_first_word_with_letter(input_text, "z")}')
    print(f'New string: \n{remove_words_with_letter(input_text, "a")}')


def count_uppercase_and_lowercase_letters(text):
    upper_count = 0
    lower_count = 0
    for ch in text:
        if ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1

    return upper_count, lower_count


def find_first_word_with_letter(text, letter):
    words = text.split(' ')
    for index, word in enumerate(words):
        if word.startswith(letter):
            if word.endswith(","):
                word = word.replace(",", "", 1)
                return index, word


def remove_words_with_letter(text, letter):
    words = text.split(' ')
    for word in words:
        if word.startswith(letter):
            words.remove(word)
    return " ".join(words)

