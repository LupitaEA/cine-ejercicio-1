#cine 
#definir clases para el cine
class Persona():
    def __init__(self, name, id, email, telefono):
        self.name = name
        self.id = id
        self.email = email
        self.telefono = telefono

#clase usuario, empleado y administrador heredan de persona
class Usuario(Persona):
        def __init__(self, name, id, email, telefono, dinero, puntos):
            super().__init__(name, id, email, telefono)
            self.dinero = dinero
            self.puntos = puntos
            self.historial_reservas = []
        def login(self):
            print(f"Hola {self.name}, bienvenido al cine Ds3")
            print(f"Tu Crédito es de:${self.dinero}")
        def logout(self):
            print(f"Nos vemos {self.name}, gracias por visitar el cine")
        def actualizar_data(self, name, email, telefono):
            self.name = name
            self.email = email
            self.telefono = telefono
        def deposito(self, monto):
            self.dinero += monto
            print(f"Depósito realizado con éxito, tu nuevo saldo es: ${self.dinero}")
        def crear_reserva(self, reserva):
            self.historial_reservas.append(reserva)
            print(f"Reserva agregada al perfil de {self.name}")
        def cancelar_reserva(self, reserva):
            if reserva in self.historial_reservas:
                self.historial_reservas.remove(reserva)
                print("Reserva cancelada exitosamente.")
            else:
                print("La reserva no se encuentra en el historial.")
        def promociones(self):
            if self.puntos >= 100:
                print("¡Felicidades! Puedes canjear tus puntos por una promoción.")
            else:
                print(f"Te faltan {100 - self.puntos} puntos para canjear una promoción.")


class Empleado(Persona):
        def __init__(self, name, id, email, telefono, trabajo):
            super().__init__(name, id, email, telefono)
            self.trabajo = trabajo
        def login(self):
            print(f"Hola {self.name}")
            print(f"Tu trabajo es de:{self.trabajo}")
            print(f"Identificación:{self.id}")
        def logout(self):
            print(f"Que te vaya bien {self.name} !, gracias por tu trabajo !")
        def actualizar_data(self, email, telefono, trabajo):
            self.email = email
            self.telefono = telefono
            self.trabajo = trabajo
        def marcar_entrada(self):
            print(f"{self.name} ha marcado su entrada.")
        def gestionar_funciones(self):
            if self.trabajo == "admin":
                print(f"{self.name} está gestionando las funciones")
            else:
                print("No tienes permiso para gestionar funciones")

#administrador hereda de empleado
class Administrador(Empleado):
        def __init__(self, name, id, email, telefono, trabajo, privilegios):
            super().__init__(name, id, email, telefono, trabajo)
            self.privilegios = privilegios
        def login(self):
            print(f"Hola {self.name}")
            print(f"Tu trabajo es de:{self.trabajo}")
            print(f"Identificación:{self.id}")
            print(f"Privilegios:{self.privilegios}")
        def logout(self):
            print(f"Con cuidado {self.name}, gracias por tu trabajo")
        def marcar_entrada(self):
            print(f"{self.name} ha marcado su entrada.")
        def gestionar_funciones(self):
            print(f"{self.name} está gestionando las funciones del cine")
        def agregar_pelicula(self, lista_peliculas, pelicula):
            lista_peliculas.append(pelicula)
            print(f"Película {pelicula.titulo} agregada correctamente")
#clase espacio, sala y comida heredan de espacio
class Espacio():
    def __init__(self, lugar):
        self.lugar = lugar
    def limpiar(self):
        print(f"Limpiando espacio en {self.lugar}")
    def disponibilidad(self):
        print(f"Verificando disponibilidad de {self.lugar}")


class Sala(Espacio):
        def __init__(self, lugar, tipo, capacidad, vip):
            super().__init__(lugar)
            self.tipo = tipo
            self.capacidad = capacidad
            self.vip = vip
            self.asientos_ocupados = []

        def que_sala_es(self):
            print(f"Esta sala es de tipo {self.tipo} con una capacidad de {self.capacidad} personas")
        def ayustar_aforo(self, nueva_capacidad):
            self.capacidad = nueva_capacidad
            print(f"La capacidad de la sala ha sido ajustada a {self.capacidad} personas")
        def asiento_libre(self, asiento):
            return asiento not in self.asientos_ocupados


class Comida(Espacio):
         def __init__(self, lugar, stock, productos):
                super().__init__(lugar)
                self.stock = stock
                self.productos = productos
         def vender_producto(self, producto):
                if producto in self.productos and self.stock > 0:
                    self.stock -= 1
                    print(f"Producto {producto} vendido. Stock restante: {self.stock}")
                else:
                    print(f"Producto {producto} no disponible o sin stock.")
         def actualizar_sttock(self, nuevo_stock):
                self.stock = nuevo_stock
                print(f"El stock ha sido actualizado a {self.stock} unidades")

#clase pelicula, funcion, promocion y reserva
class Pelicula():
        def __init__(self, titulo, duracion, genero, clasificacion):
            self.titulo = titulo
            self.duracion = duracion
            self.genero = genero
            self.clasificacion = clasificacion
        def reseña(self):
            print(f"Película: {self.titulo}")
            print(f"Duración: {self.duracion} minutos")
            print(f"Genero: {self.genero}")
            print(f"Clasificación: {self.clasificacion}")
        def clasificacion_edad(self):
             if self.clasificacion == "A":
                print("Esta película es apta para todo publico.")
             elif self.clasificacion == "B":
                print("Esta película es apta para mayores de 12 años.")
             elif self.clasificacion == "C":
                print("Esta película es apta para mayores de 18 años.")
             else:
                print("Clasificación desconocida.")


class Funcion():
        def __init__(self, pelicula, sala, horario, precio):
            self.pelicula = pelicula
            self.sala = sala
            self.horario = horario
            self.precio = precio
        def lugares_disponibles(self):
            libres = self.sala.capacidad - len(self.sala.asientos_ocupados)
            print(f"En la función de {self.pelicula.titulo} hay {libres} lugares disponibles")
            return libres
        def detalles_funcion(self):
            self.pelicula.reseña()
            self.sala.que_sala_es()
            print(f"Horario: {self.horario}")
            print(f"Precio por asiento: ${self.precio}")


class Promocion():
        def __init__(self, codigo, descripcion, descuento, vencimiento):
            self.codigo = codigo
            self.descripcion = descripcion
            self.descuento = descuento  # porcentaje ej: 20
            self.vencimiento = vencimiento
        def es_valida(self):
            from datetime import date
            if date.today() <= self.vencimiento:
                print(f"Promoción {self.codigo} válida hasta {self.vencimiento}")
                return True
            else:
                print(f"Promoción {self.codigo} vencida")
                return False
        def aplicar_descuento(self, monto):
            if self.es_valida():
                a = monto * (self.descuento / 100)
                total = monto - a
                print(f"Descuento de {self.descuento}% aplicado, ahorraste ${a:.2f}")
                print(f"Total a pagar: ${total:.2f}")
                return total
            return monto


class Reserva():
    contador = 1

    def __init__(self, usuario, funcion, asientos):
        self.id = Reserva.contador
        Reserva.contador += 1
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = []
        self.estado = "Pendiente"
        self.total = 0

        # verificar que los asientos no esten ocupados
        for a in asientos:
            if self.funcion.sala.asiento_libre(a):
                self.asientos.append(a)
                self.funcion.sala.asientos_ocupados.append(a)
                print(f"Asiento {a} bloqueado correctamente")
            else:
                print(f"El asiento {a} ya esta ocupado, no se agregó")

        self.total = len(self.asientos) * self.funcion.precio

    def confirmar_pago(self):
        if self.estado == "Pendiente":
            if self.usuario.dinero >= self.total:
                self.usuario.dinero -= self.total
                self.usuario.puntos += int(self.total // 10)
                self.estado = "Confirmada"
                self.usuario.crear_reserva(self)
                print(f"Pago confirmado. Se cobraron ${self.total:.2f}")
            else:
                print(f"Saldo insuficiente. Necesitas ${self.total:.2f} y tienes ${self.usuario.dinero:.2f}")
        else:
            print(f"La reserva ya está en estado: {self.estado}")

    def aplicar_descuento(self, promo):
        if self.estado == "Pendiente":
            self.total = promo.aplicar_descuento(self.total)
        else:
            print("Sólo se puede aplicar descuento a reservas pendientes")

    def generar_ticket(self):
        if self.estado == "Confirmada":
            print(f"---- TICKET RESERVA #{self.id} ----")
            print(f"Usuario: {self.usuario.name}")
            print(f"Película: {self.funcion.pelicula.titulo}")
            print(f"Sala: {self.funcion.sala.lugar} ({self.funcion.sala.tipo})")
            print(f"Horario: {self.funcion.horario}")
            print(f"Asientos: {self.asientos}")
            print(f"Total pagado: ${self.total:.2f}")
            print(f"Estado: {self.estado}")
            print("----------------------------------")
        else:
            print("No se puede generar el ticket, la reserva no esta confirmada")

class Producto():
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Categoría: {self.categoria}"