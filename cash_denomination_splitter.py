from num2words import num2words
amount = int(input("Pul miqdorini kiriting ($): "))

k_50 = amount // 50
amount = amount % 50
print("$50 kupyuradan:", k_50, "ta")

k_10 = amount // 10
amount = amount % 10
print("$10 kupyuradan:", k_10, "ta")

k_5 = amount // 5
amount = amount % 5
print("$5 kupyuradan:", k_5, "ta")

k_1 = amount // 1
amount = amount % 1
print("$1 kupyuradan:", k_1, "ta")

a = num2words(k_50*50 + k_10*10 + k_5*5 + k_1*1)
b = num2words(k_50*50 + k_10*10 + k_5*5 + k_1*1, lang = "ru")

print( "Umumiy summa: ",a, ",", b)


