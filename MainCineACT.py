from datetime import date
from CINEACT import *

print("REGISTRO MANUAL DE INVENTARIO")

# Creación de objetos
p1 = Producto(1, "Palomitas Grandes", 85.0, "Snacks")
p2 = Producto(2,"Refresco Mediano", 45.0, "Bebidas")
p3 = Producto(3,"Hot Dog", 60.0, "Comida")
p4 = Producto(4, "Nachos con Queso", 70.0, "Snacks")
p5 = Producto(5, "Chocolate Crunch", 35.0, "Dulces")
p6 = Producto(6, "Agua Ciel 600ml", 30.0, "Bebidas")
p7 = Producto(7, "Combo Pareja", 210.0, "Combos")
p8 = Producto(8, "Entrada 2D Adulto", 80.0, "Boletos")
p9 = Producto(9, "Entrada 3D Niño", 65.0, "Boletos")
p10 = Producto(10, "Cubeta Promocional", 150.0, "Promos")

# Impresión de métodos
print(p1.mostrar_detalle())
print(p2.mostrar_detalle())
print(p3.mostrar_detalle())
print(p4.mostrar_detalle())
print(p5.mostrar_detalle())
print(p6.mostrar_detalle())
print(p7.mostrar_detalle())
print(p8.mostrar_detalle())
print(p9.mostrar_detalle())
print(p10.mostrar_detalle())

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")

def menu():
    while True:
        print("        CINE - SISTEMA DE RESERVAS      ")
        print("  1. Ver usuarios")
        print("  2. Ver empleados")
        print("  3. Ver salas")
        print("  4. Ver zonas de comida")
        print("  5. Ver películas")
        print("  6. Ver funciones del día")
        print("  7. Ver promociones")
        print("  8. Hacer una reserva")
        print("  9. Panel de empleado (admin)")
        print("  0. Salir")
        print("******************************************")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            mostrar_empleados()
        elif opcion == "3":
            mostrar_salas()
        elif opcion == "4":
            mostrar_zonas()
        elif opcion == "5":
            mostrar_peliculas()
        elif opcion == "6":
            mostrar_funciones()
        elif opcion == "7":
            mostrar_promociones()
        elif opcion == "8":
            hacer_reserva()
        elif opcion == "9":
            panel_empleado()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo")

# 10 usuarios
us1 = Usuario("Juan Perez", 1, "juanperez@mail.com", "5550001", 500, 150)
us2 = Usuario("Maria Lopez", 2, "marialopez@mail.com", "5550002", 300, 60)
us3 = Usuario("Carlos Sanchez", 3, "carlossanchez@mail.com", "5550003", 800, 200)
us4 = Usuario("Maria Lopez", 4, "marialopez@mail.com", "5550004", 150, 20)
us5 = Usuario("Pedro Ramirez", 5, "pedroramirez@mail.com", "5550005", 600, 80)
us6 = Usuario("Sofia Hernandez", 6, "sofiahernandez@mail.com", "5550006", 200, 40)
us7 = Usuario("Diego Castro", 7, "diegocastro@mail.com", "5550007", 450, 110)
us8 = Usuario("Valeria Flores", 8, "valeriaflores@mail.com", "5550008", 350, 90)
us9 = Usuario("Andres Morales", 9, "andresmorales@mail.com", "5550009", 700, 175)
us10 = Usuario("Camila Reyes", 10, "camilareyes@mail.com", "5550010", 250, 30)
usuarios = [us1, us2, us3, us4, us5, us6, us7, us8, us9, us10]
            
# 10 empleados
em1 = Empleado("Laura Gomez", 101, "lauragomez@mail.com", "5550001", "taquillero")
em2 = Empleado("Miguel Torres", 102, "migueltorres@mail.com", "5550002", "limpieza")
em3 = Empleado("Ana Martinez", 103, "anamartinez@mail.com", "5550003", "seguridad")
em4 = Empleado("Jorge Ramirez", 104, "jorgeramirez@mail.com", "5550004", "taquillero")
em5 = Empleado("Sofia Hernandez", 105, "sofiahernandez@mail.com", "5550005", "limpieza")
em6 = Empleado("Diego Castro", 106, "diegocastro@mail.com", "5550006", "seguridad")
em7 = Empleado("Valeria Flores", 107, "valeriaflores@mail.com", "5550007", "taquillero")
em8 = Empleado("Andres Morales", 108, "andresmorales@mail.com", "5550008", "limpieza")
em9 = Empleado("Camila Reyes", 109, "camilareyes@mail.com", "5550009", "seguridad")
em10 = Empleado("Juan Perez", 110, "juanperez@mail.com", "5550010", "taquillero")

empleados = [em1, em2, em3]

# 10 salas
sala1 = Sala("Sala 1", "2D", 80, False)
sala2 = Sala("Sala 2", "3D", 100, True)
sala3 = Sala("Sala 3", "2D", 60, False)
sala4 = Sala("Sala 4", "3D", 120, True)
sala5 = Sala("Sala 5", "2D", 70, False)
sala6 = Sala("Sala 6", "4D", 90, True)
sala7 = Sala("Sala 7", "2D", 50, False)
sala8 = Sala("Sala 8", "3D", 110, True)
sala9 = Sala("Sala 9", "2D", 65, False)
sala10 = Sala("Sala 10", "4D", 85, True)
salas = [sala1, sala2, sala3, sala4, sala5, sala6, sala7, sala8, sala9, sala10]

# 10 zonas de comida
comida1 = Comida("Norte", 50, ["Palomitas", "Refresco"])
comida2 = Comida("Sur", 40, ["Hot Dog", "Nachos"])
comida3 = Comida("Este", 30, ["Chocolate", "Agua"])
comida4 = Comida("Oeste", 20, ["Combo Pareja", "Cubeta Promocional"])
comida5 = Comida("Central", 60, ["Palomitas", "Hot Dog"])
comida6 = Comida("VIP", 10, ["Combo Pareja", "Chocolate"])
comida7 = Comida("Express", 15, ["Refresco", "Agua"])
comida8 = Comida("Dulcería", 25, ["Chocolate", "Palomitas"])
comida9 = Comida("Bebidas", 35, ["Refresco", "Agua"])
comida10 = Comida("Promociones", 45, ["Combo Pareja", "Cubeta Promocional"])
zonas = [comida1, comida2, comida3, comida4, comida5, comida6, comida7, comida8, comida9, comida10]

# 10 peliculas
peli1=Pelicula("Barbie", 120, "Animación", "A")
peli2=Pelicula("Oppenheimer", 180, "Drama", "B")
peli3=Pelicula("Spiderman: Across the Spider-Verse", 140, "Animación", "A")
peli4=Pelicula("John Wick 4", 130, "Acción", "B")
peli5=Pelicula("The Marvels", 110, "Superhéroes", "A")
peli6=Pelicula("The Hunger Games: The Ballad of Songbirds & Snakes", 150, "Aventura", "B")
peli7=Pelicula("Dune: Part Two", 160, "Ciencia Ficción", "B")
peli8=Pelicula("Wonka", 100, "Fantasía", "A")
peli9=Pelicula("The Flash", 130, "Superhéroes", "B")
peli10=Pelicula("Killers of the Flower Moon", 140, "Crimen", "B")
peliculas = [peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10]

# 10 funciones
f1 = Funcion(peli1, sala3, "10:00", 150.0)
f2 = Funcion(peli2, sala2, "12:30", 120.0)
f3 = Funcion(peli3, sala1, "14:00", 90.0)
f4 = Funcion(peli4, sala6, "16:00", 160.0)
f5 = Funcion(peli5, sala4, "18:30", 110.0)
f6 = Funcion(peli6, sala5, "20:00", 130.0)
f7 = Funcion(peli7, sala8, "21:30", 140.0)
f8 = Funcion(peli8, sala7, "22:00", 125.0)
f9 = Funcion(peli9, sala10, "17:00", 135.0)
f10 = Funcion(peli10, sala9, "11:00", 95.0)
funciones = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

# 10 promociones
prom1=Promocion("Promo VIP", "20% de descuento para clientes VIP", 20, date(2026, 12, 31))
prom2=Promocion("Descuento Estudiante", "15% de descuento para estudiantes con ID válido", 15, date(2025, 6, 30))
prom3=Promocion("Combo Familiar", "10% de descuento al comprar 4 boletos y 2 combos", 10, date(2025, 12, 31))
prom4=Promocion("Martes de Cine", "25% de descuento en funciones de martes", 25, date(2025, 12, 31))
prom5=Promocion("Descuento Senior", "30% de descuento para personas mayores de 60 años", 30, date(2025, 12, 31))
prom6=Promocion("Promo 3D", "15% de descuento en funciones 3D", 15, date(2025, 12, 31))
prom7=Promocion("Descuento Matutino", "20% de descuento en funciones antes de las 12:00 PM", 20, date(2025, 12, 31))
prom8=Promocion("Combo Pareja", "10% de descuento al comprar 2 boletos y 1 combo", 10, date(2025, 12, 31))
prom9=Promocion("Descuento Nocturno", "15% de descuento en funciones después de las 8:00 PM", 15, date(2025, 12, 31))
prom10=Promocion("Promo Estreno", "20% de descuento en la primera semana de estreno", 20, date(2025, 12, 31))
promociones = [prom1, prom2, prom3, prom4, prom5, prom6, prom7, prom8, prom9, prom10]

#Menu
def mostrar_usuarios():
    print("REGISTRO DE USUARIOS")
    for i in usuarios:
        i.login()
        i.promociones()
        print()

def mostrar_empleados():
    print("REGISTRO DE EMPLEADOS")
    for e in empleados:
        e.login()
        e.marcar_entrada()
        e.gestionar_funciones()
        print()

def mostrar_salas():
    print("REGISTRO DE 10 SALAS")
    for s in salas:
        s.que_sala_es()
        s.disponibilidad()
        s.limpiar()
        print()

def mostrar_zonas():
    print("REGISTRO DE ZONAS DE COMIDA")
    for c in zonas:
        c.disponibilidad()
        c.vender_producto(c.productos[0])
        c.actualizar_sttock(c.stock + 10)
        print()

def mostrar_peliculas():
    print("REGISTRO DE PELICULAS")
    for p in peliculas:
        p.reseña()
        p.clasificacion_edad()
        print()

def mostrar_funciones():
    print("REGISTRO DE 10 FUNCIONES")
    for f in funciones:
        f.detalles_funcion()
        f.lugares_disponibles()
        print()

def mostrar_promociones():
    print("REGISTRO DE PROMOCIONES")
    for q in promociones:
        q.es_valida()
        q.aplicar_descuento(500)
        print()

def hacer_reserva():
    print("INICIANDO ROCESO DE RESERVA")

    print("Usuarios disponibles:")
    for i, u in enumerate(usuarios):
        print(f"  {i+1}. {u.name}  Saldo: ${u.dinero}  Puntos: {u.puntos}")
    idx_u = int(input("Selecciona un usuario (número): ")) - 1
    u = usuarios[idx_u]

    print("Funciones dispnibles:")
    for i, f in enumerate(funciones):
        print(f"  {i+1}. {f.pelicula.titulo} | {f.sala.lugar} ({f.sala.tipo}) | {f.horario} | ${f.precio}")
    a = int(input("Seleciona una funcion (número): ")) - 1
    f = funciones[a]

    asientos_str = input("Ingresa los asientos separados por coma (ej: A1,A2,B3): ")
    asientos = [a.strip().upper() for a in asientos_str.split(",") if a.strip()]

    print(f"\nUsuario: {u.name} (Puntos: {u.puntos})")
    print(f"Pelicula: '{f.pelicula.titulo}' | Sala: {f.sala.lugar} ({f.sala.tipo})")
    print(f"Seleccione sus asientos: {asientos}\n")

    r = Reserva(u, f, asientos)

    print("\nPromociones dispnibles:")
    print("  0. Sin promocion")
    for i, pr in enumerate(promociones):
        print(f"  {i+1}. {pr.codigo} - {pr.descuento}% | {pr.descripcion}")
    a = int(input("Selecciona una promoción (0 para ninguna): "))

    if a != 0:
        promo = promociones[a - 1]
        print(f"\n>>> APLICANDO GESTIÓN COMERCIAL...")
        print(f"Codigo: {promo.codigo}")
        r.aplicar_descuento(promo)

    print(f"Monto base: ${r.total:.2f}")
    r.confirmar_pago()
    print()
    r.generar_ticket()
#Panel de empleado (admin)
def panel_empleado():
    print("PANEL DE EMPLEADO")
    print("Administradores disponibles:")
    admins = [e for e in empleados if isinstance(e, Administrador)]
    for i, a in enumerate(admins):
        print(f"  {i+1}. {a.name} | Privilegios: {a.privilegios}")
    a = int(input("Selecciona un administrador: ")) - 1
    admin = admins[a]
    admin.login()
    admin.gestionar_funciones()

    print("¿Qué deseas hacer?")
    print("  1. Agregar película")
    print("  2. Ver funciones")
    op = input("Opción: ")
#IF para agregar película o ver funciones
    if op == "1":
        titulo = input("Título de la película: ")
        duracion = int(input("Duración en minutos: "))
        genero = input("Género: ")
        clasificacion = input("Clasificación (A/B/C): ").upper()
        nueva = Pelicula(titulo, duracion, genero, clasificacion)
        admin.agregar_pelicula(peliculas, nueva)
        nueva.reseña()
    elif op == "2":
        mostrar_funciones()

menu()

