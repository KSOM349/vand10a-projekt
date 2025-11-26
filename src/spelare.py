class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.hand = []          # الكروت في يد اللاعب
        self.uppvända_kort = [] # الكروت المكشوفة
        self.nedvända_kort = [] # الكروت المخفية
    
    def ta_kort(self, kort):
        """أخذ كرت جديد وإضافته ليد اللاعب"""
        self.hand.append(kort)
    
    def spela_kort(self, kort_index):
        """لعب كرت من يد اللاعب"""
        if 0 <= kort_index < len(self.hand):
            return self.hand.pop(kort_index)
        return None
    
    def visa_hand(self):
        """عرض كروت يد اللاعب"""
        return [str(kort) for kort in self.hand]
    
    def __str__(self):
        """عرض معلومات اللاعب"""
        return f"{self.namn} (Hand: {len(self.hand)}, Uppvända: {len(self.uppvända_kort)}, Nedvända: {len(self.nedvända_kort)})"

# اختبار الملف
if __name__ == "__main__":
    spelare = Spelare("TestSpelare")
    print(f"Spelare skapad: {spelare}")
