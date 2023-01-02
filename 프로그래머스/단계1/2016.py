from datetime import datetime


def solution(a:int, b:int):
  week=['FRI','SAT','SUN','MON','TUE','WED','THU']
  now = datetime.strptime("20160101","%Y%m%d")
  future_date="2016"+str(a).rjust(2,'0')+str(b).rjust(2,'0')
  future_date=datetime.strptime(future_date,"%Y%m%d")
  diff=future_date-now
  return week[diff.days%7]
  



# month 마다 날짜가 다른것을 배열로 만들어서 해보자 ㅎㅎ

solution(5,3)