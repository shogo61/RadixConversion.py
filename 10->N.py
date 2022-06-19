num=int(input("１０進数の数字を入力してください"))
N=int(input("何進数にしますか？"))

# 空だとエラーが起こる
weight =[1]
ans = []

# 重みの配列を降順で生成
i=1
while(weight[0]<num):
  weight.insert(0,N**i)
  i+=1
del weight[0] # 一番大きいのを削除

# 数字から重みを何回引けるか数えて、ansに格納していく
cnt=0
box=0
while(cnt<len(weight)):
  if((weight[cnt]-num)<=0):
    box+=1
    num-=weight[cnt]
  else:
    cnt+=1
    ans.append(box)
    box=0

# 答えの表示
print("答えは　：　",end="")
for i in ans:
  print(i,end="")
