
def is_sorted(massiv):
    check = massiv.copy()
    check.sort()
    if check == massiv:
        return True
    else:
        return False


def max_row(massiv):
    sum = 1
    max = -1
    for i in range(len(massiv) - 1):
        if massiv[i] <= massiv[i + 1]:
            sum += 1
        else:
            if sum > max:
                max = sum
    if max == -1:
        max = sum
    return max

def solution(massiv):
    if is_sorted(massiv):
        return(len(massiv))
    if len(massiv) % 2 != 0:
        half = len(massiv) // 2
        first = massiv[:half + 1].copy()
        second = massiv[half:].copy()
    else:
        half = len(massiv) // 2
        first = massiv[:half].copy()
        second = massiv[half:].copy()

    if max_row(first) > max_row(second):
        return solution(first)
    else:
        return solution(second)



number = input()
massiv = list(map(int, input().split()))
print(solution(massiv))



