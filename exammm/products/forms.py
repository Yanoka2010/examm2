from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования карточки книги"""

    class Meta:
        model = Product
        fields = [
            'name', 'category', 'description', 'manufacturer',
            'supplier', 'price', 'unit', 'quantity', 'discount', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'manufacturer': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем подсказки к полям
        self.fields['price'].help_text = 'Цена в рублях'
        self.fields['discount'].help_text = 'Скидка в процентах (0-100)'
        self.fields['quantity'].help_text = 'Количество на складе (не может быть отрицательным)'
        self.fields['image'].help_text = 'Обложка (опционально, не больше 300x200 пикселей)'

    def clean_image(self):
        image = self.cleaned_data.get('image')
        # TODO(student): проверка размера обложки (например, не больше 300x200) и/или
        # уменьшение через Pillow (раньше логика была здесь; восстановите при необходимости).
        return image
