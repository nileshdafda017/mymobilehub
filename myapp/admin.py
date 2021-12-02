from django.contrib import admin
from . models import Contact,User,Product,Wishlist,Cart,Transaction
from django.contrib.admin.models import LogEntry
LogEntry.objects.all().delete()
# Register your models here.
admin.site.site_header="Nilesh"
admin.site.register(Contact)

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Transaction)