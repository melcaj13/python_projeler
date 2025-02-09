# def sayi(name):
#     '''
#     mkfnlsfmsdkfnnslf       # fonksiyonla ilgili kullanan kişiye açıklama vermek istersek bunu ve help metodunu kullanırız.
#     '''
#     return "hello "+name
# print(help(sayi))    #  helllppppp
# print(sayi("a"))


# def kelime(a,b):
#     for i in range(b):          # print(a*b)  dersen de aynı işi yaparmış off
#         print(a)              # b kadar a yazdıran fonksiyon
# print(kelime(2,7))

# def toList(*params):
#     liste=[]
#     for i in params:
#         liste.append(i)
#     print(liste)    
# print(toList(2,3,6,5,"fgbj"))    

#     print(*params)         # bu yöntem direk yazdırıyo üstteki listeye çevirdi
# print(toList(10,20,30,40,50))   




#def asal(sayi1,sayi2):
#    for sayi in range(sayi1,sayi2+1):
#        if sayi>1:
#            for i in range(2,sayi):
#                if (sayi%i==0):
#                     break
#                 else:
#                     print(sayi)
# print (asal(5,15))


#def bolen(sayi):
#    bolens=[]
#    for i in range(2,sayi):
#        if sayi%i==0:
#            bolens.append(i)
#    return bolens
# print(bolen(20))