import string

cases = int(input())

for i in range(cases):
    alphabet = string.ascii_lowercase
    st = str(input())

    for c in st.lower():
        if c in alphabet:
            alphabet = alphabet.replace(c, "")

    if alphabet == "":
        print("pangram")
    else:
        print("missing", alphabet)
