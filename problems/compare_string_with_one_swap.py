import unittest


# Time complexity: O(n)
# Space complexity: O(n)
def is_compare_with_one_swap(a_str, b_str):
    if not a_str or not b_str:
        return False
    if len(a_str) != len(b_str):
        return False

    left_ptr = 0
    a_arr = list(a_str)
    b_arr = list(b_str)
    right_ptr = len(a_arr) - 1

    while a_arr[left_ptr] == b_arr[left_ptr] and left_ptr < len(b_arr):
        left_ptr += 1
    while a_arr[right_ptr] == b_arr[right_ptr] and 0 < right_ptr:
        right_ptr -= 1
    if left_ptr != len(b_arr) - 1 or right_ptr != 0:
        a_arr[left_ptr], a_arr[right_ptr] = a_arr[right_ptr], a_arr[left_ptr]
        if a_arr == b_arr:
            return True
    return False


class TestIsCompareWithOneSwap(unittest.TestCase):
    def test(self):
        self.assertTrue(is_compare_with_one_swap('reverse', 'reserve'))
        self.assertFalse(is_compare_with_one_swap('reveres', 'reserve'))
        self.assertFalse(is_compare_with_one_swap('abc', 'abcd'))
        self.assertFalse(is_compare_with_one_swap('', 'acd'))
        self.assertTrue(is_compare_with_one_swap('cad', 'acd'))
        self.assertFalse(is_compare_with_one_swap('cda', 'acd'))
        self.assertTrue(is_compare_with_one_swap('caddddddc', 'acddddddc'))
        self.assertTrue(is_compare_with_one_swap('123', '321'))
        self.assertFalse(is_compare_with_one_swap('123', '121'))
        self.assertTrue(is_compare_with_one_swap('1332', '1233'))


if __name__ == '__main__':
    unittest.TestCase()
