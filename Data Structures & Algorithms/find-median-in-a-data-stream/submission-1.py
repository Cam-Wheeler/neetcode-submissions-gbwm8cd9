class MedianFinder:

    def __init__(self):
        self.stream: List[int] = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()

    def findMedian(self) -> float:
        
        if len(self.stream) % 2:
            mean = math.floor(self.stream[int(len(self.stream) / 2)])
        else:
            l = int((len(self.stream) / 2) - 1)
            r = int(len(self.stream) / 2)
            mean = (self.stream[l] + self.stream[r]) / 2
        
        return mean 
        