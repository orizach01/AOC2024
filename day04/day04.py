directions =  [(0, 1), 
               (1, 0), 
               (1, 1), 
               (0, -1), 
               (-1, 0), 
               (-1, -1), 
               (-1, 1), 
               (1, -1)]

need = {
    'X': 'M',
    'M': 'A',
    'A': 'S'
}

def part1(path):
    with open(path) as f:
        letters = [[c for c in l if c != '\n'] for l in f.readlines()]
        
    max_x = len(letters[0])
    max_y = len(letters)
    
    res = 0

    for y, line in enumerate(letters):
        for x, letter in enumerate(line):
            if letter != 'X':
                continue
            
            for dir_x, dir_y in directions:
                found = False
                new_x, new_y = x, y
                next_needed = need['X']
                while not found:
                    new_x, new_y = new_x + dir_x, new_y + dir_y
                
                    if new_x == max_x or new_x == -1 or new_y == max_y or new_y == -1:
                        break
                    
                    if letters[new_y][new_x] != next_needed:
                        break
                    
                    if letters[new_y][new_x] == 'S':
                        found = True
                        break
                    
                    next_needed = need[letters[new_y][new_x]]
                if found:
                    res += 1
                    
    return res
                
def part2(path):
    with open(path) as f:
        letters = [[c for c in l if c != '\n'] for l in f.readlines()]
            
    res = 0
    
    for y in range(0, len(letters) - 2):
        for x in range(0, len(letters[0]) - 2):
            if letters[y+1][x+1] != 'A':
                continue
            
            if (letters[y][x], letters[y+2][x+2]) in [('M', 'S'), ('S', 'M')] and \
               (letters[y+2][x], letters[y][x+2]) in [('M', 'S'), ('S', 'M')]:
                   res += 1
                   
    return res
     

def main():
    assert (res:=part1('test.txt')) == 18, f"part1 res is {res}, need 18"
    assert (res:=part2('test.txt')) == 9, f"part2 res is {res}, need 9"
    print('part1', part1('input.txt'))
    print('part2', part2('input.txt'))


if __name__ == '__main__':
    main()
