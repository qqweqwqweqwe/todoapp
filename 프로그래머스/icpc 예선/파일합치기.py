filelist=[1, 21, 3, 4, 5, 35, 5, 4, 3, 5, 98, 21, 14, 17, 32]
answer=0

def merge(filelist:list):
  minsum=filelist[1]+filelist[0]
  start_idx=0
  end_idx=1
  for i in range(len(filelist)-1):
    if filelist[i]+filelist[i+1]<minsum:
      start_idx=i
      end_idx=i+1
      minsum=filelist[i]+filelist[i+1]
  filelist[start_idx]=minsum
  filelist.pop(end_idx)
  return minsum
  
for i in range(len(filelist)-1):
  answer+=merge(filelist)

print(answer)
