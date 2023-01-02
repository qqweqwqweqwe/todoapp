  def solution(n):
    first=0
    second=1
    for i in range(2,n):
      first,second=second,first+second

    return second%1234567