#input consigliato input1=12 input2=6.5
input1=int(input("Inserisci un numero intero:"))
input2=float(input("Inserisci un numero con la virgola:"))
print("input1/input2:",(input1/input2))
print("input1//input2:",(input1//input2))
print("input1+input2:",(input1+input2))
print("input1-input2:",(input1-input2))
print("input1*input2:",(input1*input2))
print("input1^2:",(input1**2))
print("input1%input2:",(input1%input2))

if input1==input2:
    print("I due numeri sono uguali")
elif input1>input2:
    print("Il primo numero è maggiore del secondo")
else:
    print("Il secondo numero è maggiore del primo")

str_input1=str(input1)
print("Il primo numero come stringa è "+str_input1)
flt_input1=float(input1)
print("Il primo numero come float è ",flt_input1)
int_input2=int(input2)
print("Il secondo numero come int è ",int_input2)