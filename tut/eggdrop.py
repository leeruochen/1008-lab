def eggdroprec(eggs, floors):
    if floors == 0 or floors == 1:
        return floors

    if eggs == 1:
        return floors
    
    min = 32767

    for k in range(1, floors + 1):
        drops = 1 + max(eggdroprec(eggs - 1, k - 1), eggdroprec(eggs, floors - k))
        if drops < min:
            min = drops

    return min

print(eggdroprec(2, 3))