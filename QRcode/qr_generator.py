import qrcode
import sys, time

def gen_qr(data,img_path='QRcode/images',img_filename='qr_code'):
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(img_path+'/'+img_filename+'_'+str(time.time())+'.png')
    
if __name__ == '__main__':
    input_text = str('https://www.google.com')
    gen_qr(input_text)