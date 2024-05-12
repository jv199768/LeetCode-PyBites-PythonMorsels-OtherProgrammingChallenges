
# Online Python - IDE, Editor, Compiler, Interpreter
class Dog:
    
    def __init__(self, species, name, age):
        self.species = "Canis familiaris"
        self.name = name 
        self.age = age
       

    def __str__(self):
        return f"{self.species}{self.name}({self.age})"

  
    def speak(self,sound): 
            def wrapper():
                if 5 <= len(sound) < 15:
                    print(sound)
                    return sound
                    
                else:
                    pass
                
            return wrapper
        
    def say_woof():
        print("Woof")


d1 = Dog ("Canis familaris", "Zippy", 7)
d1.speak(say_woof)
print (d1)
