from Sort import Sort
class Insertion(Sort):
    """插入排序"""
    @classmethod
    def sort(cls, arr):
        for i in range(1, len(arr)):
            for j in reversed(range(1, i+1)):
                if cls.less(arr[j], arr[j-1]):
                    cls.exch(arr, j, j-1)
        return arr

if __name__ == "__main__":
    test = [4,3,2,1]
    sorted_arr = Insertion.sort(test)
    Insertion.show(sorted_arr)

    test = list("EXEMPLE")
    sorted_arr = Insertion.sort(test)
    Insertion.show(sorted_arr)