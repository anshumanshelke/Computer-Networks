import math

# Input base IP address
ip = input("Enter base IP address (e.g., 192.168.10.0): ")

# Split IP into octets
o1, o2, o3, o4 = map(int, ip.split('.'))

# Input CIDR prefix
cidr = int(input("Enter CIDR prefix (e.g., 26 for /26): "))

# Validate CIDR
if cidr < 24 or cidr > 30:
    print("Error: This program currently supports Class C subnetting "
          "(CIDR 24 to 30).")
    exit()

# Calculate subnet information
hostBits = 32 - cidr
blockSize = 2 ** hostBits
numSubnets = 256 // blockSize
usableHosts = blockSize - 2
lastOctetMask = 256 - blockSize

print("\n--- General Subnet Information ---")
print("Calculated Subnet Mask :", f"255.255.255.{lastOctetMask}")
print("Total Usable Hosts     :", usableHosts, "per subnet")
print("Total Subnets Created  :", numSubnets)
print()

# Generate subnet information
for i in range(numSubnets):

    network = i * blockSize
    firstHost = network + 1
    lastHost = network + usableHosts
    broadcast = network + blockSize - 1

    print("=========================================")
    print(f"Subnet {i + 1}")
    print("=========================================")

    print(f"Network Address   : {o1}.{o2}.{o3}.{network}")
    print(f"First Host        : {o1}.{o2}.{o3}.{firstHost}")
    print(f"Last Host         : {o1}.{o2}.{o3}.{lastHost}")
    print(f"Broadcast Address : {o1}.{o2}.{o3}.{broadcast}")

    print("\nUsable IP Addresses:")

    for j in range(firstHost, lastHost + 1):
        print(f"  {o1}.{o2}.{o3}.{j}")

    print()
