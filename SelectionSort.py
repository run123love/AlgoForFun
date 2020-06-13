from Sort import Sort

class Selection(Sort):
    @classmethod
    def sort(cls, arr):
        for i in range(len(arr)):
            min = i
            for j in range(i+1, len(arr)):
                if cls.less(arr[j], arr[i]):
                    min = j
            cls.exch(arr, i, min)
        return arr

if __name__ == "__main__":
    test = [4,3,2,1]
    sorted_arr = Selection.sort(test)
    Selection.show(sorted_arr)

    test = list("EXEMPLE")
    sorted_arr = Selection.sort(test)
    Selection.show(sorted_arr)