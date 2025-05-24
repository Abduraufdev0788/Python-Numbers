from num2words import num2words
xarajat = input("Xarajatlarni vergul bilan ajratib kiriting: ")
xarajatlar = xarajat.split(",")
xarajatlar = [float(i) for i in xarajatlar]
if len(xarajatlar) == 7:
    haftalik = sum(xarajatlar)/7
    a = num2words(round(haftalik, 2))
    b = num2words(round(haftalik), lang="ru")
    print("O'rtacha xarajat: ", round(haftalik, 2))
    print("O'rtacha xarajat: ", a, " dollar ; ", b)
else:
    print("Iltimos, 7 ta xarajat kiriting.")    

