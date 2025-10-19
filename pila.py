# pila_simulador.py
# Programa de demostración de una pila usando lista en Python

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)
        print(f"'{item}' agregado a la pila.")

    def desapilar(self):
        if self.esta_vacia():
            print("⚠La pila está vacía, no se puede desapilar.")
        else:
            eliminado = self.items.pop()
            print(f"Elemento eliminado: '{eliminado}'")

    def cima(self):
        if self.esta_vacia():
            print(" La pila está vacía.")
        else:
            print(f" Elemento en la cima: '{self.items[-1]}'")

    def mostrar(self):
        if self.esta_vacia():
            print("⚠La pila está vacía.")
        else:
            print("\n--- Contenido de la pila (de abajo a arriba) ---")
            for i, elemento in enumerate(self.items):
                print(f"{i + 1}: {elemento}")
            print("-----------------------------------------------")


def menu():
    pila = Pila()
    while True:
        print("\n===== MENÚ PILA =====")
        print("1. Apilar (Push)")
        print("2. Desapilar (Pop)")
        print("3. Ver cima (Peek)")
        print("4. Mostrar pila")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            dato = input("Ingresa el elemento a apilar: ")
            pila.apilar(dato)
        elif opcion == '2':
            pila.desapilar()
        elif opcion == '3':
            pila.cima()
        elif opcion == '4':
            pila.mostrar()
        elif opcion == '5':
            print("Saliendo del programa de Pila...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


# Programa principal
if __name__ == "__main__":
    menu()
