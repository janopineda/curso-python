import segno
import os

ruta = os.path.dirname(__file__)
rutaQr = os.path.join(ruta, "qr")
os.makedirs(rutaQr, exist_ok=True)

# Crear el código QR
qrcode = segno.make_qr("https://docs.google.com/forms/d/e/1FAIpQLSdvgIWfbMiIkXKqvaWamcdER-uCzMzVMXgMutK5stknVOQW4w/viewform")
archivo_qr = os.path.join(rutaQr, "qrSys.png")
qrcode.save(archivo_qr, scale=10)

print(f"Código QR guardado en: {archivo_qr}")