text = "I completely agree with you"
split_text = text.split()
counter = lambda split_text: len(split_text)
xd = list(map(counter, split_text))
print(xd)