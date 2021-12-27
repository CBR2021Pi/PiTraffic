import PiTraffic as Ampel
import time as Zeit

KURZEPHASE = 2
LANGEPHASE = 4

# Festlegung der Nordampel
NordampelROT = Ampel.Traffic("NORTH", "RED")
NordampelGELB = Ampel.Traffic("NORTH", "YELLOW")
NordampelGRÜN = Ampel.Traffic("NORTH", "GREEN")

# Festlegung der Südtampel
SüdampelROT = Ampel.Traffic("SOUTH", "RED")
SüdampelGELB = Ampel.Traffic("SOUTH", "YELLOW")
SüdampelGRÜN = Ampel.Traffic("SOUTH", "GREEN")

# Festlegung der Ostampel
OstampelROT = Ampel.Traffic("EAST", "RED")
OstampelGELB = Ampel.Traffic("EAST", "YELLOW")
OstampelGRÜN = Ampel.Traffic("EAST", "GREEN")

# Festlegung der Westtampel
WestampelROT = Ampel.Traffic("WEST", "RED")
WestampelGELB = Ampel.Traffic("WEST", "YELLOW")
WestampelGRÜN = Ampel.Traffic("WEST", "GREEN")

# Festlegung der Piepser
Pizzahupe = Ampel.Buzzer()
 

try:
    # Endlos-Schleife "while True:" wiederholt die 
    # folgenden Befehle immer wieder von oben nach unten
    while True:
        Pizzahupe.off ()
        
        # +++++++++++++++
        # +++ Phase 1 +++
        # +++++++++++++++
        
        # Nord und Süd dürfen fahren
        NordampelROT.off()
        NordampelGELB.off()
        NordampelGRÜN.on()
        
        SüdampelROT.off()
        SüdampelGELB.off()
        SüdampelGRÜN.on()
                
        # Ost und West müssen anhalten
        OstampelROT.on()
        OstampelGELB.off()
        OstampelGRÜN.off() 
        
        WestampelROT.on()
        WestampelGELB.off()
        WestampelGRÜN.off()
        
        Zeit.sleep(LANGEPHASE)
        
        # +++++++++++++++
        # +++ Phase 2 +++
        # +++++++++++++++
        
        # Nord und Süd müssen bremsen
        NordampelROT.off()
        NordampelGELB.on()
        NordampelGRÜN.off()
        
        SüdampelROT.off()
        SüdampelGELB.on()
        SüdampelGRÜN.off()
        
        # Ost und West müssen sich bereitmachen
        OstampelROT.on()
        OstampelGELB.on()
        OstampelGRÜN.off()
        
        WestampelROT.on()
        WestampelGELB.on()
        WestampelGRÜN.off()
        
        Zeit.sleep(KURZEPHASE)
        
        # +++++++++++++++
        # +++ Phase 3 +++
        # +++++++++++++++
        
        # Nord und Süd müssen anhalten
        NordampelROT.on()
        NordampelGELB.off()
        NordampelGRÜN.off() 
        
        SüdampelROT.on()
        SüdampelGELB.off()
        SüdampelGRÜN.off()
        
        # Ost und West dürfen fahren
        OstampelROT.off()
        OstampelGELB.off()
        OstampelGRÜN.on()
        
        WestampelROT.off()
        WestampelGELB.off()
        WestampelGRÜN.on()
        
        Zeit.sleep(LANGEPHASE)
        
        # +++++++++++++++
        # +++ Phase 4 +++
        # +++++++++++++++
        
        # Nord und Süd müssen sich bereitmachen
        NordampelROT.on()
        NordampelGELB.on()
        NordampelGRÜN.off()
        
        SüdampelROT.on()
        SüdampelGELB.on()
        SüdampelGRÜN.off()
        
        # Bremsen
        OstampelROT.off()
        OstampelGELB.on()
        OstampelGRÜN.off()
        
        WestampelROT.off()
        WestampelGELB.on()
        WestampelGRÜN.off()
        
        Zeit.sleep(KURZEPHASE)
               
        

# Beim Unterbrechen des Programmes sollen 
# die folgenden Befehle ausgeführt werden
except KeyboardInterrupt:
    Pizzahupe.off()
    Ampel.closeGPIO()
    
    
 
