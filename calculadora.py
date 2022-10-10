from math import ceil


class Calculadora():
    def _init_(self):
        self.valor3 = 0
        self.valor1 = 0
        self.valor2 = 0


    def sumar(self):
        self.valor3 = self.valor1 + self.valor2

    def restar(self):
        self.valor3 = self.valor1 - self.valor2


    def multiplicar(self):
        self.valor3 = self.valor1 * self.valor2


    def dividir(self):
        self.valor3 = self.valor1 / self.valor2


    def mostrarResultado(self):
        return self.valor3

cal = Calculadora()
opcion = 0
while opcion != "Terminar" :

        print("""
        Dime, ¿qué quieres hacer?
        
        1) Sumar los dos números
        2) Restar los dos números
        3) Multiplicar los dos números
        4) Dividir los dos números
        5) Salir
        """)

        

        try:
            opcion = int(input("Elige una opción: ") )
            cal.valor1 = int(input("ingrese el primer número: "))
            cal.valor2 = int(input("ingrese el segundo número: "))
        
            if opcion == 1:
                cal.sumar()
                print(" ")
                print("RESULTADO: La suma de",cal.valor1,"+",cal.valor2,"es igual a", cal.mostrarResultado())
            elif opcion == 2:
                cal.restar()
                print(" ")
                print("RESULTADO: La resta de",cal.valor1,"-",cal.valor2,"es igual a",cal.mostrarResultado())
            elif opcion == 3:
                cal.multiplicar()
                print(" ")
                print("RESULTADO: El producto de",cal.valor1,"*",cal.valor2,"es igual a",cal.mostrarResultado())
            elif opcion == 4:
                cal.dividir()
                print(" ")
                print("RESULTADO: El producto de",cal.valor1,"*",cal.valor2,"es igual a",cal.mostrarResultado())
            elif opcion == 5:
                print("")
                print("Gracias por utilizarme 8====D")
                break
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        except AttributeError:
            print("No se permiten vainas raras") 
        except ValueError:
            print("Perro solo puedo operar números, calmate :c")