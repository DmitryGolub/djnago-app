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
            sender = 'gosest4@gmail.com'
            send_mail("Новая заявка!", f"{data['name']} - {data['phone']}", sender, [sender], fail_silently=False)

        return render(request, 'shop/index.html', {'form': form})
    return render(request, 'shop/index.html', {'form': form})
