import bisect

class MyCalendar:
    def __init__(self):
        import math

        self.que=[-math.inf,math.inf]

    def book(self, start: int, end: int) -> bool:
        i=bisect.bisect_right(self.que,start)-1
        j=bisect.bisect_left(self.que,end)-1

        if i%2 or j%2 or j-i>1:
            return False
        self.que[i+1:j+1]=[start,end]

        return True


obj = MyCalendar()
print(obj.book(20,30))
