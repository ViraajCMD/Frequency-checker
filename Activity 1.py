print("Welcome to the frequency checker!")

my_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'codingal' : 1}

f = int(input("Please enter a value for which you would like to check the frequency: "))

res = 0

for key in my_dict:
    if my_dict[key] == f:
        res += 1


print(f"The frequency of {f} value in the dictionary is:\n{res}")