class Time():
  def __init__(self, hrs, mins):
    self.hrs = hrs
    self.mins = mins
  @staticmethod
  def addTime(t1, t2):
    t3 = Time(0,0)
    if t1.mins+t2.mins > 60:
      t3.hrs = (t1.mins+t2.mins)//60
    t3.hrs = t3.hrs+t1.hrs+t2.hrs
    t3.mins = (t1.mins + t2.mins) % 60
    return t3
  def displayTime(self):
    print ("Time is",self.hrs,"hrs &",self.mins,"minutes.")
  def displayMinute(self):
    print ((self.hrs*60)+self.mins)
a = Time(3,40)
b = Time(5,30)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
