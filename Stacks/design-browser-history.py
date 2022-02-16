"""
    Design browser history
    Link: https://leetcode.com/problems/design-browser-history/
"""


# Simplest approach by using a list and a pointer
# Runtime: 235 ms, faster than 80.84% of Python3 online submissions for Design Browser History.
# Memory Usage: 16.7 MB, less than 62.87% of Python3 online submissions for Design Browser History.
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        # Erasing forward history
        self.history = self.history[:self.pos + 1]
        self.history.append(url)
        self.pos += 1

    def back(self, steps: int) -> str:
        # pos should be at least 0
        self.pos = max(0, self.pos - steps)
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        # pos should be at most len(history) - 1
        self.pos = min(len(self.history) - 1, self.pos + steps)
        return self.history[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)