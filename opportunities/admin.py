from django.contrib import admin
from .models import Application, Opportunity, Profile


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title_en", "company", "category", "is_remote", "created_at")
    list_filter = ("category", "is_remote")
    search_fields = ("title_en", "title_ar", "company")
    list_per_page = 25
    ordering = ("-created_at",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "headline")
    list_filter = ("role",)
    search_fields = ("user__username", "user__email", "headline")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("user", "opportunity", "created_at")
    list_filter = ("opportunity__category", "created_at")
    search_fields = ("user__username", "opportunity__title_en", "opportunity__company")
    autocomplete_fields = ("user", "opportunity")
    date_hierarchy = "created_at"


admin.site.site_header = "CareerBridge إدارة المنصة"
admin.site.site_title = "CareerBridge Admin"
admin.site.index_title = "إدارة الفرص والمستخدمين"
