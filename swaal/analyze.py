import json

with open("output.json") as f:
    packets = json.load(f)

letters: dict[int, str] = {}
column = 0
for packet in packets:
    value = int(packet, base=16)

    if value == 0:
        print(" ", end="")
        if column not in letters:
            letters[column] = " "
    elif value == 10: # LF
        print()
        column = 0
    else:
        print(chr(value), end="")
        letters[column] = chr(value)

    column += 1

print()

print("".join(letters.values()))
