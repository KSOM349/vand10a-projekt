from spel_logic import Vänd10aSpel

def huvudmeny():
    """القائمة الرئيسية للعبة"""
    print("🎴 VÄLKOMMEN TILL VÄND 10A! 🎴")
    print("=" * 40)
    print("👥 Spelare: Marcus, Fahad, Ruffin, Kaled, Murgar")
    print("=" * 40)
    
    # بداية اللعبة مع جميع اللاعبين الخمسة
    spel = Vänd10aSpel(["Marcus", "Fahad", "Ruffin", "Kaled", "Murgar"])
    
    # تشغيل اللعبة
    spel.kör_spel()

if __name__ == "__main__":
    huvudmeny()
