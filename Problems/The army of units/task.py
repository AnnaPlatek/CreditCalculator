army_number = int(input())
if army_number < 1:
    print("no army")
elif army_number < 10:
    print("few")
elif army_number < 50:
    print("pack")
elif army_number < 500:
    print("horde")
elif army_number < 1000:
    print("swarm")
else:
    print("legion")