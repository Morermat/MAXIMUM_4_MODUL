from django.contrib import admin
from .models import Advetisment

# Register your models here.
class AdvetismentAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'description', 'price', 'auction','created_date','update_date','get_image']
    list_filter=['auction','price','created_at']
    actions=['make_auction_as_false','make_auction_as_true']
    @admin.action(description='Make auction as false')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Make auction as True')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
admin.site.register(Advetisment,AdvetismentAdmin)