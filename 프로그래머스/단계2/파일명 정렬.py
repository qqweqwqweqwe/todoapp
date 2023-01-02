def splitt(file:str):
  start=0
  begin=0
  end=0
  while True:
    if file[start].isdigit():
      begin=start
      while start<len(file) and file[start].isdigit():
        start+=1
        end=start
      break
    start+=1
  head=file[0:begin]
  end=min(end,begin+5)
  number=file[begin:end]
  splitlist=[file,head,int(number)]
  return splitlist
def solution(files:list):
  answer=[]
  filelist=[]
  for file in files:
    filelist.append(splitt(file))
  filelist=sorted(filelist, key=lambda x:(x[1].lower(), x[2]))
  for i in filelist:
    answer.append(i[0])
  return answer