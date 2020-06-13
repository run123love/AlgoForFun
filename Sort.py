
class Sort:
    """排序通用模板类"""
    @classmethod
    def sort(cls, arr):
        raise NotImplementedError("必须实现sort方法！")

    @classmethod
    def less(cls, arrA, arrB):
        return arrA < arrB

    @classmethod
    def exch(cls, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    @classmethod
    def show(cls, arr):
        for item in arr:
            print(item, end=" ")
        print()

    @classmethod
    def isSorted(cls, arr):
        for i in range(start=1, stop=len(arr)):
            if cls.less(arr[i], arr[i-1]):
                return False
        return True