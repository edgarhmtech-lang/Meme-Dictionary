word = input("Type a word you don't understand: ")
meme_dict = {
            "CRINGE": "Something exceptionally awkward or embarrassing",
            "LOL": "A common response to something funny",
            "GHOSTING": "Suddenly stopping all communication with someone without explanation",
            "STAN": "Being an extremely enthusiastic fan of something or someone",
            "FLEX": "Showing off something, usually achievements or possessions",
            }
word = word.upper()
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("The word you're looking for isn't in our dictionary, sorry 0_0")
