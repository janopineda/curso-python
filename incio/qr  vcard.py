import qrcode
from PIL import Image
import os

# Obtener la ruta del directorio actual
ruta = os.path.dirname(__file__)

# Información del contacto
nombre = 'Alejandro Pineda Sanchez'
telefono = '9991259761'

# Ruta local del logo
logo_path = os.path.join(ruta, "logo.png")
logo = Image.open(logo_path)

# Ajustar el tamaño del logo
basewidth = 100
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

# Crear el código QR con corrección de errores alta
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Datos del vCard
vcard = f'BEGIN:VCARD\nVERSION:3.0\nFN:{nombre}\nTEL:{telefono}\nEND:VCARD'

# Añadir los datos al código QR
qr.add_data(vcard)
qr.make()

# Generar la imagen del código QR
qr_img = qr.make_image(fill_color='black', back_color='white').convert('RGB')

# Añadir el logo al código QR
pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
qr_img.paste(logo, pos)

# Crear la carpeta para guardar el código QR si no existe
ruta_qr = os.path.join(ruta, "qr")
if not os.path.exists(ruta_qr):
    os.makedirs(ruta_qr)

# Guardar el código QR generado
archivo_qr = os.path.join(ruta_qr, "qrSys.png")
qr_img.save(archivo_qr)

print('¡QR Listo!')