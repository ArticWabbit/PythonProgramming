def count_vowels(vowel):
    lc = vowel.lower()
    vowel_counts = {}
    for index in "aeiou":
        count = lc.count(index)
        vowel_counts[index] = count
    counts = vowel_counts.values()
    total = sum(counts)
    return print(total)


count_vowels("Prediction")
