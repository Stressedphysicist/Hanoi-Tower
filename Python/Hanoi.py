def towermaker():
    """

    Inicializa una torre de Hanoi con n platos
    """
    n = int(input('Number of Plates: \n'))
    A = [] 
    B = []
    C = []
    hanoisetup = range(1,n+1)
    for number in hanoisetup:
        A.insert(0,number)
    return len(A),A,B,C

def rmove(n,source,target,auxiliary, count = []):
    """

    Basado en el codigo de la implementacion recursiva hallada en Wikipedia.com.
    Cuenta con el paso-a-paso dado por el codigo original y agrega un contador de pasos
    que permite demostrar que el numero minimo de pasos es 2^n - 1
    """
    if n > 0:
        # Mueve n-1 discos desde el origen al auxiliar, asi estan fuera del camino
        rmove(n-1,source,auxiliary,target,count)
        # Mueve el n-esimo disco del origen al objetivo
        target.append(source.pop())
        # Muestra el Proceso
        count.append(1)
        print("Step: " + str(len(count)))
        print(A,B,C,'============', sep='\n')
        # Mueve el n-1 disco que dejamos en el auxiliar al objetivo
        rmove(n-1,auxiliary,target,source,count)

# Inicia el llamado del origen A al objetivo C con el auxiliar B

n, A, B, C = towermaker()
rmove(n,A,C,B)

