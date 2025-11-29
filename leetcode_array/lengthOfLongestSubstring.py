class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first = 0
        second = 0
        my_str = ''
        str_len = 0

        while second < len(s):
            if s[second] in my_str:
                # update max length
                str_len = max(str_len, second - first)

                # find the index of repeated char inside my_str
                idx = my_str.index(s[second])

                # shrink window: remove characters up to repeated one
                my_str = my_str[idx + 1:]

                # move first pointer accordingly
                first = first + idx + 1

            # add current char & expand window
            my_str += s[second]
            second += 1

        # final update for last window
        str_len = max(str_len, second - first)

        return str_len
