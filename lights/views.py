from django.shortcuts import render
from .models import LightPassport
import qrcode
from django.http import HttpResponse
from io import BytesIO


def light_passport(request, light_id):
    passport = type('FakePassport', (), {'light_id': light_id, 'qr_data': f'QR for {light_id}'})
    created = True

    context = {
        "passport": passport,
        "created": created,  # True if just created now
    }
    return render(request, "light_passport.html", context)


def generate_qr(request, light_id):
    qr_url = f"http://192.168.29.153:8000/light/{light_id}/light_passport.html"
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response
