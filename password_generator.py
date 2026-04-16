import random
print("==== Welcome to Password Maker ====\n")
print("1 -> System generate password")
print("2 -> Make password using your own word")
opt = int(input("\nEnter option: "))
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "0123456789"
c = "!@#$%&*?"
mix = ""
l = input("Need letters? (yes/no): ")
n = input("Need numbers? (yes/no): ")
s = input("Need symbols? (yes/no): ")
if l == "yes":
    mix = mix + a
if n == "yes":
    mix = mix + b
if s == "yes":
    mix = mix + c
if mix == "":
    print("You didn't choose anything")
else:
    final = ""
    if opt == 1:
        size = int(input("Enter length: "))
        i = 0
        while i < size:
            pick = random.choice(mix)
            final = final + pick
            i = i + 1
        print("\nGenerated Password:", final)
    elif opt == 2:
        base = input("Enter your word: ")
        extra = int(input("How many extra chars you want: "))
        final = base
        i = 0
        while i < extra:
            final = final + random.choice(mix)
            i = i + 1
        print("\nYour Modified Password:", final)
    else:
        print("Wrong option")
    if final != "":
        length = len(final)
        count_num = 0
        count_sym = 0
        for ch in final:
            if ch in b:
                count_num = count_num + 1
            if ch in c:
                count_sym = count_sym + 1
        if length > 10 and count_num > 0 and count_sym > 0:
            print("Strength: Strong")
        elif length > 6:
            print("Strength: Medium")
        else:
            print("Strength: Weak")