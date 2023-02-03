from django.contrib import admin
from .models import Product, Post, Review

admin.site.register(Product)
admin.site.register(Post)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Review, ReviewAdmin)