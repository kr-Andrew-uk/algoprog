import csv

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1              
            return True
        return False

def calculate_min_cable_length(filename):
    edges = []
    vertices = set()
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                u = row[0].strip()
                v = row[1].strip()
                weight = int(row[2].strip())
                
                edges.append((weight, u, v))
                vertices.add(u)
                vertices.add(v)
    except FileNotFoundError:
        print(f"Помилка: Файл {filename} не знайдено.")
        return None
        
    edges.sort()
    
    ds = DisjointSet(vertices)
    
    min_cable_length = 0
    edges_used = 0
    
    for weight, u, v in edges:
        if ds.union(u, v):
            min_cable_length += weight
            edges_used += 1
            
    if edges_used == len(vertices) - 1 and len(vertices) > 0:
        return min_cable_length
    else:
        return -1

if __name__ == "__main__":
    filename = 'communication_wells.csv'
    
    result = calculate_min_cable_length(filename)
    if result is not None:
        print(f"Результат: {result}")