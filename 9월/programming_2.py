def solution(n):
    answer = []
    
    list_map = [[0]*n for _ in range(n)]
    count = 1
    l_count = n
    direction = 1
    h = 0
    w = 0


    for _ in range(n):
        if direction == 1:
            for _ in range(l_count) : 
                list_map[h][w] = count
                count += 1
                h += 1
            direction = 2
            l_count -= 1
            h -= 1
            w += 1

        elif direction == 2:
            for _ in range(l_count) :
                list_map[h][w] = count
                count += 1
                w += 1
            direction = 3
            l_count -= 1
            h -= 1
            w -= 2

        elif direction == 3:
            for _ in range(l_count) :
                list_map[h][w] = count
                count += 1
                w -= 1
                h -= 1
            direction = 1
            l_count -= 1
            h += 2
            w += 1
            
            
    for i in range(n):
        for j in range(i+1):
            answer.append(list_map[i][j])

    return answer


if __name__ == "__main__":

    print(solution(6))