from django.db import models
from django.utils.text import slugify
from django.contrib.auth.hashers import make_password

class Thread(models.Model):
    thread_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    password = models.CharField(max_length=128, blank=True)  # 空を許可
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # slug の自動生成
        if not self.slug:
            self.slug = slugify(self.thread_name)

        # password の処理: 入力がない場合はデフォルト値やハッシュ化
        #if self.password and not self.password.startswith('pbkdf2_'):
        #    self.password = make_password(self.password)  # 入力があればハッシュ化
        #elif not self.password:
        #    self.password = make_password('default')  # 入力がない場合のデフォルト値
            # または self.password = '' で空のまま保存も可

        super().save(*args, **kwargs)

    def __str__(self):
        return self.thread_name

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.thread}: {self.content[:50]}"
