from unicodedata import name

#Clase padre
class Person:
    def __init__(self, name:str, age: int, size: float, hair_color: str):
        self.name = name
        self.age = age
        self.size = size
        self.hair_color = hair_color

    def walk(self, distance: int):
        return f"Me llamo {self.name} y hoy camine {distance} metros"

    def eat(self, food: str):
        return f"Me llamo {self.name} y hoy comí {food}"

    def speak(self, language: str):
        return f"Me llamo {self.name} y hablo {language}"

#clase hija 
class Student(Person):
    def Study(self, subject: str):
        return f"Mi nombre es {self.name} y estoy estudiando {subject}"


#clase hija
class Teacher(Person):
    def Teach(self, subject: str):
        return f"Mi nombre es {self.name} y soy su profesor de {subject}"


s1 = Student("Antonio", 20, 1.80, "Marron")

t1 = Teacher("Octavio", 57, 1.70, "Negro")


print("-"*50)
print(s1.walk(100))
print("")
print(t1.walk(500))
print("-"*50)

print(s1.eat("Alfajor"))
print("")
print(t1.eat("Arroz"))
print("-"*50)

print(s1.speak("Español"))
print("")
print(t1.speak("ESpañol, ingles y ruso"))
print("-"*50)

print(s1.Study("Matemáticas puras"))
print("")
print(t1.Teach("Filosofia"))
print("-"*50)