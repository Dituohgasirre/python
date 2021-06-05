from io import BytesIO
import string
import random

from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.http import HttpResponse

from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            posted_captcha = form.cleaned_data['captcha']
            saved_captcha = request.session.get('captcha')
            if saved_captcha is None:
                return HttpResponse('refresh and retry')
            # 对比验证码
            if posted_captcha.lower() == saved_captcha:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                if username == 'alice' and password == 'abc':
                    return HttpResponse('login success.')
            else:
                form.add_error('captcha', '验证码不匹配')
    else:
        form = LoginForm()
    return render(request, "polls/login.html", context={'form': form})


def make_image(char):
    im_size = (70, 40)
    font_size = 28
    bg = (0, 0, 0)
    offset = (1, 1)
    im = Image.new('RGB', size=im_size, color=bg)
    font = ImageFont.truetype('polls/ubuntu.ttf', font_size)
    draw = ImageDraw.ImageDraw(im)
    draw.text(offset, char, fill='yellow', font=font)
    im = im.transform(im_size, Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
    return im


def captcha(request):
    text = gentext(4)
    request.session['captcha'] = text.lower()
    im = make_image(text)
    imgout = BytesIO()
    im.save(imgout, format='png')
    img_bytes = imgout.getvalue()
    return HttpResponse(img_bytes, content_type='image/png')


def gentext(n):
    chars = string.ascii_letters
    return ''.join([random.choice(chars) for i in range(n)])

