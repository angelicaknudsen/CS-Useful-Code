# A regular expression or regex for short is a way of searching text
# for a pattern. Most people look at regex and get scared away, and
# it does look confusing at first. But it's also an incredibly useful
# tool to add to your programming arsenal.

# First you need to import the 're' library:
import re

# In it's most basic form, you can use regex to search for words in
# some text:
pattern = "flag"
text = "The flag is: this is a fake flag: bajhdasdohaudsnasdaasd"

if re.findall(pattern, text):
    print("Found match!")

# Just telling you if something is there is not that useful though.
# Ideally we want to extract some information out of the text you are
# searching.

pattern = "flag: (.*)"
data = re.findall(pattern, text)
print(data[0])

# In this case, we managed to extract the flag from the text provided.
# Let's look more closely at how this happened.

# The key is the pattern: flag: (.*).
# First we're looking for any text that starts with Flag:
# The brackets surround the bit we want to extract. We know the flag
# we want to get comes after flag: so the brackets are after flag:.
# The . inside the brackets means match any character.
# The * means any number of times.
# So put it together and you're extracting any series of characters
# after the word flag: .

# What re.findall returns is an array. That's because it find all
# possible matches, so if there was more than one match, it would
# put them in the other positions in the array.
# For example data[1] for the second match, data[2] for the third
# match and so on...

# Regex is a whole language on it's own, but that is the basics.
# You can find out how to do more things with it at:
# https://regexone.com/

# Jelly's input: so apparently you can use triple quotations for multiline text in variables... nice
html = """
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>
"""

# CHALLENGE 1: Write a regex search that extracts all the classes from
#             the divs and saves them into an array.

#regex my love
wow = "<div class='(.*)'>Hello</div>"
listWow = re.findall(wow, html)

# CHALLENGE 2: Write a loop that goes through the array from
#              CHALLENGE 1 and prints the contents.

for x in listWow:
  print(x)