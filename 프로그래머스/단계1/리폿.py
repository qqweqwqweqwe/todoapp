

def solution(id_list, report, k):
  report_list={}
  report_count={}
  
  report=set(report)
  report=list(report)
  # 중복 제거


  for id in id_list:
    report_list[id]=[]
    report_count[id]=0

  #키값이 신고한 애들 발류 값이 신고 당한 애들
  #카운트 값이 신고 당한 횟수
  
  #신고한새끼들 리스트 생성
  
  for rep in report:
    rep_prep=rep.split()
    report_count[rep_prep[1]]+=1
    report_list[rep_prep[0]].append(rep_prep[1])

  disable_list=[]
  #정지된 애들 모음
  for id in report_count.keys():
    if report_count[id]>=k:
      disable_list.append(id)

  i=0

  # 신고 당한 횟수 계산

  answer = []

  for key in report_list.keys():
    numofreport=len(list(set(report_list[key])&set(disable_list)))
    answer.append(numofreport)
  return answer


id_list=["muzi", "frodo", "apeach", "neo"]	
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	

print(solution(id_list,report,2))
