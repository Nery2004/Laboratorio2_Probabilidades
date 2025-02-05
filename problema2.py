#Laboratorio 2
#Mario Rocha 23501
#Kevin Villagran 23584
#Jonathan Zacarias 231104
#Luis Pedro Lira 23669
#Carlos Alburez 231311
#Nery Molina 23218

def main():
    pu = [1/3, 1/3, 1/3]
    pl_u = [1/2, 2/5, 1/3]
    pt_lyu = [2/3, 1/2, 2/5]
    p_por_urna = [pu[i] * pl_u[i] * pt_lyu[i] for i in range(3)]
    p_total = sum(p_por_urna)
    
    # a) Se extrae una dona al azar, ¿cuál es la probabilidad de que sea de limón y en forma de toro?
    print("a) La probabilidad de que la dona sea de limón y en forma de toro es P(L y T) =", p_total)
    
    p_urna0 = p_por_urna[0] / p_total
    p_urna1 = p_por_urna[1] / p_total
    p_urna2 = p_por_urna[2] / p_total
    
    # b) Se extrae una dona al azar y salió que es de limón y en forma de toro. ¿Cuál es la probabilidad de que provenga de la urna 2?
    print("b) Dado que la dona es de limón y en forma de toro, la probabilidad de que provenga de la urna 2 es P(U=2 | L y T) =", p_urna2)
    
    # c) Se extrae una dona al azar y salió que es de limón y en forma de toro. ¿Cuál es la probabilidad de que provenga de la urna 1?
    print("c) Dado que la dona es de limón y en forma de toro, la probabilidad de que provenga de la urna 1 es P(U=1 | L y T) =", p_urna1)
    
    # d) Se extrae una dona al azar y salió que es de limón y en forma de toro. ¿Cuál es la probabilidad de que provenga de la urna 0?
    print("d) Dado que la dona es de limón y en forma de toro, la probabilidad de que provenga de la urna 0 es P(U=0 | L y T) =", p_urna0)

if __name__ == "__main__":
    main()
