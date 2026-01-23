def stringCount(len):
    count = 0
    for i in len:
        count = count+1
    return count

fra = str(input("dame una frase y te diré cuantos caracteres tiene: "))
print(stringCount(fra))