numbers = list(map(int, input().split()))

avging = sum(numbers) / len(numbers)

diff_avg = []
for i in range(len(numbers)):
    diff = abs(number[i] - avging)
    diff_avg.append(diff)

print(*diff_avg, sep = ' ')

# ******************************
# Make your Code
# ******************************


# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
