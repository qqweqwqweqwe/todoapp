


def solution(files):
  filelist=[]
  for file in files:
    number=""
    file.split()
    for i in range(len(file)):
      if file[i].isdigit():
        while file[i].isdigit():
          number+=file[i]
          i+=1
        break
    file=file.split(number)
    head=file[0]
    tail=file[1]
    filelist.append([head,number,tail])
  print(filelist)
  filelist=sorted(filelist,key=lambda x :x[0])
  print(filelist)
  
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])