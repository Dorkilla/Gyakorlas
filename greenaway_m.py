import greenaway_o


def beolvas():
    lista=[]
    beFajl = open("greenaway.txt", "r", encoding="utf-8")
    #első sor
    beFajl.readline()
    #többi sor
    sorok = beFajl.readlines()

    for index in range(0,len(sorok),1):
        tisztitottSor= sorok[index].strip()
        #print(tisztitottSor)
        daraboltSor = tisztitottSor.split("-")
        #print(daraboltSor)
        konyvem=greenaway_o.Film(daraboltSor[0], daraboltSor[1])
        #print(konyvem)
        lista.append(konyvem)
    #print(lista)

    return lista

def kiir(lista):
    for index in range(0,len(lista),1):
        print(lista[index])

def filmekszama(lista):
    print("III/b.")
    print(f"\t A filmek száma: {len(lista)}")

def d(lista):
    print("III/b.")
    talalat= True
    index = 0
    while index < len(lista) or talalat:
        # eldöntés tétele
        if "szakács" in lista[index].cim.lower():
            talalat= False
        index += 1
    if not talalat:
        print("\t Van olyan film, amiben szerepel a \"szakács\" szó")
    else:
        print("\t Nincs olyan film, amiben szerepel a \"szakács\" szó")











