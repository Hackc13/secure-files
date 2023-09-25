k = int(input("Enter year: "))
file_name = str(k) + ".txt"
with open(file_name, "w") as file:
    for i in range(1, 32):
        for j in range(1, 13):
            day = str(i).zfill(2)
            month = str(j).zfill(2)
            file.write(f"{day}{month}{k}\n")
print(f"Output saved to {file_name}")
