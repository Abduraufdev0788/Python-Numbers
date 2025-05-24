from  num2words import num2words
narx = (input("narxlarni vergul bilan ajratib kiriting: "))
a = narx.split(",")
b = [float(i) for i in a]
c = sum(b)
d = num2words(c)
e = num2words(c, lang = "ru")
print("Jami narx: ", round(c, 1))
print("jami summa: ", d,"; ",e)
