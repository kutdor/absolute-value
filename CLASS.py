class Linux:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def idk(self):
        pass
    
    def thglinuxnoi(self):
        print("ĐM, ẢO THẬT ĐẤY")
    
if __name__ == "__main__" :       
    
    ln = Linux("thanh", 16, "male")
    print(f"thằng linux hay nói: \n{ln.thglinuxnoi()}")
    print("tên tuổi thằng linux: ")
    print(ln.name)
    print(ln.age)
    print(ln.sex)