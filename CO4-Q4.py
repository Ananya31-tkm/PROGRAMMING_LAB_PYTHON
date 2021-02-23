class Time:
    def __init__(self,h,m,s):
        self.__hour=h
        self.__minute=m
        self.__second=s

    def time(self):
        if self.__second>=60:
            self.__second-=60
            self.__minute+=1
        if self.__minute>=60:
            self.__minute-=60
            self.__hour+=1
        return("%.2d:%.2d:%.2d"%(self.__hour,self.__minute,self.__second))
    def __add__(self,other):
        __hour=self.__hour+other.__hour
        __minute=self.__minute+other.__minute
        __second=self.__second+other.__second
        return("%.2d:%.2d:%.2d"%(__hour,__minute,__second))

t1=Time(2,60,60)
print("TIME 1",t1.time())
t2=Time(4,50,5)
print("TIME 2",t2.time())
print("\nTIME 1 + TIME 2: ",(t1 + t2))
