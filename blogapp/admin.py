from django.contrib import admin
from .models import author,article,content,Contatct,subscribe,livingcost,earning,embassy_address,ticket_price

# Register your models here.
class authorModel1(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model=author
admin.site.register(author, authorModel1)
class articleModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]

    class Meta:
        Model=article
admin.site.register(article,articleModel1)
class contentModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]

    class Meta:
        Model=content
admin.site.register(content,contentModel1)
class livingcostModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]

    class Meta:
        Model=livingcost
admin.site.register(livingcost,livingcostModel1)
class earningModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]

    class Meta:
        Model=earning
admin.site.register(earning,earningModel1)
class embassy_addressModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]

    class Meta:
        Model=embassy_address
admin.site.register(embassy_address,embassy_addressModel1)
class ticket_priceModel1(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__","details"]

    class Meta:
        Model=ticket_price
admin.site.register(ticket_price,ticket_priceModel1)

admin.site.register(Contatct)

admin.site.register(subscribe)