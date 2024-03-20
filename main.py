import spellchecker

sc = spellchecker.SpellChecker()

while True:
    sc.printMenu()
    try:
        txtIn = input()
    except:
        raise ValueError
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        print("--------------------------------------\nUsing contains")
        sc.handleSentence(txtIn, "italian")
        print("--------------------------------------\nUsing Dichotomic search")
        sc.handleSentenceWithDichotomic(txtIn, "italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        print("--------------------------------------\nUsing contains")
        sc.handleSentence(txtIn, "english")
        print("--------------------------------------\nUsing Dichotomic search")
        sc.handleSentenceWithDichotomic(txtIn, "english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        print("--------------------------------------\nUsing contains")
        sc.handleSentence(txtIn, "spanish")
        print("--------------------------------------\nUsing Dichotomic search")
        sc.handleSentenceWithDichotomic(txtIn, "spanish")
        continue

    if int(txtIn) == 4:
        break
