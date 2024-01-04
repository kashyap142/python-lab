if __name__ == "__main__":
    file_name = input("Enter file name: ")

    f = open(file_name, "r")

    # print(f.read())
    str = f.read()

    sentence_cnt = str.count('?') + str.count('.') + str.count('!')
    word_cnt = len(str.split())
    char_cnt = len(str)

    print(f"Sentences count: {sentence_cnt}\nWord count: {word_cnt}\nCharacter count: {char_cnt}\n")


