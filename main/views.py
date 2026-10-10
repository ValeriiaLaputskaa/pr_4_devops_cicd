from django.http import HttpResponse

def home(request):
    html = """
    <div style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h1 style="color: #2c3e50;">Головна сторінка</h1>
        <p style="font-size: 18px; color: #27ae60;">Успіх!</p>
        <a href="/about/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #3498db; color: white; text-decoration: none; border-radius: 5px;">Про нас</a>
    </div>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <div style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h1 style="color: #2c3e50;">Сторінка 'Про нас'</h1>
        <p style="font-size: 18px;">Практична робота 4, Лапуцька Валерія ПДМ-51</p>
        <a href="/" style="display: inline-block; margin-top: 20px; padding: 10px 20px; background: #3498db; color: white; text-decoration: none; border-radius: 5px;">На головну</a>
    </div>
    """
    return HttpResponse(html)