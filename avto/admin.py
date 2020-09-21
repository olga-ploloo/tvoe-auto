from django.contrib import admin

# Register your models here.
from avto.models import Category, Model, ModelImage, Brend, Generation, Equipment

class BrendAdmin(admin.ModelAdmin):
    model = Brend
    #fields = ('title', 'country')

class ModelImageInline(admin.TabularInline):
    model = ModelImage
    fields = ('description', 'image', 'image_base64')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'get_subcategories')
    filter_vertical = ('subcategories', )


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'generations')


class GenerationAdmin(admin.ModelAdmin):
    inlines = (ModelImageInline, )
    list_display = ('__str__',)


admin.site.register(Brend, BrendAdmin)
admin.site.register(Model)
admin.site.register(Category)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Generation, GenerationAdmin)