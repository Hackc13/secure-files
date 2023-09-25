regulation = str(input("Regulation no Y20: "))
branch = str(input("Enter your branch: "))
r = int(input("Enter range: "))

with open("redg.txt", "w") as file:
    for i in range(401, r):
        file.write(regulation + branch + str(i) + "\n")

print("Output has been written to 'redg.txt'.")
