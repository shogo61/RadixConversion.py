print("N進数を１０進数に変換します")
val=int(input("数字を入力してください"))
N=int(input("何進数ですか？"))

weight=[]
num=list(str(val))

# 重みの配列を降順で生成
for i in range(0,len(num),1):
  weight.insert(0,N**i)

# 全桁で要素と重みをかける
total=0
for i in range(0,len(num),1):
  total+=int(num[i])*weight[i]

print(total)
