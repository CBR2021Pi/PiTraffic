import PiTraffic as Ampel
import time as Zeit

# Festlegung der Ostampel
OstampelROT = Ampel.Traffic("EAST", "RED")
OstampelGELB = Ampel.Traffic("EAST", "YELLOW")
OstampelGRÜN = Ampel.Traffic("EAST", "GREEN")

# Festlegung der Südampel
Pizzaampelrot = Ampel.Traffic("SOUTH", "RED")

# Festlegung der Piepser
Pizzahupe = Ampel.Buzzer()

try:
    # Endlos-Schleife "while True:" wiederholt die 
    # folgenden Befehle immer wieder von oben nach unten
    while True:
        
        # alles anschalten
        OstampelROT.on()
        OstampelGELB.on()
        OstampelGRÜN.on()
        Pizzahupe.on()
        Pizzaampelrot.on()
        
        Zeit.sleep(0.2)
        
        OstampelROT.off()
        Pizzahupe.off()
        
        Zeit.sleep(2)
        
        OstampelGELB.off()
                
        Zeit.sleep(2)
        
        OstampelGRÜN.off()
        
        Zeit.sleep(3)
         
        

# Beim Unterbrechen des Programmes sollen 
# die folgenden Befehle ausgeführt werden
except KeyboardInterrupt:
    Pizzahupe.off()
    Ampel.closeGPIO()
    
    
 
