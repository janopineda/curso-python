import qrcode
from PIL import Image
import os

ruta = os.path.dirname(__file__)

# Cambia la ruta de la URL a una ruta local
logo_path = os.path.join(ruta, "logo.png")

Logo_link = str(logo_path)
logo = Image.open(Logo_link)

basewidth = 100

# ajustar tamaño
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)


QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# tomando url o texto
url = 'https://forms.gle/2gYq3SMH46nST5By7'

# añadiendo URL o texto al QRcode
QRcode.add_data(url)

# generando el código QR
QRcode.make()

# tomando color de usuario
QRcolor = 'Black'

# añadiendo color al código QR
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color='white').convert('RGB')

# establecer tamaño del código QR
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# crear la carpeta si no existe
rutaQR = os.path.join(ruta, "qr")
if not os.path.exists(rutaQR):
    os.makedirs(rutaQR)

# guardar el código QR generado
archivo_qr = os.path.join(rutaQR, "qrregistro.png")
QRimg.save(archivo_qr, scale=10)

print('QR Listo!')






 

