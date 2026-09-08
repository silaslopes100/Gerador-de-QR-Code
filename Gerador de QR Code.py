import qrcode
# 1. Defina o link do seu QR Code
link = "https://missceliaassistentevirtual.lovable.app/"

# 2. Configure o design e tamanho do QR Code
qr = qrcode.QRCode(
    version=1,       # Define a complexidade/tamanho (1 a 40)
    box_size=10,     # Tamanho de cada quadrado do código (pixels)
    border=4,        # Espessura da margem branca
)

# 3. Adicione o link e compile
qr.add_data(link)
qr.make(fit=True)

# 4. Gere a imagem (você pode mudar as cores aqui)
imagem = qr.make_image(fill_color="black", back_color="white")

# 5. Salve o arquivocls
imagem.save("misscelia_qrcode.png")
print("QR Code gerado com sucesso!")