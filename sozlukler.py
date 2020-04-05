#bir karşılığı olan tanımlar için kullanılır
karakter1={"ad":"A",
        "guc":500,
        "silah":"kılıç",
        "can":4000}

"""print("karakterin adi : {}".format(karakter1["ad"]))
print("karakterin gucu : {}".format(karakter1["guc"]))
print("karakterin silahi : {}".format(karakter1["silah"]))"""

karakter2={"ad":"B",
        "guc":700,
        "silah":"kılıç",
        "can":7000}
def vur(vuran:dict,vurulan:dict):
    vurulan["can"]=vurulan["can"]-vuran["guc"]

vur(karakter1,karakter2)
vur(karakter2,karakter1)

print("karakter 2 vurulduğunda kalan canı: ",karakter2["can"])
print("karakter 1 vurulduğunda kalan canı: ",karakter1["can"])

