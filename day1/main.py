input_file = "./day1/input.txt"


def part1(left, right):
    left.sort()
    right.sort()
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    return sum

def part2(left, right):
    sum = 0
    rightmap = {}
    for num in right:
        if (num in rightmap):
            rightmap[num] += 1
        else:
            rightmap[num] = 1
            
    for num in left:
        if num in rightmap:
            sum += (num * rightmap[num])
    return sum
        

with open(input_file, 'r') as f:
    lines = (line.strip() for line in f.readlines())
    left = []
    right = []
    for line in lines:
        split = line.split("   ")
        left.append(int(split[0]))
        right.append(int(split[1]))
    print(part1(left, right))
    print(part2(left, right))