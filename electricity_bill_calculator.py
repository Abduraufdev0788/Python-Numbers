from num2words import num2words
start = float(input("oyning boshidagi qiymatni kiriting (kWh): "))
end = float(input("oyning oxiridagi qiymatni kiriting (kWh): "))
free = (end - start) * 0.45
a = num2words(round(free, 2),)
b = num2words(round(free, 2), lang='ru')
print(f"Elektr energiyasi uchun to'lov: {free:.2f} $\n {a} dollar\n {b} dоллар")