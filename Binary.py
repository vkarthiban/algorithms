
class BinaryTree:
    
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None
        
    def add_chiled(self,data):
        
        if data == self.data:
            return
        if data < self.data:
            
            if self.left:
                print("left0000000000",data)
                self.left.add_chiled(data)
            else:
                print("left00else00000000",data)
                self.left = BinaryTree(data)
        else:
            if self.right:
                print("rigthj000000",data)
                self.right.add_chiled(data)
            else:
                print("rigtelsehj000000",data)
                self.right = BinaryTree(data)            
            
        
    def search(self,data):
        if data == self.data:
            return self.data
        
        if data > self.data:
            if self.left:
                print("lesft",data,self.data)
                return self.left.search(data)
            else:
                return False
        
        else:
            if self.right:
                print("right",data,)
                return self.right.search(data)
            else:
                return False
        
        

bin = BinaryTree(50)

for cnt in range(48,55):
    bin.add_chiled(cnt)
    
    

print("dataddsafewsdde",bin.search(51))
    
    

class recursion:
    
    def __init__(self,data):
        self.data = data
        self.obj = None
        
    def add(self,data):
        if self.obj:
            print("added",data,self.obj.data)
            self.obj.add(data)
        else:
            print("none called...",data)
            self.obj = recursion(data)
        
    def find_all(self):       
        if self.obj:
            print("datas",self.obj.data)
            self.obj.find_all()
        else:
            return             
        
objx = recursion(0)
for cnt in range(45,60):
    objx.add(cnt)
    
objx.find_all()

