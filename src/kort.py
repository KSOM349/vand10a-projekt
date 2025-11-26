class Kort:
    def __init__(self, kort_id, valör, färg, typ):
        self.kort_id = kort_id
        self.valör = valör
        self.färg = färg
        self.typ = typ
    
    def __str__(self):
        return self.kort_id
    
    def kan_läggas_på(self, topp_kort):
        if self.valör in ['2', '3', '10']:
            return True
        elif self.valör == '7':
            return topp_kort.valör <= '7'
        elif self.valör == '8':
            return topp_kort.valör not in ['8', '9', '10', 'J', 'Q', 'K', 'A']
        else:
            return self.valör >= topp_kort.valör

def skapa_kortlek():
    färger = {'H': 'Hjärter', 'R': 'Ruter', 'S': 'Spader', 'K': 'Klöver'}
    valörer = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    kortlek = []
    for färg_kod, färg_namn in färger.items():
        for valör in valörer:
            kort_id = f"{valör}{färg_kod}"
            typ = 'speciell' if valör in ['2', '3', '7', '8', '10'] else 'vanlig'
            kortlek.append(Kort(kort_id, valör, färg_namn, typ))
    
    return kortlek

# اختبار الملف
if __name__ == "__main__":
    lek = skapa_kortlek()
    print(f"Skapade {len(lek)} kort")
    print("Första 5 korten:")
    for i in range(5):
        print(f"  {lek[i]}")
