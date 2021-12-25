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
        Pizzahupe.off()
        
        # Halten
        OstampelROT.on()
        OstampelGELB.off()
        OstampelGRÜN.off() 
        
        Zeit.sleep(3)
        
        # Bereitmachen
        OstampelROT.on()
        OstampelGELB.on()
        OstampelGRÜN.off()
        
        Zeit.sleep(2)
        
        # Fahren
        OstampelROT.off()
        OstampelGELB.off()
        OstampelGRÜN.on()
        
        Zeit.sleep(3)
        
        # Bremsen
        OstampelROT.off()
        OstampelGELB.on()
        OstampelGRÜN.off()
        
        Zeit.sleep(2)
               
        

# Beim Unterbrechen des Programmes sollen 
# die folgenden Befehle ausgeführt werden
except KeyboardInterrupt:
    Pizzahupe.off()
    Ampel.closeGPIO()
    
    
 
