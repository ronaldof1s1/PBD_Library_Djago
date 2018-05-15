from django.contrib import admin
from .models import *
# Register your models here.

class ExcludeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
    
admin.site.register(Address, ExcludeAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Copy)
admin.site.register(User)
admin.site.register(Loan)