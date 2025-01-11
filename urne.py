from fractions import Fraction
U2b = Fraction(1)
U1b1n = Fraction(0)
Somme=Fraction(0)
Perim = Fraction(1)

BK_U2b = Fraction(1)
BK_U1b1n = Fraction(0)
BK_Somme=Fraction(0)

for i in range(10):
    if U2b:
        new_U1b1n = U2b
        #print(new_U1b1n)
        U2b = Fraction(0)
    if U1b1n:
        new_U1b1n += U1b1n / 2
        new_U2n = U1b1n / 4
        new_U2b = U1b1n / 4
        new_U2n *= Perim
        Perim -= new_U2n
        Somme+=new_U2n
        print(i+1,float(Somme))

        U2b = new_U2b
    U1b1n = new_U1b1n
    new_U1b1n = Fraction(0)
    #print("U1b1n",U1b1n)

    if BK_U2b:
        BK_new_U1b1n = BK_U2b*2/3
        BK_new_U2b = BK_U2b/3
        #print(new_U1b1n)
        BK_U2b = Fraction(0)
    if BK_U1b1n:
        BK_new_U1b1n += BK_U1b1n * 4 /6
        BK_new_U2n = BK_U1b1n / 6
        BK_new_U2b += BK_U1b1n / 6
        BK_new_U2n *= Perim
        Perim -= BK_new_U2n
        #print(i+1,BK_new_U2n)
        BK_Somme+=BK_new_U2n
        print(i+1,float(BK_Somme)," -- BK")
        print(i+1,BK_Somme+Somme," --SOMME")

    BK_U2b = BK_new_U2b
    BK_U1b1n = BK_new_U1b1n
    BK_new_U1b1n = Fraction(0)
    BK_new_U2b = Fraction(0)
#print("--",Fraction(0.678466297985))
print(Somme,BK_Somme)