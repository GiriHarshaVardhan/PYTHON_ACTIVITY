''' Repeated Word and Phrase Detection: Process a paragraph,
 normalize letter case, count word occurrences using permitted string 
 and list operations, and identify repeated words and their positions. '''
text = "apple banana apple orange".split()
words_to_check = ["apple", "banana", "orange"]

for word in words_to_check:
    count = text.count(word)
    if count > 1:
        print("Repeated word:", word, "| Times:", count)