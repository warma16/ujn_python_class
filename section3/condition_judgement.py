myWeight=70.5
yourWeight=81.3
if myWeight < yourWeight:
    print("You are heavier than me")
#输出:You are heavier than me

#小明可以买鞋吗
price=500
balance=600
if price <= balance:
    print("yes")

if price > balance:
    print("no")

#yes

'''管老师吃鸡腿吃的太多，就会变成一个胖子，所以当他一天内吃5个以上不包括5鸡腿是当天就要跑步'''

drumStick=3
if(drumStick>5):#C语言码风，小朋友们不要学我。 要这样写 if drumStick > 5:
    print("yes")
else:
    print("no")

print(f"今天吃了{drumStick}个鸡腿")

'''no
今天吃了3个鸡腿'''

myHeight=171
yourHeight=181
#快速做法。小孩子不要这样学。
temp="I am not shorter than you"
if myHeight<yourHeight:
    temp=temp.replace(" not","")
print(temp)
#I am shorter than you 输出

#慢速一点是
if myHeight<yourHeight:
    print("I am shorter than you")
else:
    print("I am not shorter than you")

a=3
b=4
c=5
if a*a+b*b==c*c :
    print("这是直角三角形")
else:
    print("这不是直角三角形")
#这是直角三角形
#简便的方法是，我先假设这东西不是直角三角形，然后发现它是，把不这个字用replace换掉即可，有兴趣可以自己研究下

weather="晴天"
action="宅在家"
if weather =="晴天":
    action="去爬山"
print("我们"+action)
#我们去爬山

#这段代码的逻辑是默认我们宅在家，如果是晴天就去爬山
#等效情况是

if weather == "晴天":
    print("我们去爬山")
else:
    print("我们宅在家")

#这串代码还可以这样写

print("我们去爬山" if weather == "晴天" else "我们宅在家")

bid=200
price=300
profit=8*price-10*bid
if profit>=0:
    print("回本了")
else:
    print("没回本")
#回本了

cityPopulation=10
if cityPopulation <=5 :
    print("small city")
elif cityPopulation > 5 and cityPopulation <= 40:
    print("middle city")
else:
    print("big city")
#middle city