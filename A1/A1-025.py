books = {'A':'ace','J':'jack','Q':'queen','K':'king','D':'diamonds','H':'hearts','S':'spades','C':'clubs'}
text = input()
text = text.upper()

if text[0].isdigit():
    if len(text) == 3:
        print(f"10 of {books[text[-1]]}")
    else:
        print(f"{text[0]} of {books[text[-1]]}")
else:
    print(f"{books[text[0]]} of {books[text[-1]]}")