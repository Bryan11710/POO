class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)
        self.categoria, self.isbn = categoria, isbn

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre, self.user_id = nombre, user_id
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.user_id] = usuario

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            self.usuarios[user_id].libros_prestados.append(self.libros.pop(isbn))

    def devolver_libro(self, user_id, isbn):
        usuario = self.usuarios.get(user_id)
        if usuario:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    self.libros[isbn] = libro
                    usuario.libros_prestados.remove(libro)
                    break

    def listar_libros_prestados(self, user_id):
        return [libro.info[1] for libro in self.usuarios.get(user_id, Usuario('', '')).libros_prestados]

biblioteca = Biblioteca()
biblioteca.agregar_libro(Libro("Cien años de soledad", "G.G. Márquez", "Novela", "123"))
biblioteca.registrar_usuario(Usuario("Juan Pérez", "U001"))
biblioteca.prestar_libro("U001", "123")
print(biblioteca.listar_libros_prestados("U001"))
