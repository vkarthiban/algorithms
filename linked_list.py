
class linked_list:
    
    def __init__(self,data):
        self.data = data
        self.pre = None
        self.nxt = None
        
    def add_element(self,data):
        if self.nxt:
            self.nxt.add_element(data)
        else:
            self.nxt= linked_list(data)
            
            
    def show(self):
        if self.nxt:
            print(self.data)
            self.nxt.show()
        else:
            print(self.data)
            return
        
    def rshow(self):
        if self.pre:
            print(self.data)
            self.pre.show()
        else:
            return        
        
    def serach(self,val):
        if self.data == val:
            return self.data
        else:
            if self.nxt:
                return self.nxt.serach(val)
            else:
                return "NOT found"

                        
obj = linked_list(0)
for cnt in range(5,12):
    obj.add_element(cnt)

obj.show()
x = obj.serach(11)
print(x)


'''singly linked list create using recusion'''