text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
index = 0

# Count vowels in the text using a while loop
while index < len(text):
    if text[index] in vowels:
        vowel_count += 1
    index += 1
