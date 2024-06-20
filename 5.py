def calc_stat(listened):
    N = len(listened)
    M = sum(listened) // 60  # целое количество минут
    return f'Вы прослушали {N} песен общей продолжительностью {M} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))