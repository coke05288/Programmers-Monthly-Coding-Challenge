def solution(a):
    answer = 0
    cehck_list = a

    mid = min(cehck_list)

    idx = cehck_list.index(mid)

    left = min(cehck_list[:idx])

    idx_l = cehck_list.index(left)

    right = min(cehck_list[idx+1:])

    idx_r = cehck_list.index(right)

    temp_list = cehck_list[:idx_l+1] + [mid] + cehck_list[idx_r:]

    answer = len(temp_list)

    return answer


if __name__ == "__main__":

    print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))