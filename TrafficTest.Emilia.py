import PiTraffic as Ampel
import time as Zeit

# Festlegung der Nordampel
NordampelROT = Ampel.Traffic("NORTH", "RED")
NordampelGELB = Ampel.Traffic("NORTH", "YELLOW")
NordampelGRÜN = Ampel.Traffic("NORTH", "GREEN")

# Festlegung der Westtampel
#WestampelROT = Ampel.Traffic("WEST", "RED")
#WestampelGELB = Ampel.Traffic("WEST", "YELLOW")
#WestampelGRÜN = Ampel.Traffic("WEST", "GREEN")


# Festlegung der Ostampel
OstampelROT = Ampel.Traffic("EAST", "RED")
OstampelGELB = Ampel.Traffic("EAST", "YELLOW")
OstampelGRÜN = Ampel.Traffic("EAST", "GREEN")

# Festlegung der Westtampel
WestampelROT = Ampel.Traffic("WEST", "RED")
WestampelGELB = Ampel.Traffic("WEST", "YELLOW")
WestampelGRÜN = Ampel.Traffic("WEST", "GREEN")


# Festlegung der Südampel
Pizzaampelrot = Ampel.Traffic("SOUTH", "RED")

# Festlegung der Piepser
Pizzahupe = Ampel.Buzzer()
 

try:
    # Endlos-Schleife "while True:" wiederholt die 
    # folgenden Befehle immer wieder von oben nach unten
    while True:
        Pizzahupe.off ()
        
        # +++ Phase 1 +++
        
        # Nord und Süd dürfen fahren
        NordampelROT.off()
        NordampelGELB.off()
        NordampelGRÜN.on()
        
        #SüdampelROT.off()
        #SüdampelGELB.off()
        #SüdampelGRÜN.on()
        
        
        # Ost und West müssen anhalten
        OstampelROT.on()
        OstampelGELB.off()
        OstampelGRÜN.off() 
        
        WestampelROT.on()
        WestampelGELB.off()
        WestampelGRÜN.off()
        
        Zeit.sleep(3)
        
        # +++ Phase 2 +++
        
        # Bereitmachen
        OstampelROT.on()
        OstampelGELB.on()
        OstampelGRÜN.off()
        
        WestampelROT.on()
        WestampelGELB.on()
        WestampelGRÜN.off()
        
        Zeit.sleep(2)
        
        # +++ Phase 3 +++
        
        # Fahren
        OstampelROT.off()
        OstampelGELB.off()
        OstampelGRÜN.on()
        
        WestampelROT.off()
        WestampelGELB.off()
        WestampelGRÜN.on()
        
        Zeit.sleep(3)
        
        # +++ Phase 4 +++
        
        # Bremsen
        OstampelROT.off()
        OstampelGELB.on()
        OstampelGRÜN.off()
        
        WestampelROT.off()
        WestampelGELB.on()
        WestampelGRÜN.off()
        
        Zeit.sleep(2)
               
        

# Beim Unterbrechen des Programmes sollen 
# die folgenden Befehle ausgeführt werden
except KeyboardInterrupt:
    Pizzahupe.off()
    Ampel.closeGPIO()
    
    
 
