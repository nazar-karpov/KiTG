N = 4

def prefersCurrentPartner(preferences, woman, current_man, new_man):
    for preference in preferences[woman]:
        if preference == current_man:
            return True
        if preference == new_man:
            return False
    return False

def findStablePairs(preferences):
  
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

    print("Женщина", "Мужчина")
    for woman, man in enumerate(engagements):
        print(woman + N, "\t", man)

preferences = [
    [6, 7, 4, 5],  # Мужчина 0
    [7, 6, 5, 4],  # Мужчина 1
    [5, 4, 7, 6],  # Мужчина 2
    [4, 7, 5, 6],  # Мужчина 3
    [0, 2, 1, 3],  # Женщина 4
    [1, 0, 3, 2],  # Женщина 5
    [3, 1, 0, 2],  # Женщина 6
    [2, 3, 0, 1]   # Женщина 7
]

print("Стабильные пары:")
findStablePairs(preferences)
