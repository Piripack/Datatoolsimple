from word2number import w2n

def text_to_number(text):
    try:
        return w2n.word_to_num(text)
    except ValueError:
        return text