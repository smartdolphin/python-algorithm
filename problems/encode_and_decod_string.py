# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings
import unittest


class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        result = []
        for s in strs:
            size = len(s)
            result.append(str(size) + '#' + s)
        return ''.join(result)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            number = []
            while ord('0') <= ord(s[i]) <= ord('9'):
                number.append(s[i])
                i += 1
            number = int(''.join(number))
            if s[i] == '#':
                content = s[i + 1:i + 1 + number]
                i += number + 1
            else:
                raise ValueError('Invalid encoded str')
            result.append(content)
        return result


class TestEncodeDecodeString(unittest.TestCase):
    def test(self):
        # Your Codec object will be instantiated and called as such:
        codec = Codec()
        list = ['abc', 'de', '12']
        self.assertEqual(
            codec.decode(codec.encode(list)),
            list
        )


if __name__ == '__main__':
    unittest.TestCase()
