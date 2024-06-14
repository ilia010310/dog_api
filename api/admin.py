from django.contrib import admin

from api.models import Dog, Breed


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    """
    Админ-панель модели собак
    """
    list_display = ['name', 'age', 'gender', 'color', 'breed']
    list_editable = ['age']
    search_fields = ['name', 'breed']
    ordering = ['name']

    def has_delete_permission(self, request, obj=None):
        """Запред на удаление любой собаки, кому бы то ни было"""
        return False


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """
    Админ-панель модели породы
    """
    list_display = ['name_of_breed',
                    'size',
                    'friendliness',
                    'trainability',
                    'shedding_amount',
                    'exercise_needs']
    list_editable = ['size',
                     'friendliness',
                     'trainability',
                     'shedding_amount',
                     'exercise_needs']

    search_fields = ['name_of_breed', 'size']

    ordering = ['size']
