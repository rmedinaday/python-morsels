number = 13242341244

chars = number.__str__()
count = {}
for i in range(len(chars)):
    if chars[i] in count.keys():
        count[chars[i]] += 1
    else:
        count[chars[i]] = 1

print (count)



