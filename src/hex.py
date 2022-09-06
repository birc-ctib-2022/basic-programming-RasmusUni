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
            y.append(hex(ord(a)))
  
        encoding="".join(y)
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        y = x.split("0x")
        list4=[]

        for a in y[1:]:
            a=int(a, base=16)
            list4.append(chr(a))
        
        decoding="".join(list4)

        print(decoding)
