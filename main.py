text = input("Enter a string: ")

if len(text) > 10:
    print("Resultado:", text[:10] + "...")
else:
    print("Resultado:", text)
