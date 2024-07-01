import network
import ubinascii
import time

wifi = network.WLAN(network.STA_IF)

wifi.active(True)

PC08 = "f4eab5a75e18"
PC082 = "f4eab53f4118"
LaboratorioCentral = "f4eab5a73ed8"
LaboratorioCentral2 = "f4eab53f4c98"
LaboratiorioCentral3 = "f4eab53f5658"
LaboratirioCentral_07_09 = "f4eab5a75598"
PasilloCad = "f4eab53faf98"
PasilloLab = "c8675e43db15"
Pasillocad_lab = "f4eab53f5358"
lab = "c8675e447398"
Pasillo_C_Santander = "f4eab5f843d8" 
Pasillo_C_Escalera = "f4eab5f843d8"
while True:
    networks = wifi.scan()
    mac_encontrada = False
    for network in networks:
        mac_address = ubinascii.hexlify(network[1]).decode('utf-8')
        if mac_address == PC08:
            print("P08")
            mac_encontrada = True
            break
        if mac_address == PC082:
            print("P08")
            mac_encontrada = True
            break
        if mac_address == LaboratorioCentral:
            print("Laboratorio Central")
            mac_encontrada = True
            break
        if mac_address == lab:
            print("Laboratorio Central")
            mac_encontrada = True
            break
        if mac_address == PasilloCad:
            print("Pasillo Cad")
            mac_encontrada = True
            break
        if mac_address == Pasillocad_lab:
            print("Pasillo Cad-Lab")
            mac_encontrada = True
            break
        if mac_address == PasilloLab:
            print("Pasillo Lab")
            mac_encontrada = True
            break
        if mac_address == LaboratirioCentral_07_09:
            print("LaboratorioCentral_07_09")
            mac_encontrada = True
            break
        if mac_address == Pasillo_C_Santander:
            print("Pasillo_C_Santander")
            mac_encontrada = True
            break
        if mac_address == Pasillo_C_Escalera:
            print("Pasillo_C_Escalera")
            mac_encontrada = True
            break
    if not mac_encontrada:
        print("No se a dectetado ninguna red cercana")
    time.sleep(1)
        

wifi.active(False)