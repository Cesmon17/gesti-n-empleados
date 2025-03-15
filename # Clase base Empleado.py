# Clase base Empleado
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: ${self.salario}")

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * (porcentaje / 100)

# Clase derivada Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, "Gerente", salario)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}")

# Clase derivada Trabajador
class Trabajador(Empleado):
    def __init__(self, nombre, salario, horas_extras):
        super().__init__(nombre, "Trabajador", salario)
        self.horas_extras = horas_extras

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Horas Extras: {self.horas_extras}")

# Programa principal para probar la herencia
def main():
    gerente = Gerente("Carlos López", 50000, "Recursos Humanos")
    trabajador = Trabajador("Ana Pérez", 20000, 10)
    
    print("Información del Gerente:")
    gerente.mostrar_info()
    
    print("\nInformación del Trabajador:")
    trabajador.mostrar_info()
    
    print("\nAumentando salario del Trabajador en 10%...")
    trabajador.aumentar_salario(10)
    trabajador.mostrar_info()

if __name__ == "__main__":
    main()