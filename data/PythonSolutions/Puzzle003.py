# YouTube Video: https://www.youtube.com/watch?v=_1Wp4Bww8Rs
def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

s = "1"
n = 25
print ("1\t: 1")
for i in range(2,n+1):
    s = next_number(s)
    print(f'{i}\t: {s[0:10]} -> {s.count("1")}')