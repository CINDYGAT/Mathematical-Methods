import math
import matplotlib.pyplot as plt

# Funcion para calcular la distancia y velocidad en X y Y
def proyectil(V0, theta, B, g, dt, Xtot):
    x = 0   # condicion inicial de x
    y= 0    # condicion inicial de y
    t = 0   # condicion inicial del tiempo
    vx = V0 * math.cos(theta)  # Velocidad en el eje x
    vy = V0 * math.sin(theta)   # Velocidad inicial en y
    X = []  # Lista para la distancia en x
    Y = []  # Lista para la distancia en y
    T = []  # Lista para el tiempo
    V_x = []  # Lista para la velocidad en x
    V_y = []    # Lista para la velocidad en y

    for i in range(Xtot):
        if y < 0:
            break  # Detiene el ciclo si el objeto ha caido al suelo
#Adicion de los elementos a las listas de distancias y velocidades
        V_x.append(vx) 
        V_y.append(vy)
        X.append(x)
        Y.append(y)
        T.append(t)
        t += dt
        v = math.sqrt(vx**2 + vy**2)  # Velocidad resultante
        vx -= B * v * vx * dt
        vy -= (g + (B * v * vy)) * dt  # Actualización de la velocidad en y
        x += vx * dt  # Actualización x
        y += vy * dt  # Actualización  y
    return T, X, Y, V_x , V_y ,x

# Indicando valores constantes
V0 = 700
theta = math.pi / 6
dt = 0.01
Xtot = 10**5
B = 0.00004
g = 9.8


#Adicionando valores constantes a la funcion dis_xy y obteniendo los valores de las listas
sol_xy = proyectil(V0, theta, B, g, dt, Xtot)
T = sol_xy[0]
X = sol_xy[1]
Y = sol_xy[2]
V_x = sol_xy[3]
V_y = sol_xy[4]


#Creacion de los plots anidados en una sola figura

figure, axis = plt.subplots(2, 2, figsize=(12, 11))   
# Para la figura de la posicion en x 
axis[0, 0].plot(T, X, 'tab:orange') 
axis[0, 0].set_title("Distancia en X vs Tiempo") 
axis[0, 0].set_ylabel('Distancia en X (m)')
# Figura de la posicion en Y 
axis[1, 0].plot(T, Y , 'tab:green') 
axis[1, 0].set_title("Distancia en Y vs Tiempo")   
axis[1, 0].set_xlabel('Tiempo (s)') 
axis[1, 0].set_ylabel('Distancia en X (m)')
axis[1, 0].sharex(axis[0, 0])
# Figura para la velocidad en x
axis[0, 1].plot(T, V_x, 'tab:red') 
axis[0, 1].set_title("Velocidad en X vs Tiempo") 
axis[0, 1].set_ylabel('Distancia en X (m)') 
# Figura para la velocidad en y
axis[1, 1].plot(T, V_y) 
axis[1, 1].set_title("Velocidad en Y vs Tiempo") 
axis[1, 1].set_xlabel('Tiempo (s)') 
axis[1, 1].set_ylabel('Distancia en X (m)')

plt.show()


#Trayectoria del proyectil con y sin resistencia del aire
#Con resistencia del aire
trayectoria_RA = proyectil(V0, theta, B, g, dt, Xtot) 
X_RA = trayectoria_RA[1]
Y_RA = trayectoria_RA[2]

#Sin resistencia del aire
trayectoria_SRA = proyectil(V0, theta, 0, g, dt, Xtot) 
X_SRA = trayectoria_SRA[1]
Y_SRA = trayectoria_SRA[2]

#intentando plotear juntas las distancias
plt.plot(X_RA, Y_RA , color= "r", label= "Con resistencia")
plt.plot(X_SRA, Y_SRA, color= "g", label= "Sin resistencia")
plt.xlabel('Distancia en Y (m)')
plt.ylabel('Distancia en X (m)')
plt.title('Trayectoria del proyectil con y sin resistencia del aire')
plt.legend() #para diferenciar cada curva
plt.grid()
plt.show()

#aqui debemos agregar la interpretacion de la grafica!


##########INCISO 4###########
thetas = []
alcances_x = []
alcances_y = []
thetas = []
alcances_x = []
alcances_y = []

for angulo in range(0,91,15):
        theta = math.radians(angulo)
        T, X, Y, V_x , V_y, x = proyectil(V0, theta, 0, g, dt, Xtot)
        thetas.append(angulo)
        alcances_x.append(x)
        plt.plot(X, Y, label=f'{angulo} grados')

plt.xlabel('Distancia en X (m)')
plt.ylabel('Distancia en Y (m)')
plt.title('Trayectoria del Proyectil para Diferentes Ángulos de Lanzamiento')
plt.legend()
plt.grid()
plt.show()

    # Encontrar el ángulo que produce el alcance máximo
max_alcance = max(alcances_x)
max_theta = thetas[alcances_x.index(max_alcance)]

# Imprimir el ángulo con el alcance máximo
print(f'El ángulo que produce el alcance máximo sin resistencia al aire es: {max_theta} grados')


##########INCISO 5###########

thetasB = []
alcancesB_x = []
alcancesB_y = []

plt.figure(figsize=(11, 7)) #ajustar el tamaño de la grafica

for anguloB in range(0,91,5):
        theta = math.radians(anguloB)
        T, X, Y, V_x , V_y, x = proyectil(V0, theta, B, g, dt, Xtot)
        thetasB.append(anguloB)
        alcancesB_x.append(x)
        plt.plot(X, Y, label=f'{anguloB} grados')

plt.xlabel('Distancia en X (m)')
plt.ylabel('Distancia en Y (m)')
plt.title('Trayectoria del Proyectil para Diferentes Ángulos de Lanzamiento')
plt.legend()
plt.grid()
plt.show()

    # Encontrar el ángulo que produce el alcance máximo
max_alcanceB = max(alcancesB_x)
max_thetaB = thetasB[alcancesB_x.index(max_alcanceB)]

# Imprimir el ángulo con el alcance máximo
print(f'El ángulo que produce el alcance máximo con resistencia al aire es: {max_thetaB} grados')
