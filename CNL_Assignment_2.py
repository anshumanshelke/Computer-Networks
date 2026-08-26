import math

# Input 4-bit binary code
binary = [0] * 4

print("Enter 4 bits binary code:")

for i in range(4):
    bit = int(input(f"Enter bit {i + 1} : "))

    if bit != 0 and bit != 1:
        print("Invalid input: Code must only contain 0 and 1")
        exit()

    binary[i] = bit

print("Your binary code is:", end=" ")

for bit in binary:
    print(bit, end="")

print()

# Calculate number of parity bits
m = 4
r = 0

while True:
    if 2 ** r >= m + r + 1:
        break
    r += 1

print("Number of parity bits r:", r)

# Total number of bits
totalBits = m + r
finalBinary = [0] * totalBits

# Place parity bits at positions 1, 2, 4...
k = 0

for i in range(totalBits):
    if k >= r:
        break

    position = 2 ** k

    # Positions are counted from the right
    finalBinary[totalBits - position] = 0
    k += 1

# Place data bits
binaryIndex = 0

for i in range(totalBits, 0, -1):

    arrayIndex = totalBits - i

    if i != 1 and i != 2 and i != 4:
        finalBinary[arrayIndex] = binary[binaryIndex]
        binaryIndex += 1

print("Your binary code is with parity bits set to 0:", end=" ")

for bit in finalBinary:
    print(bit, end="")

print()

# Calculate parity bits
for parityIndex in range(r):

    parityPosition = 2 ** parityIndex
    parity = 0

    for position in range(1, totalBits + 1):

        if (position & parityPosition) != 0:

            arrayIndex = totalBits - position

            parity = parity ^ finalBinary[arrayIndex]

    finalBinary[totalBits - parityPosition] = parity

print("Final signal:", end=" ")

for bit in finalBinary:
    print(bit, end="")

print()
print()

# ---------------- RECEIVER ----------------

print("Enter received codeword:", end=" ")
received = input()

if len(received) != totalBits:
    print(f"Invalid codeword! Enter exactly {totalBits} bits.")
    exit()

receivedBinary = [0] * totalBits

for i in range(totalBits):

    bit = received[i]

    if bit != '0' and bit != '1':
        print("Invalid input: Code must only contain 0 and 1")
        exit()

    receivedBinary[i] = int(bit)

errorPosition = 0

# Check parity bits
for parityIndex in range(r):

    parityPosition = 2 ** parityIndex
    parity = 0

    for position in range(1, totalBits + 1):

        if (position & parityPosition) != 0:

            arrayIndex = totalBits - position

            parity = parity ^ receivedBinary[arrayIndex]

    if parity != 0:
        errorPosition += parityPosition

print()
print("----- RECEIVER -----")

if errorPosition == 0:

    print("No error detected.")

else:

    print("Error detected at bit position:",
          errorPosition,
          "from the right")

    errorArrayIndex = totalBits - errorPosition

    # Correct the error
    receivedBinary[errorArrayIndex] = receivedBinary[errorArrayIndex] ^ 1

    print("Corrected Codeword:", end=" ")

    for bit in receivedBinary:
        print(bit, end="")

    print()

# Recover original data bits
print("Recovered Data Bits:", end=" ")

for position in range(totalBits, 0, -1):

    if position != 1 and position != 2 and position != 4:

        arrayIndex = totalBits - position

        print(receivedBinary[arrayIndex], end="")

print()
