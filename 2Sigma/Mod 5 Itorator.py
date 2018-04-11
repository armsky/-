
class ModFiveIterator:

    def __init__(self, l):
        self.l = l
        self.nextNum = None

    def next(self):
        if not self.hasNext():
            raise Exception('No Next !')

        return self.nextNum

    def hasNext(self):
        while self.l:
            n = self.l.pop()
            if n % 5 == 0:
                self.nextNum = n
                return True
        return False
