# 535. Encode and Decode TinyURL
# https://leetcode.com/problems/encode-and-decode-tinyurl
import unittest


class Codec:
    def __init__(self):
        self.hash_dic = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = hash(longUrl)
        self.hash_dic[str(key)] = longUrl
        return 'http://tinyurl.com/' + str(key)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.hash_dic[shortUrl.replace('http://tinyurl.com/', '')]


class TestCodec(unittest.TestCase):
    def test(self):
        # Your Codec object will be instantiated and called as such:
        codec = Codec()
        url = 'https://leetcode.com/problems/design-tinyurl'
        self.assertEqual(
            codec.decode(codec.encode(url)),
            url
        )


if __name__ == '__main__':
    unittest.TestCase()
