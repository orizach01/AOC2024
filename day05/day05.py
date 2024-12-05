def part1(path):
    with open(path) as f:
        text = f.read()
        
    rules, lists = text.split('\n\n')
    rules = [[int(n[0]), int(n[1])] for n in [r.split('|') for r in rules.split('\n')]]
    lists = [[int(x) for x in l.split(',')] for l in lists.split('\n')]

    res = 0
    
    for l in lists:
        good = True
        for i in range(len(l) - 1):
            for j in range(i+1, len(l)):
                if not [l[i], l[j]] in rules:
                    good = False
        if good:
            res += l[len(l)//2]
            
    return res
        
        
def find_first(rules, l):
    good_rules = [r[1] for r in rules if r[0] in l and r[1] in l]
    for num in l:
        if num not in good_rules:
            return num
                
def part2(path):
    with open(path) as f:
        text = f.read()
        
    rules, lists = text.split('\n\n')
    rules = [[int(n[0]), int(n[1])] for n in [r.split('|') for r in rules.split('\n')]]
    lists = [[int(x) for x in l.split(',')] for l in lists.split('\n')]
    
    res = 0
    
    for l in lists:
        new_l = []
        while len(new_l) != len(l):
            new_l.append(find_first(rules, [n for n in l if n not in new_l]))
        if new_l != l:
            res += new_l[len(new_l)//2]

    return res
     

def main():
    assert (res:=part1('test.txt')) == 143, f"part1 res is {res}, need 143"
    print('part1', part1('input.txt'))
    
    assert (res:=part2('test.txt')) == 123, f"part2 res is {res}, need 123"
    print('part2', part2('input.txt'))


if __name__ == '__main__':
    main()
