def solution(cards1, cards2, goal):
    i, j = 0, 0  # 각 카드 리스트에서 현재 확인할 위치

    for word in goal:
        # cards1에서 사용 가능한 경우
        if i < len(cards1) and cards1[i] == word:
            i += 1
        # cards2에서 사용 가능한 경우
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            return "No"  # 어느 카드에서도 현재 단어를 사용할 수 없으면 불가능

    return "Yes"