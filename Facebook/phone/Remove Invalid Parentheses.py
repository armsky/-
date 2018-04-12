"""
Remove the minimum number of invalid parentheses in order to make the input
string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        # solution BFS
        import queue
        q = queue.Queue()
        q.put(s)
        results, visited = [], set()
        visited.add(s)
        isStop = False
        while not q.empty():
            size = q.qsize()
            for k in range(size):
                s = q.get()
                if self.check_valid(s):
                    isStop = True
                    results.append(s)
                if isStop:
                    break
                for i in range(len(s)):
                    if s[i] == "(" or s[i] == ")":
                        new_s = s[:i] + s[i+1:]
                        if new_s not in visited:
                            q.put(new_s)
                            visited.add(new_s)
        if not results:
            return [""]
        return results

    def check_valid(self, s):

        counter = 0
        for c in s:
            if counter < 0:
                return False
            if c == "(":
                counter += 1
            if c == ")":
                counter -= 1
        return counter == 0
