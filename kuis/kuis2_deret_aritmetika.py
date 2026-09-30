print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi n harus lebih dari 0
while n <= 0:
    print("Banyak suku (n) harus lebih besar dari 0.")
    n = int(input("Banyak suku n: "))

total = 0
print("\nSuku-suku deret:")
for i in range(1, n + 1):
    suku = a + (i - 1) * d
    print(f"Suku ke-{i} = {suku}")
    total += suku

print(f"\nJumlah total deret = {total}")