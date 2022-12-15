def get_sum(input_list):
    sum = 0
    for i in input_list:
        sum += int(i)
    return sum

def get_Input():
    input_list = []
    maxValue = 0
    while True:
        line = input()
        if line == "" or line == "\n":
            maxValue = max(maxValue, get_sum(input_list))
            input_list = []
            continue
        elif line == "!":
            return maxValue
        else:
            input_list.append(line)

# input ! to exit
print(get_Input())
