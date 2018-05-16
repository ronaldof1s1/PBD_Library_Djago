from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.

class ExcludeAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}



class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ['authors']
    forms = BookAdminForm

class CopyAdmin(admin.ModelAdmin):
    form = CopyAdminForm

admin.site.register(Address, ExcludeAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Copy, CopyAdmin)
admin.site.register(User)
admin.site.register(Loan)