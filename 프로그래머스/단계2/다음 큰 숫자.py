from typing import Counter
def numofone(n):
  return (Counter(n)['1'])
def solution(n):
  nextn=n+1
  n=format(n,'b')
  while True:
    if numofone(n)==numofone(format(nextn,'b')):
      return nextn
    nextn+=1
