#수강신청
#대기목록에 들어간다.
#대기열에 들어가있는데 다시 수강신청 버튼을 누르면 대기목록의 맨 뒤로 밀려난다
#수강신청 버튼이 비활성화되면 대기목록에서 가장 앞에 있는 학생부터 
#자동으로 수강신청이 완료되며, 
#수강 가능 인원이 꽉 찰 경우 나머지 대기목록은 무시하고 수강신청을 종료한다.

#중복된 대기목록을 삭제하고, 맨앞에서부터 수강 가능 인원만큼 선정
import sys
input=sys.stdin.readline

waiting_list={}
afford,waiting=map(int, input().split())
print(afford, waiting)
for i in range(waiting):
    waiting_list[input().rstrip()]=i

#waiting_list:{'20103324': 0, '20133221': 2, '20093778': 6, '20140101': 4, '01234567': 5, '20103325': 7}

sort=sorted(waiting_list.items())
sort=sorted(waiting_list.items(),key = lambda x:x[1])#순서대로 정렬하라는 뜻
#sort=[('20103324', 0), ('20133221', 2), ('20140101', 4), ('01234567', 5), ('20093778', 6), ('20103325', 7)]

if (afford>len(sort)):
    afford=len(sort)

for i in range(afford):
    print(sort[i][0])
