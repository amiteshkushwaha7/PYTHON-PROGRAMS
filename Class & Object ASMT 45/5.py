class Team:
    def inputMember(self,memberList):
        self.memberList = memberList
        
    def displayMembers(self):
        for m in self.memberList:
            print(m)
            
obj = Team()
obj.inputMember(["Cristiano Ronaldo","Leonal Messi","Mbaape"])
obj.displayMembers()