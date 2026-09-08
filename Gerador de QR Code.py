import qrcode
# 1. link do seu QR Code
link = "https://missceliaassistentevirtual.lovable.app/"

# 2. Design e tamanho do QR Code
qr = qrcode.QRCode(
    version=1,       # Define a complexidade/tamanho (1 a 40)
    box_size=10,     # Tamanho de cada quadrado do código (pixels)
    border=4,        # Espessura da margem branca
)

# 3. link e compile
qr.add_data(link)
qr.make(fit=True)

# 4. Gere a image
imagem = qr.make_image(fill_color="black", back_color="white")

# 5. Arquivo fica salvo geralmente na mesma pasta em que o arquivo original está
imagem.save("misscelia_qrcode.png")
print("QR Code gerado com sucesso!")
