Garaje = ["Pintura", "Ventanas", "Ruedas", "Carroceria"]
#STOCK
Ruedas = ["Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"]
Ruedas[0] = {"existencias": 15, "precio": 100}
Ruedas[1] = {"existencias": 15, "precio": 150}
Ruedas[2] = {"existencias": 15, "precio": 200}
Ruedas[3] = {"existencias": 15, "precio": 250}

Ventanas = ["Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"]
Ventanas[0] = {"existencias": 10, "precio": 100}
Ventanas[1] = {"existencias": 10, "precio": 115}
Ventanas[2] = {"existencias": 10, "precio": 175}
Ventanas[3] = {"existencias": 10, "precio": 200}

Pintura = ["Color 1", "Color 2", "Color 3", "Color 4"]
Pintura[0] = {"existencias": 13, "precio": 100}
Pintura[1] = {"existencias": 13, "precio": 120}
Pintura[2] = {"existencias": 13, "precio": 150}
Pintura[3] = {"existencias": 13, "precio": 250}

Carroceria = ["Tipo 1", "Tipo 2", "Tipo 3", "Tipo 4"]
Carroceria[0] = {"existencias": 12, "precio": 130}
Carroceria[1] = {"existencias": 12, "precio": 170}
Carroceria[2] = {"existencias": 12, "precio": 200}
Carroceria[3] = {"existencias": 12, "precio": 250}

CAT = {"Pintura": Pintura, "Ventanas": Ventanas, "Ruedas": Ruedas, "Carroceria": Carroceria}
pedido = []

while True:
    for c in Garaje: print(c, CAT[c])
    cat = input("Categoria (fin): ")
    if cat == "fin": break
    if cat not in CAT: print("No valida."); continue
    tipo = input("Tipo: ")
    if tipo not in CAT[cat]: print("No valido."); continue
    i = CAT[cat].index(tipo)
    n = int(input("Cantidad: "))
    if n <= 0 or n > CAT[cat][i]["existencias"]: print("Stock insuficiente."); continue
    CAT[cat][i]["existencias"] -= n
    pedido.append([n, cat, CAT[cat][i]["precio"]])

def fila(nombre):
    return [[p[0], p[2]] for p in pedido if p[1] == nombre]
#CLAS
x, y, z = fila("Ruedas"), fila("Ventanas"), fila("Carroceria")
M = [x, y, z]

#Suma
cr = sum(c * pr for c, pr in x)
cv = sum(c * pr for c, pr in y)
cc = sum(c * pr for c, pr in z)
cp = sum(p[0] * p[2] for p in pedido if p[1] == "Pintura")

for p in pedido: print(p[0], "x", p[1], "=", p[0] * p[2], "EUR")
for f in M: print(f)
print("Coste ruedas:", cr)
print("Coste ventanas:", cv)
print("Coste carrocerias:", cc)
print("Coste pintura:", cp)
print("TOTAL:", cr + cv + cc + cp)
TOTAL = cr + cv + cc + cp

def generate_TAX(cr,cv,cc,cp):
    if TOTAL > 1000:
        return False
    if cr+cc > cv+cp:
        TAX =TOTAL+cv+cp//100
    if cr+cc < cv+cp:
        TAX = TOTAL+cr+cc//100
        return TAX
def generate_quota():
    Quota=Quota

def ganancias():
    Winnings = cr + cv + cc + cp + 1000
    RR_Winnings = Winnings*generate_TAX/4
    if RR_Winnings >= Quota:
        print("we survive")
    else:
        print("we ded")
