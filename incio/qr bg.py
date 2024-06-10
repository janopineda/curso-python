import segno
from urllib.request import urlopen
import os

ruta = os.path.dirname(__file__)
rutaQR = os.path.join(ruta, "qr")

slts_qrcode = segno.make_qr("https://drive.google.com/file/d/1ALgt0W0bf9_EYhIyIexKk55eeaYNtNPh/view?usp=sharing")

# Cambia la ruta de la URL a una ruta local
logo_path = os.path.join(ruta, "logo.png")

# Usa open para abrir el archivo local
with open(logo_path, 'rb') as logo_file:
    slts_qrcode.to_artistic(
        background=logo_file,
        target=os.path.join(rutaQR, "Harkness_Arte.png"),
        scale=5,
    )

print(rutaQR)
