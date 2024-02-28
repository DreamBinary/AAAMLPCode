# -*- coding:utf-8 -*-
# @FileName : tmp.py
# @Time : 2024/2/26 20:14
# @Author : fiv


class AllOne:

    def __init__(self):
        self.data = {}

    def inc(self, key: str) -> None:
        if key in self.data:
            self.data[key] += 1
        else:
            self.data[key] = 1

    def dec(self, key: str) -> None:
        if key in self.data:
            self.data[key] -= 1
            if self.data[key] == 0:
                del self.data[key]

    def getMaxKey(self) -> str:
        if len(self.data) == 0:
            return ""
        return max(self.data, key=self.data.get)

    def getMinKey(self) -> str:
        if len(self.data) == 0:
            return ""
        return min(self.data, key=self.data.get)

    # Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
