def calc_sum(input_list):
    sum = 0
    for i in input_list:
        sum += int(i)
    return sum

def get_sums(lines):
    sum = 0
    allSums = []
    for line in lines:
        line = line.strip()
        if line == "":
            allSums.append(sum)
            sum = 0
        else:
            sum += int(line)
    return allSums

with open("elves.txt") as file:
    allSums = get_sums(file)
    greatestSum = max(allSums)
    threeGreatestSums = calc_sum(sorted(allSums, reverse=True)[:3])

    print("All sums: " + str(allSums))
    print("Greatest sum: " + str(greatestSum))
    print("Three greatest sums: " + str(threeGreatestSums))

file.close()
