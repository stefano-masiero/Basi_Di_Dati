# consiglio input1=ciao input2=robegano
STR="ci"
input1=input("Inserisci la stringa 1:")
input2=input("Inserisci la stringa 2:")
print("La lunghezza della stringa è:",len(input1))
print("Il primo carattere della stringa è:",input1[0])
print("La stringa maiuscola è:",input1.upper())
print("La stringa minuscola è:",input1.lower())
print("La stringa contiene ci:",STR in input1)
if input1==input2:
    print("Le due stringhe sono uguali")
elif input1<input2:
    print("La stringa 1 viene prima della stringa 2")
else:
    print("La stringa 2 viene prima della stringa 1")
print("La stringa inizia con ci:",input1.startswith("ci"))
print("L'indice dove compare la prima c nella prima stringa è",input1.find("c"))
input1=input1.replace("ciao","mondo")
print("La stringa 1 è:",input1)
print("Le occorrenze di o nella prima stringa sono:",input1.count("o"))