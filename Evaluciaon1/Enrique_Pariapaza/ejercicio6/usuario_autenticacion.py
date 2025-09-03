# Esta clase define un usuario con credenciales de acceso.
class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
# Esta clase se encarga de la lógica de registro y acceso de usuarios.
class Auth:
    def __init__(self):
        self.usuarios_registrados = {}
        
    def registrar_usuario(self, usuario):
        if usuario.username in self.usuarios_registrados:
            print(f"El usuario '{usuario.username}' ya existe.")
            return False
        
        self.usuarios_registrados[usuario.username] = usuario.password
        print(f"Usuario '{usuario.username}' registrado con éxito.")
        return True
        
    def login(self, username, password):
        if username in self.usuarios_registrados and self.usuarios_registrados[username] == password:
            print(f"¡Bienvenido, '{username}'! Has iniciado sesión con éxito.")
            return True
        else:
            print("Error: Nombre de usuario o contraseña incorrectos.")
            return False