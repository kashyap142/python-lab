def solve(email):
    vowel = "aeiou"

    cnt_vowel = 0
    cnt_consonant = 0
    cnt_digits = 0
    cnt_space = 0

    for ch in email:
        if ch.isalpha():
            ch = ch.lower()
            if ch in vowel:
                cnt_vowel += 1
            else:
                cnt_consonant += 1
        elif ch == ' ':
            cnt_space += 1
        elif ch.isdigit():
            cnt_digits += 1

    print(f"Vowels: {cnt_vowel},\nConsonant: {cnt_consonant},\nSpace: {cnt_space},\nDigits: {cnt_digits}")


if __name__ == "__main__":
    email = input("Enter email: ")

    solve(email)
