N = 4

def prefersCurrentPartner(preferences, woman, current_man, new_man):
    """
    Проверяет, предпочитает ли женщина своего текущего партнёра новому мужчине.
    """
    for preference in preferences[woman]:
        if preference == current_man:
            return True
        if preference == new_man:
            return False
    return False

def findStablePairs(preferences):
    """
    Алгоритм для нахождения стабильных паросочетаний.
    """
    engagements = [-1] * N  # Список пар, где индекс — женщина, значение — мужчина
    free_men = list(range(N))  # Список свободных мужчин

    # Пока есть свободные мужчины
    while free_men:
        man = free_men.pop(0)  # Берём первого свободного мужчину
        for woman in preferences[man]:
            current_partner = engagements[woman - N]
            if current_partner == -1:  # Если женщина свободна
                engagements[woman - N] = man
                break
            else:  # Женщина уже помолвлена, проверяем предпочтения
                if not prefersCurrentPartner(preferences, woman, current_partner, man):
                    engagements[woman - N] = man
                    free_men.append(current_partner)
                    break

    # Печать результатов
    print("Женщина", "Мужчина")
    for woman, man in enumerate(engagements):
        print(woman + N, "\t", man)

# Списки предпочтений: сначала для мужчин, затем для женщин
preferences = [[7, 5, 6, 4], [5, 4, 6, 7],
               [4, 5, 6, 7], [4, 5, 6, 7],
               [0, 1, 2, 3], [0, 1, 2, 3],
               [0, 1, 2, 3], [0, 1, 2, 3]]

print("Стабильные пары:")
findStablePairs(preferences)
