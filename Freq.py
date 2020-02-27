import sys


def alphaArr():
    # create a array list of the alphabeth
    arr = [None] * 26
    arr[:] = [chr(i + ord("a")) for i in range(26)]
    return arr


def letterfreq(text):
    # Count how often letters are in a text
    alpha = alphaArr()
    frequency = [0] * 26
    for i in text:
        if "a" <= i <= "z":
            index = alpha.index(i)
            frequency[index] += 1
    return frequency


def possiblecombos(text):
    # Het gebruik van meest voorkomende letters omvormen naar de meest gebruikte letters
    freq = letterfreq(text)
    pos = 0
    for i in range(len(freq)):
        counter = 0
        for j in range(len(freq)):
            if freq[i] == freq[j] and freq[i] != 0:
                counter += 1
        if counter > 1:
            pos += 1
    return pos


def decode(text, frequency):
    NLfreq = ["e", "n", "a", "t", "i", "r", "o", "d", "s", "l", "g", "v",
              "h", "k", "m", "u", "b", "p", "w", "j", "z", "c", "f", "x", "y", "q"]
    alphabet = alphaArr()
    counter = 0
    while max(frequency) != 0:
        # Get the index of most frequent number
        mostFreqLetter = max(frequency)
        # Get the letter corosponding to the most frequent
        letter = alphabet[frequency.index(mostFreqLetter)]
        # replace the most frequent letter with the most used letter in nl
        text = text.replace(letter, NLfreq[counter].upper())
        # set the frequency to 0 because we have used this letter
        frequency[frequency.index(mostFreqLetter)] = 0
        counter += 1
    return text


# main
# open file
bestand = open("text.txt")
text = bestand.read().lower()
bestand.close()

# get freqency table
alphabet = alphaArr()
numbers = (letterfreq(text))

# Print formatted frequency table
for i in range(26):
    print(alphabet[i], numbers[i])

print(possiblecombos(text))
print(decode(text, numbers))
