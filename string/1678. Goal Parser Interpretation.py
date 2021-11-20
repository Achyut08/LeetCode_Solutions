class Solution:
    def interpret(self, command: str) -> str:
        res=[]
        dict={
            "G":"G",
            "()":"o",
            "(al)":"al"}
        for i in dict:
            command = command.replace(i,dict[i])
        return command
    
    
  
