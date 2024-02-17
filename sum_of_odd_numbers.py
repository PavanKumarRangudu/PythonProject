# Print the sum of all the odd numbers.
number = int(input("Enter a number:\n"))
total =0
for n in range(1, number+1, 2):
  total += n
print(total)

total =0
for n in range(1, number+1):
  if n % 2 != 0:
    total += n
print(total)

print(sum(range(1, number+1, 2)))