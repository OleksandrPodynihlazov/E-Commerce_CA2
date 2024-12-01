from django.db import models
from django.conf import settings

class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Користувач, який звертається в техпідтримку
    created_at = models.DateTimeField(auto_now_add=True)  # Час створення чату
    is_active = models.BooleanField(default=True)  # Активний чат

    def __str__(self):
        return f"Chat with {self.user.username}"

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")  # Чат, до якого належить повідомлення
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Відправник повідомлення
    content = models.TextField()  # Вміст повідомлення
    created_at = models.DateTimeField(auto_now_add=True)  # Час створення повідомлення

    def __str__(self):
        return f"Message from {self.sender.username} on {self.created_at}"