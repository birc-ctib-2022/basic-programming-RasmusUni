import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        y=[]
        for a in x:
            y.append(hex(a))

        z="".join(y)
        encoding=z
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        list3 = x.split("0x")
        list4=[]
        for a in list3:
            y=int(a, base=16)
            list4.append(chr(y))
        
        z="".join(list4)
        decoding=z

        print(decoding)
