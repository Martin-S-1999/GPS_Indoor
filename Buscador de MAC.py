import network
import ubinascii
import time

# Configura el ESP8266 como estación
wifi = network.WLAN(network.STA_IF)

# Activa el ESP8266
wifi.active(True)


        # Escanea las redes WiFi disponibles
networks = wifi.scan()

        # Imprime las direcciones MAC de las redes WiFi
for network in networks:
    ssid = network[0].decode('utf-8')
    mac_address = ubinascii.hexlify(network[1]).decode('utf-8')
    print("SSID:", ssid)
    print("MAC Address:", mac_address)
    print("---------------------------")
        
        # Espera 3 segundos antes de repetir el bucle

    # Asegura que el WiFi se desactive en caso de interrupción del bucle
wifi.active(False)