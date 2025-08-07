data1 = list(map(int, input("Digite a primeira data: ").split()))
data2 = list(map(int, input("Digite a segunda data: ").split()))

def data_recente(data1, data2):
    if data1[2] > data2[2]:
        return data1
    elif data1[2] < data2[2]:
        return data2
    else:
        if data1[1] > data2[1]:
            return data1
        elif data1[1] < data2[1]:
            return data2
        else:
            if data1[0] > data2[0]:
                return data1
            elif data1[0] < data2[0]:
                return data2
            else:
                return None  # datas iguais

recente = data_recente(data1, data2)
if recente:
    print(f"A data mais recente é: {recente[0]} {recente[1]} {recente[2]}")
else:
    print("As datas são iguais.")
    
   
    
    
    
    
