from django.contrib import admin
from app.models import JobPost,Location,Author,Skills
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','salary','expiry_date')
    list_filter = ('title','salary')
    search_fields = ['title','salary']
    #fields = (('title',salary'),'expiry_date')
    #exlude
    fieldsets = (("Basic Information",{"fields": ('title','salary','type')}),
    ("Gernal Information",{"fields": ('description','slug','expiry_date','location','author','skills')}))

admin.site.register(JobPost,JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)


