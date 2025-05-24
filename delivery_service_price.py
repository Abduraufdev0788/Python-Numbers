from num2words import num2words
masofa = float(input("masofanini kiriting kmda: "))
km_uchun =masofa * 0.80
jami = 5.00 + km_uchun
eng = num2words(round(jami,2))
ru = num2words(round(jami,2), lang='ru')
print(f"jami: {round(jami,2)}$, {eng} dollar ; {ru} dоллар")

