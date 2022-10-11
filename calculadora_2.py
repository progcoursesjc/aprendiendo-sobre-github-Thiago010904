class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def numeros(self):
        try:
            num=input("Ingrese dos numeros y su operador: ")
            print("Si desea terminar la calculadora escriba terminar")
            Calculadora.proceso(num,self)
        except:
            if len(num.split()) != 3:
                print("Solo puedes ingresar dos numeros separados y su operador")
                print("-"*50)
                r.numeros()

    def proceso(num,self):
            if num != "terminar":
                try:
                    if num.split()[1] == "+":
                        self.resultado = int(num.split()[0]) + int(num.split()[2])
                        print(f"El resultado es: {self.resultado:}")
                        self.numeros()
                    elif num.split()[1] == "-":
                        self.resultado = int(num.split()[0]) - int(num.split()[2])
                        print(f"El resultado es: {self.resultado:}")
                        self.numeros()
                    elif num.split()[1] == "*":
                        self.resultado = int(num.split()[0]) * int(num.split()[2])
                        print(f"El resultado es: {self.resultado:}")
                        self.numeros()
                    elif num.split()[1] == "/":
                        self.resultado = int(num.split()[0]) / int(num.split()[2])
                        print(f"El resultado es: {self.resultado:}")
                        self.numeros()
                        
                except ZeroDivisionError:
                    print("No puedes dividir por 0 papi")
                    self.numeros()
                except AttributeError:
                    print("No se permiten vainas raras")
                    self.numeros()
                except ValueError:
                    print("Solo puedes ingresar números")
                    self.numeros()
    
                
r = Calculadora()
r.numeros()