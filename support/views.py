from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Chat, Message
from .forms import MessageForm

def user_chat_view(request):
    chat, created = Chat.objects.get_or_create(user=request.user, is_active=True)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user
            message.save()
            return redirect('support:user_chat')  # Перезавантажуємо чат після відправлення повідомлення
    else:
        form = MessageForm()

    messages = Message.objects.filter(chat=chat).order_by('created_at')

    return render(request, 'support/user_chat.html', {'chat': chat, 'form': form, 'messages': messages})

def admin_chat_view(request):
    chats = Chat.objects.filter(is_active=True)

    return render(request, 'support/admin_chat_list.html', {'chats': chats})

@login_required
def admin_chat_view(request):
    chats = Chat.objects.filter(is_active=True)

    return render(request, 'support/admin_chat_list.html', {'chats': chats})
def is_admin(user):
    return user.is_superuser

# Перегляд всіх чатів адміністратором
@login_required
@user_passes_test(is_admin)
def admin_chat_list(request):
    chats = Chat.objects.all()  # Отримуємо всі чати
    return render(request, 'support/admin_chat_list.html', {'chats': chats})

# Перегляд конкретного чату
@login_required
@user_passes_test(is_admin)
def admin_chat_detail(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    messages = chat.messages.all()  # Отримуємо всі повідомлення для цього чату

    if request.method == 'POST':
        message_content = request.POST.get('message')  # Отримуємо текст відповіді
        if message_content:
            # Створюємо нове повідомлення від адміністратора
            Message.objects.create(
                chat=chat,
                sender=request.user,
                content=message_content
            )

    return render(request, 'support/admin_chat_detail.html', {
        'chat': chat,
        'messages': messages
    })

@login_required
def admin_reply_chat(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user  # Відправник - адміністратор
            message.save()
            return redirect('support:admin_chat_view')  # Переходимо до списку чатів

    form = MessageForm()
    messages = Message.objects.filter(chat=chat).order_by('created_at')

    return render(request, 'support/admin_reply_chat.html', {'chat': chat, 'form': form, 'messages': messages})