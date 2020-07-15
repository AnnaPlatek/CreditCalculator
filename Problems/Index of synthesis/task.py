index_lang = float(input())
if index_lang < 2:
    print("Analytic")
elif index_lang > 3:
    print("Polysynthetic")
else:
    print("Synthetic")