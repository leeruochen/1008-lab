def palindrome(word, i, j):
    if i >= j: # base case, reached the middle
        return True
    if word[i] != word[j]: # found a mismatch, not a palindrome
        return False
    
    # recursive case, check the next pair of characters as it matches
    return palindrome(word, i+1, j-1)
    
def wordFormat(word):
    word = word.lower().replace(" ", "")
    word = ''.join(char for char in word if char.isalnum()) # remove punctuation
    return word

def main():
    word = "Madam, I\'m Adam"
    word = wordFormat(word)
    i = 0
    j = len(word) - 1
    print(palindrome(word, i, j))

if __name__ == "__main__":
    main()