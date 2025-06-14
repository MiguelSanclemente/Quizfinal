import re

# Function to read the content of 'seguridad.txt' and store it in the global variable 'text'
def txt_reader():
    global text
    with open("seguridad.txt", "r", encoding="utf-8") as file:
        text = file.read()

# Call the function to read the file
txt_reader()       

# Find all sentences that are questions (both Spanish and English)
# The first group matches Spanish questions (¿...?), the second matches any sentence ending with '?'
result = re.findall(r"(\¿.+?\?)|(.+?\?)", text)

if result:
    print("the following questions will be found:")
    print(result)
else:
    print("No questions were found in the text.")

# Find all sentences that are exclamations (both Spanish and English)
# The first group matches Spanish exclamations (¡...!), the second matches any sentence ending with '!'
result = re.findall(r"(\¡.+?\!)|(.+?\!)", text)

if result:
    print("The following exclamations will be found:")
    print(result)
else:
    print("No exclamations were found in the text.")



# Define a regular expression pattern to match the specified abbreviations and acronyms.
# (?<!\w) and (?!\w) ensure that the match is not part of a longer word (word boundaries).
# The pattern includes both English and Spanish abbreviations, as well as acronyms like DDoS, SMS, and PC.

# Search for all occurrences of the abbreviations in the text, ignoring case sensitivity.
result = re.findall(r"(?<!\w)(Don’t|Don't|He’s|He's|Haven’t|Haven't|Mr\.|Mrs\.|No|És el|No lo he hecho|Señor|Señora|DDoS|SMS|PC)(?!\w)", text,
                     flags=re.IGNORECASE)


if result:
    print("The following abbreviations will be found:")
    print(result)

else:
    print("No abbreviations were found in the text.")