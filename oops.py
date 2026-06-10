class car :
    def __init__(self,model,colour):
        self.model=model
        self.colour=colour

model=input("Enter model:")
colour=input("Enter colour:")
s1=car(model,colour)
print(s1.model)
print(s1.colour)