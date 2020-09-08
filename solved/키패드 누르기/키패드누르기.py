def solution(numbers, hand):
    answer = []
    left = [3,0]
    right = [3,2]
    for number in numbers:
        if number == 0:
            number = 11
        if number%3 == 1:
            left = [number//3, 0]
            answer.append('L')
        elif number%3 == 0:
            right = [number//3-1, 2]
            answer.append('R')
        elif number%3 == 2:
            dist_left = abs(left[0]-number//3)+abs(left[1]-1)
            dist_right = abs(right[0]-number//3)+abs(right[1]-1)
            if dist_left > dist_right:
                right = [number//3, 1]
                answer.append('R')
            elif dist_right > dist_left:
                left = [number//3, 1]
                answer.append('L')
            else:
                answer.append(hand[0].upper())
                if hand[0].upper() == 'L':
                    left = [number//3,1]
                else:
                    right = [number//3,1]    
    return ''.join(answer)