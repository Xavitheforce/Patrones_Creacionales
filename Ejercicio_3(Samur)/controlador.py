import pandas as pd

def separador():
    print("--------------------------------------------------")

def login():
    nombre = input("Ingrese su nombre de usuario: ")
    print('\n')
    contraseña = input("Ingrese su contraseña: ")
    print('\n')
    usuarios = pd.read_csv('Ejercicio_3(Samur)/usuarios.csv', sep=';')
    if nombre in usuarios['Usuario'].values:
        if contraseña in usuarios['Contraseña'].values:
            print("¡Bienvenido!")
        else:
            print("Contraseña incorrecta")
            login()
    else:
        print("Nombre de usuario incorrecto")
        login()

def registrarse():
    print("Registro de usuario:\n")
    usuario = input("Usuario: ")
    #el nombre de usuario no puede estar vacío ni tener espacios
    while usuario == "" or " " in usuario:
        print("El nombre de usuario no puede estar vacío ni tener espacios")
        usuario = input("Usuario: ")
    print('\n')
    nombre = input("Nombre: ")
    #el nombre no puede estar vacío
    while nombre == "":
        print("El nombre no puede estar vacío!")
        nombre = input("Nombre: ")
    print('\n')
    apellidos = input("Apellidos: ")
    print('\n')
    correo = input("Correo: ")
    #el correo no puede estar vacío, no debe tener espacios y debe tener formato de correo
    while correo == "" or "@" not in correo or ".com" not in correo or ".es" not in correo or " " in correo or correo.count("@") > 1 or correo.count(".com") > 1 or correo.count(".es") > 1:
        print("El correo no puede estar vacío y debe tener formato de correo (solo se admiten .com y .es)")
        correo = input("Correo: ")
    print('\n')
    contraseña = input("Contraseña: ")
    #la contraseña no puede estar vacía
    while contraseña == "":
        print("La contraseña no puede estar vacía!")
        contraseña = input("Contraseña: ")
    print('\n')
    confirmar_contraseña = input("Confirmar Contraseña: ")
    #la contraseña no puede estar vacía
    while confirmar_contraseña == "":
        print("La contraseña no puede estar vacía!")
        confirmar_contraseña = input("Confirmar Contraseña: ")

    if contraseña == confirmar_contraseña:
        usuarios = pd.read_csv('Ejercicio_3(Samur)/usuarios.csv', sep=';')
        ids_registrados = usuarios['ID'].values

        #si el usuario y la contraseña ya existen volver atrás
        if nombre in usuarios['Usuario'].values:
            if contraseña in usuarios['Contraseña'].values:
                print("El usuario ya existe.")
                gestor()
        else:
            if len(ids_registrados) == 0:
                identificador = 1
            else:
                identificador = max(ids_registrados) + 1

            nuevo_usuario = pd.DataFrame({'ID': [identificador], 'Usuario': [usuario], 'Nombre': [nombre], 'Apellidos': [apellidos], 'Email': [correo], 'Contraseña': [contraseña]})
            nuevo_usuario.to_csv('Ejercicio_3(Samur)/usuarios.csv', sep=';', mode='a', header=False, index=False)
            print("¡Registro exitoso!")
    else:
        print("Las contraseñas no coinciden. Vuelve a intentarlo.")
        registrarse()

def login_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    print('\n')
    contraseña = input("Ingrese su contraseña: ")
    print('\n')
    usuarios = pd.read_csv('Ejercicio_3(Samur)/admin.csv', sep=';')
    if nombre in usuarios['Usuario'].values:
        if contraseña in usuarios['Contraseña'].values:
            print(f"¡Bienvenido administrador {nombre}!")
        else:
            print("Contraseña incorrecta")
            login_usuario()
    else:
        print("Nombre de usuario incorrecto")
        login_usuario()

def gestor():
    print("1. Login")
    print("2. Registrarse")
    print("3. Salir")
    separador()
    opcion = input("Introduzca una opción: ")
    if opcion == "1":
        login()
        return True
    elif opcion == "2":
        registrarse()
        return True
    elif opcion == "3":
        print("Hasta pronto")
    elif opcion == "/admin":
        login_usuario()
        return True
    else:
        print("\nOpción incorrecta\n")
        gestor()