#Wheresoever you go, go with all your heart
#go thru every cahracter of each word, add letters to words, if all word is alpha save it if first letter of the word
#is h print the word in caps.

print("provide the quote you would like to iterate via this wonderful app: ")
quote = input()
var = quote.lower()
for word in var.split():
    if word[0] >= "h":
        print(word.capitalize())
    else:
        continue

'''
just because test program wanted to do the same stuff, with a bit too much unnecesary steps, 
I think I have made it a bit more simple
and straight way to get the same results.
'''