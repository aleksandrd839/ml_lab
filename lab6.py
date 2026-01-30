def vowel_percentage(slogan: str) -> str:
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    
    v = 0
    for x in slogan:
        print(x, type(x))
        if x in vowels:
            v += 1
    
    return str(round(v / len(slogan))) + '%'


slogan = input()

percentage = vowel_percentage(slogan)

print(percentage)