#19.04.2024
def cagr_berechnung(AK=100, EK=700, t=30):
    AK_abs = abs(AK)
    t_abs = abs(t)
    CAGR = ((EK/AK_abs)**(1/t_abs))-1
    return CAGR
    #print(CAGR)

cagr1 = cagr_berechnung()
cagr2 = cagr_berechnung(120, 840, 30)

print("1.: ", cagr1, "\n2.: ", cagr2, sep='')

#cagr_berechnung()
#cagr_berechnung(120, 840, 30)

AK = 120
t = 30
cagr = cagr_berechnung(100, 700, 30)
EK = AK * (1 + cagr)**t
print(EK)