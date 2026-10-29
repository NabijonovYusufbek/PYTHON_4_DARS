def parol_yetarlimi(parol):
    if len(parol) >= 8:
        return True
    else:
        return False

print(parol_yetarlimi("Python123"))