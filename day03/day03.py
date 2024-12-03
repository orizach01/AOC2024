import re

def part1(path):
    with open(path) as f:
        text = f.read()
    
    matches: list[str] = re.findall(r'mul\(\d{1,3},\d{1,3}\)', text)

    sum = 0
    for match in matches:
        nums = [int(n) for n in match[4:-1].split(',')]
        sum += nums[0] * nums[1]

    return sum


def part2(path):
    with open(path) as f:
        text = f.read()
    
    matches: list[str] = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", text)

    sum = 0
    enabled = True
    for match in matches:
        if 'mul' in match and enabled:
            nums = [int(n) for n in match[4:-1].split(',')]
            sum += nums[0] * nums[1]
            continue

        if "don't" in match:
            enabled = False
            continue

        if 'do' in match:
            enabled = True
            continue
        

    return sum

def main():
    assert (res:=part1('test.txt')) == 161, f"part1 res is {res}, need 161"
    assert (res:=part2('test2.txt')) == 48, f"part2 res is {res}, need 48"
    print('part1', part1('input.txt'))
    print('part2', part2('input.txt'))


if __name__ == '__main__':
    main()
