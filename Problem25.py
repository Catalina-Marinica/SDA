from problem import Problem
import random


class Problem25(Problem):

    def __init__(self):
        data = random.sample(range(100), random.randint(7, 10))

        statement = '1. Sa presupunem ca am vrea sa implementam un heap ternal(fiecare nod are 3 fii). \n'
        statement += '2. Introduceti elementele: ' + str(data) + ' intr-un max heap ternal si decapitati heap-ul. \n'

        super().__init__(statement, data)

    def solve(self):
        data = self.data
        solution = '3. Solutia problemei: \n'
        solution += '\t0.Vectorul este: ' + str(data) + '\n'

        def sift_up(heap, idx, another_solution):
            if idx == 0:
                return
            father = int((idx - 1) / 3)
            if heap[idx] >= heap[father]:
                another_solution += "Interschimbam elementele " + str(heap[idx]) + " si " + str(heap[father]) + '\n'
                heap[father], heap[idx] = heap[idx], heap[father]
                sift_up(heap, father, another_solution)

                return another_solution

        def sift_down(heap, idx, another_solution):
            n = len(heap)
            swap_son = idx
            left_son = 3 * idx + 1
            middle_son = 3 * idx + 2
            right_son = 3 * idx + 3
            if left_son < n and heap[left_son] > heap[swap_son]:
                swap_son = left_son
            if middle_son < n and heap[middle_son] > heap[swap_son]:
                swap_son = middle_son
            if right_son < n and heap[right_son] > heap[swap_son]:
                swap_son = right_son
            heap[idx], heap[swap_son] = heap[swap_son], heap[idx]
            another_solution += 'Interschimb ' + str(heap[idx]) + ' si ' + str(heap[swap_son]) + '\n'
            if swap_son != idx:
                sift_down(heap, swap_son, another_solution)

                return another_solution

        heap = []
        j = 1
        for i in range(len(data)):
            solution += "\t" + str(1) + "." + str(j) + " : "
            j += 1
            heap.append(data[i])
            solution += str(heap) + '\n'
            result = sift_up(heap, i, '')
            if result is not None:
                solution += result

        solution += '\t2.Arborele in heap : ' + str(heap) + '\n'

        solution += '\t3.Pentru decapitare interschimbam : ' + str(heap[0]) + ' si ' + str(heap[len(heap) - 1]) + '\n'
        heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
        heap.pop()
        solution += '\t4.Arborele decapitat ' + str(heap) + '\n'
        result = sift_down(heap, 0, '')
        solution += result
        solution += '\t5.Arborele rearanjat ' + str(heap) + '\n'

        return solution