dict = {}
nums = int(raw_input())
for i in range(nums):
    tel1, tel2 = map(int, raw_input().split())
    if tel1 in dict:
        dict[tel1] += 1
    else:
        dict[tel1] = 1
    if tel2 in dict:
        dict[tel2] += 1
    else:
        dict[tel2] = 1


MaxTimes = 1
theone = None
perNum = 0
for key in dict:
    temp = dict[key]
    if temp > MaxTimes:
        MaxTimes = temp
        theone = key
        perNum = 1
    elif temp == MaxTimes:
        perNum += 1
        if key < theone:
            theone = key

if perNum == 1:
    print theone, MaxTimes
else:
    print theone, MaxTimes, perNum
