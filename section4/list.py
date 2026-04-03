Names=["Alice","Bob","Caroline","David","Ella"]
print(Names[1:4])
print(Names[:3])
print(Names[1:])

rank_list=[100,98,88,80,75,64]
rank_list.pop()
rank_list.append(70)
print(rank_list)
#[100, 98, 88, 80, 75, 70]

#pop 更恰当的解释是化学实验中的胶头滴管。
#当你pop一个位置的时候就是拿胶头滴管把那个位置的元素吸进滴管里面。 
#pop返回的值就是你吸得位置的值

#这部分在后面的queue中有用到