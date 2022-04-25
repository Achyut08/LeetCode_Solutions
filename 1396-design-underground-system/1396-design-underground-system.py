class UndergroundSystem:

    def __init__(self):
        self.c=[]
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.t=[]
        self.t.extend([id,stationName,t])
        self.c.append(self.t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for i in range(len(self.c)):
            if len(self.c[i])==3 and self.c[i][0]==id:
                self.c[i].append(stationName)
                self.c[i].append(t)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        temp=[]
        for l in self.c:
            try:
                if l[1]==startStation and l[3]==endStation:
                    temp.append(l[4]-l[2])
            except:
                continue
        return sum(temp)/len(temp)