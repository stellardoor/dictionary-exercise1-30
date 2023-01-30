"""Count words in file."""

# test = str(input(""))
test = 'test.txt'
def word_count(text_file):
    text_input = open(text_file)
    # text_input = text_input.split(" ")
    word_count = { }
    
    for line in text_input:
        line = line.rstrip().lower()
        words = line.split()
        for word in words:
            if word[-1] in "!?,.":
                word = word[:-1]
            if word in word_count:
                word_count[word] = word_count[word] + 1 
            else:
                word_count[word] = 1

    return word_count

print(word_count(test))
        
# put your code here.

