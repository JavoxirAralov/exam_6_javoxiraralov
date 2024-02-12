import csv
import io

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path
from django.utils.html import format_html

from apps.models import User, Product


@admin.register(Product)
class ProductListAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'user_image']

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ('first_name', 'last_name', 'email', 'image')}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def user_image(self, obj: User):
        return format_html(
            f'<a href="{obj.pk}">'
            f'<img src="{obj.image.url}" width="35" height="35" style="object-fit: cover;"></a>'
        )

    user_image.short_description = 'Image'


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "admin/change_list.html"
    list_display = ['id', 'title']

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            next(reader)
            result = []
            for row in reader:
                result.append(Product(
                    pk=int(row[0]),
                    title=row[1],
                    image=row[2],
                    description=row[3],
                    quantity=row[4],
                    price=row[5]
                ))

            Product.objects.bulk_create(result)
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "csv_form.html", payload)