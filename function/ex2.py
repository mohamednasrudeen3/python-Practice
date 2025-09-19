
# *args
def total(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(total(5,6,7,9))


# **kwargs

def printAddress(**kwags):
    for key,val in kwags.items():
        print(f"{key} : {val}")


printAddress(doorNo=27,street_Name="Thiyagu Nagar",city="Cuddalore")