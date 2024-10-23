def minion_game(s: str) -> str:
    vowels = ["A", "E", "I", "O", "U"]
    consonants = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", 
                  "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    Kevin = 0
    Stuart = 0
    #Kevin
    for vowel in vowels:
        for i in range(len(s)):
            if s[i] == vowel:
                for j in range(i+1, len(s)+1):
                    Kevin = Kevin + 1
    #Stuart
    for consonant in consonants:
        for k in range(len(s)):
            if s[k] == consonant:
                for l in range(k+1, len(s)+1):
                    Stuart = Stuart + 1
    if Stuart > Kevin:
        eredmeny = f"Stuart {Stuart}"
    elif Kevin > Stuart:
        eredmeny = f"Kevin {Kevin}"
    elif Stuart == Kevin:
        eredmeny = "Draw"
    return eredmeny  
    pass
