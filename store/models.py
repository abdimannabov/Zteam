from django.db import models
from django.db import models
import datetime

from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Name")
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    genre = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("category", kwargs={"genre": self.genre})

    def __str__(self) -> str:
        return self.title

class Game(models.Model):
    GENRES = [
        ('AC', "Action"),
        ('Sh', "Shooter"),
        ('AR', "Arcade"),
        ('RA', "Racing"),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0, null=False)
    downloads = models.FloatField(default=0.0, null=False)
    storage = models.IntegerField(default=0, null=False)
    genre = models.CharField(max_length=2, choices=GENRES, default="AC")
    added_at = models.DateTimeField(default=datetime.date.today)
    played_hours = models.IntegerField(default=40)
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_photo(self):
        try:
            return self.image.url
        except:
            return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAM1BMVEX///+/v7+8vLz8/Pz5+fnt7e3ExMTHx8fPz8/h4eHw8PD29vbY2Njn5+fMzMzU1NS2trYNfAMMAAAEIUlEQVR4nO2c2ZqjIBBGI+573v9pOyZMVHZaC6rn+8/ltAonlFAUmTweAAAAAAAAAFDNPWfqMkZmaEXBF9FVkGEJZLgCGa5AhiuQ4Qpkvjcz4DaZJXeW3PdTc5OMmGJupWE8deiSTNT2gQTISCBDCWQkkKEEMhLIUAIZCWQogYwEMpRARgIZSpLJpFBNIVMOU/F8scxRj48ngcy4yoKWEO1MOkD0MvWyXyWannJwyGWG5lz2pCyvUctU3bkeLUR9T8dNUMv0am1dLL8JtGoIedmoZfSDAjHHtCGZuyHgKmKZUT/0EGtMGx+qrgj5CIhltCh70UZPz+UkxBrQNWKZyXQcFS0zPAvRBsTZX5Apt3ZE778tg0wTK/N+iGhG74XEMrVhAlhi2tieIe/zL1DEMpU+MKKPaeP1CNlKwBRAvc6s+tD4w+XEHqneoaGWGQrFJjY5q9vwO8kTzVnJzZa4gRmX/dbW1ztymW3BO7qEpCUHpuMH4csC6PczZf+NNPGMHJdHfdpANJ6rU2ybx7X5fH9iic0xx/MG4un5KNIUNMa5n6Y5MsLeg3p+4TxTAOtSU61OhZ4pIL9Mbf1m+Lhoi5R7wc0uU3WN5U1Sg2xjcTaSW2ab6yw2daPLNM4sILfM0BY2G9NX89zb1Mwy5SfzMtmYNqmvLMA1O2eW+W4RNBtTkG24poC8MtX3CerYVEthxrURyCtzCCXFxrjf3ppxTQFZZYbj/adIswWZu52sMqcssmh3m7GzuTjLNDll1K3ON9JMy+V+mX0KyCgzqqH0fR/Oib96lb2TGWUmvZ/t26YyFA4O2KeARDKGv82Gd/w9Ns4gc7aUaD/Tawv3aFxINpu9hGGRsWYBaWT6olP/avv429odZIWjFpBE5rX7Fcr+vb7yPzxs5whJZPr3s4//UtpW+CBstYAkBY13WUIcI22+4mKtBaSQkRnY4TTTsCGOwzw0Kb7U8K9eJDrZB9/k68WSBSSQmfeL1o+NPY0MlTHXAuhljiEl3jbl1SCzHdbQy8ynXmyRdu3tlz3NIlMqC8pSja40MhjTFJD6SOMVad4VPgTjFEAu40m0fo2pq9QyN7wfFgwJGrFMeXUStrPq7RHL0A2MqRZALEM3MEWhJ2i0MrPehdswdJZUxlqWvAW9QE0qczWf9DCpvaWUqeylvDvQpwBKGeKB0U8ECGXUL87eznd/lEDGVBi72UaJMzqZy1vjABnlsIZOZlg7cqZUMo8yAecWc5823wpkJJChBDISyFACGQlkKIGM5P+VYfBjbXN/14+1sQMyXIEMVyDDFchwBTJcgQxXIMMVyHAFMlyBDFcgwxXIcAUyXIEMVyDDFchwBTJcgQxXIMMVyHAFMlyBDFcgw5VYma7hTMgPie9UQ82ZoF/fBwAAAAAAAIC/ww/JmYESURpw2wAAAABJRU5ErkJggg=="
