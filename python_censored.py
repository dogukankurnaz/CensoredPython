def sansur(cumle):
    kelime_list=["merhaba","test","araba","dünya","köpek","bitcoin"]   
    cumleler=cumle.split()
    for i in kelime_list:
        for j in cumleler:
            if i in j:
                a=cumleler.index(j)
                cumleler.remove(j)
                cumleler.insert(a,"*"*len(i))
    print ( " ".join(cumleler))
a=input(str("cumle giriniz: "))
print (sansur(a)) 