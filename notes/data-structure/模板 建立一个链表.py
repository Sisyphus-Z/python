class node():
    def __init__(self,a,b=None):
        self.v=a
        self.next=b

Head=node(0)
x=Head
for i in range(1,10):

    x.next=node(i)
    x=x.next


for i in range(9):
    print(Head.v)
    Head= Head.next

print(Head)
