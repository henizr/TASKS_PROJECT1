def check_length(words: tuple) -> tuple:
    min_len_word: int = len(words[0])
    max_len_word: int = len(words[0])
    words_lens = [min_len_word]

    for i in range(1, len(words)):
        current_word_len: int = len(words[i])
        words_lens.append(current_word_len)

        if current_word_len < min_len_word:
            min_len_word = current_word_len
        if current_word_len > max_len_word:
            max_len_word = current_word_len

    middle_word_length = round(sum(words_lens) / len(words))

    return (min_len_word, max_len_word, middle_word_length)

print(check_length(words=("да", "люблю свою работу", "конечно")))

from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))