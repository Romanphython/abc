###################################################
n_of_r = int(input("Enter the number of rows: "))
r = 1
while(r <= n_of_r):
    d = "." * (n_of_r - r)
    s = "*" * r
    print(d + s)
    r += 1