n = int(input())
dict_str = input().strip()
pattern = input().strip()
dict_str = dict_str.replace("{", "").replace("}", "")
words = dict_str.split(",")
matches = []
for word in words:
    word = word.strip()
    abbr = ""
    for ch in word:
        if ch.isupper():
            abbr += ch
    if abbr.startswith(pattern):
        matches.append((abbr, word))
if len(matches) == 0:
    print("No match found")
else:
    matches.sort(key=lambda x: (x[0], x[1]))
    for abbr, word in matches:
        print(word)
