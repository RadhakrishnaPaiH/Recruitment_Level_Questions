#Method-1(Simple,Less efficient) TC-O(n) SC-O(n)
my_set = {1, 2, 3, 5}
your_set = set()

for i in range(1, 6):
    your_set.add(i)

missing_element = your_set - my_set
print(missing_element)

#Method-2 XOR(Simple,Efficient) TC-O(n) SC-O(1)
missing = 0

for i in range(1, 6):
    missing ^= i

for num in [1, 2, 3, 5]:
    missing ^= num

print(missing)

#Method-3 SUM(Simple,Efficient) TC-O(n) SC-O(1)
n = 5
nums = [1, 2, 3, 5]

missing = n * (n + 1) // 2 - sum(nums)
print(missing)  # 4
