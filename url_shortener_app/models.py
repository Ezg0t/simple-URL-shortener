from django.db import models
import random
import string

class URL(models.Model):
    url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=6, unique=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.short_code:
            self.short_code = self.generate_short_code(length=6)
        super().save(*args, **kwargs)
        
    @staticmethod
    def generate_short_code(length: int = 6) -> str:
        characters: str = string.ascii_letters + string.digits
        while True:
            code = ''.join(random.choices(characters, k=length))
            if not URL.objects.filter(short_code=code).exists():
                return code