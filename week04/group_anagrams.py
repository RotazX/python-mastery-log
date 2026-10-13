from collections import defaultdict

def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for word in words:
        word_letters = tuple(sorted(word))
        anagrams[word_letters].append(word)
        # if word_letters not in anagrams.keys():
        #     anagrams[word_letters].append(word)
        # else:
        #     anagrams[word_letters].append(word)
    return [anagram for anagram in anagrams.values()]
    
if __name__ == "__main__":
    w = ["ab", "aab", "abb", "ba"]
    w1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    w2 = []
    print(group_anagrams(w))
    print(group_anagrams(w1))
    print(group_anagrams(w2))
