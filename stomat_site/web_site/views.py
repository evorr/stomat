from django.shortcuts import render, redirect
from .models import Service, Category
from .forms import FormText
import asyncio
from telegram import Bot


def about_clinic(request):
    return render(request, 'web_site/about_clinic.html')


def price_list(request):
    categories = Category.objects.all()
    services = Service.objects.all()

    context = {
        'services': services,
        'categories': categories,
    }
    return render(request, 'web_site/price_list.html', context)


async def send_telegram_message(chat_id, message):
    bot_token = '6612335040:AAHhUWB9youeoFg3rdURinADlSI83j2guP4'
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)


def online_entry(request):
    if request.method == 'POST':
        form = FormText(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']

            chat_id = '1255453166'
            message = f"Запись на прием:\n Имя: {name}\n Телефон: {phone}"
            asyncio.run(send_telegram_message(chat_id, message))

    else:
        form = FormText()

    return render(request, 'web_site/online_entry.html', {'form': form})
