zirhlar={"demir":10,"çelik":20}
karakterler={
    "karakter1":{"silah":"kılıç",
                 "güç":30,
                 "sağlık":100,
                 "zırh":zirhlar["demir"]},

    "karakter2":{"silah":"kılıç",
                 "güç":30,
                 "sağlık":100,
                 "zırh":zirhlar["çelik"]},
}

def vur(saldiran,saldirilan):
    guc=saldiran["güç"]
    saglik=saldirilan["sağlık"]
    zirh=saldirilan["zırh"]
    damage=guc-zirh
    saglik-=damage
    saldirilan["sağlık"]=saglik
print(karakterler["karakter2"]["sağlık"])
vur(karakterler["karakter1"],karakterler["karakter2"])
print(karakterler["karakter2"]["sağlık"])
