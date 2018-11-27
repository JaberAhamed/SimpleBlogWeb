from django.contrib import admin
from .models import author,articla,catagory,comment

# Register your models here.


#admin.site.register(author)
#admin.site.register(articla)
#admin.site.register(catagory)


@admin.register(author)
class authorAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'details']
    search_fields = ["__str__", "details"]

    class Meta:
        model = author

@admin.register(articla)
class articaleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "posted_on", "update_on"]
    search_fields = ["__str__", "details"]
    list_per_page = 10
    list_filter = ["posted_on", "catagory"]
    class Meta:
        model = articla


@admin.register(catagory)
class catagoryAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10


@admin.register(comment)
class catagoryAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        model = comment