import PiTraffic as Ampel
import time as Zeit

# Festlegung der Ostampel
OstampelROT = Ampel.Traffic("EAST", "RED")
OstampelGELB = Ampel.Traffic("EAST", "YELLOW")
OstampelGRÜN = Ampel.Traffic("EAST", "GREEN")

Pizzahupe = Ampel.Buzzer()

try:
    while True:
        # alles anschalten
        OstampelROT.on()
        OstampelGELB.on()
        OstampelGRÜN.on()
        Pizzahupe.on()
        
        Zeit.sleep(0.2)
        
        OstampelROT.off()
        Pizzahupe.off()
        
        Zeit.sleep(2)
        
        OstampelGELB.off()
                
        Zeit.sleep(2)
        
        OstampelGRÜN.off()
        
        Zeit.sleep(3)
         
        

except KeyboardInterrupt:
    Pizzahupe.off()
    PiTraffic.closeGPIO()
    
    
 
