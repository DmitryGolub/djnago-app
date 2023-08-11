from django.shortcuts import render
from django.core.mail import send_mail
from .form import OrderForm


def index(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = {
                'name': form.cleaned_data['name'],
                'phone': form.cleaned_data['phone'],
            }
            send_mail("Новая заявка!", f"{data['name']} - {data['phone']}", "dmitrygolub23@yandex.ru", ["dmitrygolub23@yandex.ru"], fail_silently=False)

        return render(request, 'shop/index.html', {'form': form})
    return render(request, 'shop/index.html', {'form': form})
