# etela'at koli:
list_nomarat = {'farsi': 17, 'riazi': 20, 'oloom': 19, 'ejtemaei': 20, 'dini': 17}   # list (dict) kol nomarat va doroos
nomarat = list_nomarat.values() # list (dict) nomarat
list_nomreha = [] #list (list) nomarat

# tabdil dictionery be list
for i in nomarat:
    list_nomreha.append(i) #afzoodan ajzaye dict nomarat e list nomre ha
list_nomreha.sort()  # morattab kardan list az koochak be bozorg

# bazgasht be vaziat
def back_vaziat():
    print('------------------------------') 
    print('1.bazgash be vaz\'iat')
    print('2.bazgash be menoye asli')
    g = int(input('-> ')) #daryaft gozineye mored nazare karbar
    #ejra kardan gozineye entekhab shode
    if g == 1:
        vaziat()
    elif g == 2:
        kol()
    else: #baraye gozine hayi ke ta'rif nashode and
        namotabar()

# bazgasht be  taghir
def back_taghir():
    print('------------------------------')
    print('1.bazgash be taghir')
    print('2.bazgash be menoye asli')
    g = int(input('-> ')) #daryaft gozineye mored nazar
    #ejraye dastoor entekhab shode
    if g == 1:
        taghirat()
    elif g == 2:
        kol()
    else:
        namotabar()

# liste kamele nomarat
def list_kamel_nomarat():
    print('______________________________')
    for i in list_nomarat: #entekhab kardan yeki az nomarat dar list(dict) nomarat
        nomre = list_nomarat[i] #entekhab nomreye dars marboote
        print('{:9s}: '.format(i), nomre) #print kardan anha ba nazm va tartib
    miangin() #seda zadan function miangin
    back_vaziat() #ezafe kardan gozineye bargasht be menoye asli va vaz'iat

# miangin nomarat
def miangin():
    tedad = len(nomarat) #tedad kol nomarat #be dast avardan tedade kole nomarat
    kol_nomarat = 0  # jam' kol nomarat
    for i in nomarat:
        kol_nomarat = kol_nomarat + i #hesab kardan majmoo' nomarat
    miangin = kol_nomarat / tedad  #be dast avardan miangin
    print('{:9s}:  {}'.format('miangin', miangin)) #print kardan miangin ba formati hamahang ba nomarat


# neshan dadan balatarin nomre ha va darseshan
def balatarin_nomre():
    print('______________________________')
    b_nomre = list_nomreha[-1] #peya kardan balatarin nomreye mojood be vasileye list(list)nomarat
    print('balatrin doroos va nomarat shoma:')
    for i in list_nomarat: #entekhab yek dars az list(dict) nomarat kol
        if list_nomarat[i] >= b_nomre: #agar nomreye darsi ke entekhab shode ba balatarin  nomre barabar bood anra print kon
            b_dars = i # darsi ke darhal barresi ast ra be onvan balatarin dars zakhire mikonad
            b_nomre = list_nomarat[b_dars] # az list(dict) kol nomarat nomreye balatarin dars ra peyda va an ra be onvan balatarin nomre zakhire mikonad
            print('{:9} : {}'.format(b_dars, b_nomre)) #an ra besoorat monazam chap mikonad
    back_vaziat()# gozine haye bargasht be menoye vaz'iat ra namayesh midahad

# neshan dadn payin tarin nomre ha va darseshan
def payintarin_nomre():
    print('______________________________')
    p_nomre = list_nomreha[0] #entekhab kardan payintarin nomre mojood dar list(list)nomreha
    print('balatrin doroos va nomarat shoma:')
    for i in list_nomarat:
        if list_nomarat[i] == p_nomre:
            p_dars = i #zakhire kardan dars fe'li be onvan
            print('{:9s} : {}'.format(p_dars, p_nomre))
    back_vaziat()

# namayesh tedad yek nomre va darsad an
def tedad_darsad():
    print('______________________________')
    tedad = len(nomarat)  # tedad kol nomarat
    for i in range(1, 21):
        t = list_nomreha.count(i)
        darsad = (t / tedad) * 100
        if t != 0:
            print('{:<2d} ta {:2d} dari, {:3.2f}% kol nomre hat'.format(t, i, darsad))
    back_vaziat()

# afzoodan yek nomre
def add():
    print('______________________________')
    nam_dars = input('{:8s}dars ra vared konid : '.format('naam'))
    nomre_dars = int(input('{:8s}dars ra vared konid : '.format('nomreye')))
    if nomre_dars>20:
        print('nomre ye vared shode as saghf nomarat balatar ast')
        add()
    list_nomarat[nam_dars] = nomre_dars
    print('dars', nam_dars, 'ba nomreye', nomre_dars, 'afzoode shod')
    back_taghir()

# hazf yek nomre
def delete():
    print('______________________________')
    nam_dars = input('nam dars ra vared konid: ')
    nomre_dars = list_nomarat[nam_dars]
    print ('aya motma\'enid mikhahid dars "', nam_dars, '"ra ba nomre ye "', nomre_dars, '"ra pak konid?')
    print('1.yes\n2.no')
    g2_2_1 = int (input('-> '))
    if g2_2_1==1:
        del list_nomarat[nam_dars]
    khorooji = 'dars  "{}"  ba nomreye  "{}"  as list nomarat hazf shod'
    print(khorooji.format(nam_dars, nomre_dars))
    back_taghir()

# pak kardan tamam nomarat
def clear():
    print('______________________________')
    print('aya motma\'enid mikhahid kol doroos ra pak konid?')
    print('1.yes\n2.no')
    g2_2_2 = int(input('-> '))
    if g2_2_2 == 1:
        list_nomarat.clear()
        print('tamam nomarat hazf shod')
    back_taghir()

# gozineye namo'tabar
def namotabar():
    print('______________________________')
    print ('adad vared shode mo\'tabar nist')

#vaz'iat
def vaziat():
    print('______________________________')
    print('1.list kamel nomarat')
    print('2.balatarin doroos')
    print('3.payintarin doroos')
    print('4.tedad doros ba yek nomre')
    print('5.bazgasht be menoye asli')
    g1 = int(input('-> ')) # gozine ye mored nazar, vaz'iat nomarat
    if g1==1:
        list_kamel_nomarat()
        miangin()
    elif g1==2:
        balatarin_nomre()
    elif g1==3:
        payintarin_nomre()
    elif g1==4:
        tedad_darsad()
    elif g1==5:
        kol()
    else:
        namotabar()

#taghirat
def taghirat():
    print('______________________________')
    print('1.afzoodan')
    print('2.hazf')
    print('3.bazgasht be menoye asli')
    g = int(input('-> '))
    if g == 1:
        add()
    elif g == 2:
        delete()
    elif g == 3:
        kol()
    else:
        namotabar()

#kol
def kol():
    print('______________________________')
    print('yek gozineh ra entekhab konid')
    print('1.vaziat nomarat')
    print('2.taghir nomarat')
    g = int(input('-> '))  # gozine ye mored nazar, menoye asli
    if g == 1:
        vaziat()
    elif g == 2:
        taghirat()
    else:
        namotabar()
        kol()

try:
    while True:
        kol()
except ValueError:
    print('harf ersali na mo\'tabar')
    kol()