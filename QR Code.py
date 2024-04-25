import qrcode

features = qrcode.QRCode(version=1, box_size = 10, border= 4)
features.add_data('https://www.linkedin.com/in/analytical-kaif74/')
features.make(fit=True)
generate_image = features.make_image(fill_color="navy", back_color= 'lightgrey')
generate_image.save('LinkedIN.png')