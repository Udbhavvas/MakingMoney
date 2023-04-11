
y = []
# Read newstocks.txt
with open("newstocks.txt", "r") as f:
    x = f.read().splitlines()
    # print(x)

    x[0] = "MMM"

    x.sort()
    # print(x)

    y = x
with open("newstocks1.txt", "w") as f:
    for line in y:
        f.write(line)
        f.write("\n")
