class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Каждый элемент изначально свой собственный родитель
        self.rank = [0] * n           # Ранг каждого дерева изначально равен 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Рекурсивное обновление родителя
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    n = 8  # Количество элементов
    uf = UnionFind(n)

    # Примеры операций
    uf.union(0, 1)
    uf.union(1, 4)
    uf.union(5, 6)

    print(f"Принадлежат ли 0 и 4 одному множеству? {'Да, принадлежат.' if uf.connected(0, 4) else 'Нет, не принадлежат.'}")
    print(f"Принадлежат ли 3 и 6 одному множеству? {'Да, принадлежат.' if uf.connected(3, 6) else 'Нет, не принадлежат.'}")

    uf.union(4, 5)
    print(f"Принадлежат ли 0 и 6 одному множеству после объединения? {'Да, теперь они в одном множестве.' if uf.connected(0, 6) else 'Нет, они всё ещё в разных множествах.'}")

    uf.union(2, 3)
    print(f"Связаны ли 2 и 3? {'Да, они принадлежат одному множеству.' if uf.connected(2, 3) else 'Нет, они принадлежат разным множествам.'}")
