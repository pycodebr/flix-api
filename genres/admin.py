from django import forms
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from genres.models import Genre


class FileUploadForm(forms.Form):
    file = forms.FileField()


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    change_list_template = 'genre_changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('upload-file/', self.upload_file),
        ]
        return my_urls + urls

    def upload_file(self, request):
        if request.method == 'POST':
            file = request.FILES['file']

            # Processe seu arquivo aqui e faça o que quiser com ele (file)
            print(f'Variável com conteúdo do arquivo: {file}')

            form = FileUploadForm()
            return render(
                request=request,
                template_name='admin/upload.html',
                context={
                    'form': form,
                    'title': 'Importar arquivo',
                    'response': 'Arquivo processado com sucesso.'
                },
            )

        form = FileUploadForm()
        return render(
            request=request,
            template_name='admin/upload.html',
            context={'form': form, 'title': 'Importar arquivo'},
        )
