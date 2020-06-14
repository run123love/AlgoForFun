from Sort import Sort
import itertools

class Shell(Sort):
    """希尔排序"""

    @classmethod
    def sort(cls, arr):
        N = len(arr)
        # 定义一个h生成器
        def init_h(N):
            h = 1
            while h < N/3:
                h = 3*h + 1
            return h
        h = init_h(N)
        while h >= 1:
            for i in range(h, N):
                for j in reversed(range(0, i+1, h)):
                    if j >=h and cls.less(arr[j], arr[j-h]):
                        cls.exch(arr, j, j-h)
            h = h // 3

        return arr


if __name__ == "__main__":
    test = [4,3,2,1]
    sorted_arr = Shell.sort(test)
    Shell.show(sorted_arr)

    test = list("SIMPLESHELLEXEMPLEFORFUN")
    sorted_arr = Shell.sort(test)
    Shell.show(sorted_arr)