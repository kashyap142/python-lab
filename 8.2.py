
if __name__ == "__main__":
    src = open('test.txt', 'r')

    target = open('target.txt', 'w')

    str = src.read()
    cnt = str.count('\n')

    if str[-1] != '\n':
        cnt += 1

    for ch in str:
        target.write(ch.lower())

    print(cnt)