from fractions import Fraction
U1b1n_n2 = Fraction(0)
U1b1n_n1 = Fraction(1)

V1b1n_n1 = Fraction(2)/Fraction(3)
W2b_n1 = Fraction(1)/Fraction(3)
D1 = Fraction(1)
D2=Fraction(1)
S1 = Fraction(0)
S2=Fraction(0)

for i in range(10):
    U1b1n_n = U1b1n_n1/2 + U1b1n_n2/4
    U2n = U1b1n_n1/4
    U1b1n_n2 = U1b1n_n1
    U1b1n_n1 = U1b1n_n
    # print("1b1n",U1b1n_n) 
    # print("2n",U2n) 

    V1b1n_n = (V1b1n_n1+W2b_n1)*2/3
    W2b_n = V1b1n_n1/6+W2b_n1/3
    W2n_n = V1b1n_n1/6
    V1b1n_n1 = V1b1n_n
    W2b_n1 = W2b_n

    # print("V1b1n",V1b1n_n) 
    # print("V2b",W2b_n) 
    #print("V2n",W2n_n) 
    p1 = U2n*D1
    D1 -= W2n_n
    D2 -= U2n
    p2 = W2n_n*D2
    S1 += p1
    S2 += p2
    print(p2,float(S2))
    #print(float(p1),float(p2))
    #print(float(S1),float(S2),S1+S2)
    #print(Fraction(float(S1)))
    #print("----")
print(float(S1),float(S2),float(S1+S2))
print(Fraction(6784922394)/Fraction(10000000000-1))
print(Fraction(3215077605)/Fraction(10000000000-1))

print(float(Fraction(6784922394)/Fraction(10000000000-1)))