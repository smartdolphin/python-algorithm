import unittest


def merge_sort(arr):
    def _merge(left, right):
        merged_list = []
        i, j = 0, 0
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                merged_list.append(left[i])
                i += 1
            else:
                merged_list.append(right[j])
                j += 1
        while len(left) > i:
            merged_list.append(left[i])
            i += 1
        while len(right) > j:
            merged_list.append(right[j])
            j += 1
        return merged_list

    def _merge_sort(list):
        if len(list) <= 1:
            return list
        mid = len(list) // 2
        left = _merge_sort(list[:mid])
        right = _merge_sort(list[mid:])
        return _merge(left, right)

    result = _merge_sort(arr)
    return result


class TestMergeSort(unittest.TestCase):
    def test(self):
        arr = merge_sort([5, 3, 2, 1, 4])
        self.assertEqual(
            arr,
            [1, 2, 3, 4, 5]
        )
        arr = merge_sort([-1, -10, 2, 4, 1])
        self.assertEqual(
            arr,
            [-10, -1, 1, 2, 4]
        )
        arr = merge_sort([1, -1, 5, 2, 4, 2])
        self.assertEqual(
            arr,
            [-1, 1, 2, 2, 4, 5]
        )
        arr = merge_sort([5, 2])
        self.assertEqual(
            arr,
            [2, 5]
        )
        arr = merge_sort([-1, -1, 2, 5, 4, 2])
        self.assertEqual(
            arr,
            [-1, -1, 2, 2, 4, 5]
        )


if __name__ == '__main__':
    unittest.TestCase()
