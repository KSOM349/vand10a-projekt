import random
import os
from kort import skapa_kortlek, Kort
from spelare import Spelare

class Vänd10aSpel:
    def __init__(self, spelare_namn):
        self.kortlek = skapa_kortlek()
        self.spelare = [Spelare(namn) for namn in spelare_namn]
        self.hög = []
        self.tur_index = 0
        self.riktning = 1
    
    def starta_spel(self):
        random.shuffle(self.kortlek)
        
        for spelare in self.spelare:
            for _ in range(3):
                if self.kortlek:
                    spelare.hand.append(self.kortlek.pop())
            
            for _ in range(3):
                if self.kortlek:
                    spelare.uppvända_kort.append(self.kortlek.pop())
            
            for _ in range(3):
                if self.kortlek:
                    spelare.nedvända_kort.append(self.kortlek.pop())
        
        if self.kortlek:
            self.hög.append(self.kortlek.pop())
    
    def rensa_skärm(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def visa_spelmeny(self, spelare):
        print("\n🎴 VÄND 10A - Välj alternativ:")
        print("[1] Spela kort")
        print("[2] Visa hand")
        print("[3] Visa spelstatus")
        print("[4] Avsluta tur")
    
    def välj_kort_interaktivt(self, spelare):
        while True:
            print("\nDina kort:")
            for i, kort in enumerate(spelare.hand):
                print(f"  [{i}] {kort}")
            
            val = input("Välj kort (0-{}): ".format(len(spelare.hand)-1))
            
            try:
                val_index = int(val)
                if 0 <= val_index < len(spelare.hand):
                    return val_index
                else:
                    print("Ogiltigt val! Välj mellan 0-{}".format(len(spelare.hand)-1))
            except ValueError:
                print("Ogiltigt val! Ange en siffra.")
    
    def visa_spelstatus(self):
        print("\n📊 SPELSTATUS:")
        print(f"Riktning: {'⏩ Framåt' if self.riktning == 1 else '⏪ Bakåt'}")
        print(f"Kort kvar i lek: {len(self.kortlek)}")
        print(f"Kort på högen: {len(self.hög)}")
        print("Toppkort:", self.hög[-1] if self.hög else "Inget")
        
        print("\n👥 Spelare:")
        for spelare in self.spelare:
            print(f"  {spelare.namn}: {len(spelare.hand)} kort på hand, {len(spelare.uppvända_kort)} uppvända, {len(spelare.nedvända_kort)} nedvända")
    
    def spelarens_tur(self, spelare_index):
        spelare = self.spelare[spelare_index]
        
        self.rensa_skärm()
        print(f"=== {spelare.namn}s tur ===")
        print(f"Toppkort på högen: {self.hög[-1] if self.hög else 'Inget'}")
        
        while True:
            self.visa_spelmeny(spelare)
            val = input("\nVälj alternativ (1-4): ")
            
            if val == "1":
                if not spelare.hand:
                    print("Inga kort på handen att spela!")
                    continue
                
                kort_index = self.välj_kort_interaktivt(spelare)
                valt_kort = spelare.spela_kort(kort_index)
                
                if valt_kort and self.är_giltigt_drag(valt_kort):
                    print(f"Du spelar: {valt_kort}")
                    self.hög.append(valt_kort)
                    self.applícera_speciella_effekter(valt_kort)
                    return True  # تم لعب كرت بنجاح
                else:
                    print("Ogiltigt drag! Försök igen.")
                    spelare.ta_kort(valt_kort)
            
            elif val == "2":
                print(f"\nDin hand: {spelare.visa_hand()}")
            
            elif val == "3":
                self.visa_spelstatus()
            
            elif val == "4":
                print("Avslutar tur...")
                return False  # إنهاء الدور بدون لعب كرت
            
            else:
                print("Ogiltigt val! Försök igen.")
    
    def är_giltigt_drag(self, kort):
        if not self.hög:
            return True
        
        topp_kort = self.hög[-1]
        return kort.kan_läggas_på(topp_kort)
    
    def applícera_speciella_effekter(self, kort):
        if kort.valör == '8':
            self.riktning *= -1
            print("🔄 Riktningen ändras!")
        elif kort.valör == '10':
            self.hög = []
            print("💥 Högen vänds bort!")
    
    def vinnare(self):
        for spelare in self.spelare:
            if not spelare.hand and not spelare.uppvända_kort and not spelare.nedvända_kort:
                return spelare
        return None
    
    def kör_spel(self):
        """الدورة الرئيسية للعبة - الإصدار المصحح"""
        self.starta_spel()
        
        while not self.vinnare():
            # لعب دور اللاعب الحالي
            self.spelarens_tur(self.tur_index)
            
            # التحقق إذا كان هناك فائز
            if self.vinnare():
                break
            
            # الانتقال للاعب التالي
            input("\nTryck Enter för nästa spelare...")
            self.tur_index = (self.tur_index + self.riktning) % len(self.spelare)
        
        # إعلان الفائز
        vinnare = self.vinnare()
        print(f"\n🎉 {vinnare.namn} vinner spelet!")

if __name__ == "__main__":
    test_spel = Vänd10aSpel(["Test1", "Test2"])
    test_spel.starta_spel()
    print("Spel startat med 2 testspelare!")
