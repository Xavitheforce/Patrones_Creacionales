from controlador import *
import pandas as pd

if __name__ == "__main__":
    print("Bienvenido al gestor de documentos")
    separador()
    print("Identifíquese:")
    separador()
    separador()
    identificacion = gestor()
    if identificacion:
        pass