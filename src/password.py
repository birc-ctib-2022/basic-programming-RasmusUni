import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

hej=[0, 0, 0, 0, 0, 0]


if len(password) >= 6:
    hej[0]=1
    if len(password) <= 16:
        hej[1]=1
        for x in password:
            if x.isupper()==True:
                hej[2]=1
            elif x.islower()==True:
                hej[3]=1
            elif x.isnumeric()==True:
                hej[4]=1
            elif x in "$#@":
                hej[5]=1

if 0 not in hej:
    is_valid = True

print(is_valid)
