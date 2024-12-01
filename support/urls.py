from django.urls import path
from .views import user_chat_view, admin_chat_view, admin_reply_chat,admin_chat_detail,admin_chat_list

app_name = 'support'

urlpatterns = [
    path('chat/', user_chat_view, name='user_chat'),
    path('admin/chat/', admin_chat_view, name='admin_chat_view'),
    path('admin/chat/<int:chat_id>/', admin_reply_chat, name='admin_reply_chat'),
    path('', admin_chat_list, name='admin_chat_list'),
    path('<int:chat_id>/', admin_chat_detail, name='admin_chat_detail'), 
]
