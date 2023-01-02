import math
def solution(n, words):
  answer = [0,0]
  spoken_words=[]
  spoken_words.append(words[0])
  for i in range(1,len(words)):
    print(words[i])
    if words[i] in spoken_words or words[i][0]!=words[i-1][-1] :
      answer=[i%n+1,math.ceil((i+1)/n)]
      return answer
    else:
      spoken_words.append(words[i])
  return answer
solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])