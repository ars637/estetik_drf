# Generated by Django 5.0.3 on 2024-06-24 12:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='only_medias/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'svg', 'jpeg', 'mp4', 'avi', 'mkv', 'mov', 'pdf', 'doc', 'docx', 'gif'])], verbose_name='Файл')),
                ('file_type', models.CharField(choices=[('image', 'Изображение'), ('video', 'Видео'), ('document', 'Документ'), ('gif', 'Гиф')], max_length=10, verbose_name='Тип файла')),
            ],
            options={
                'verbose_name': 'Медиа файл',
                'verbose_name_plural': 'Медиа файлы',
            },
        ),
        migrations.CreateModel(
            name='CommonSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_phone_number', models.CharField(max_length=20, verbose_name='Номер телефона клиники')),
                ('main_text', models.TextField(verbose_name='Текст на главной странице в header !')),
                ('main_page_text_on_right_gif', models.TextField(verbose_name='Текст на гиф с права на главной странице !')),
                ('our_clinic_text', models.TextField(verbose_name='Текст на странице о клинике !')),
                ('specialists_page_text_on_right_photo', models.TextField(verbose_name='Текст на странице специалисты на правом фото !')),
                ('actions_page_text_on_right_photo', models.TextField(verbose_name='Текст на странице специалисты на правом фото !')),
                ('product_page_text_on_right_photo', models.TextField(verbose_name='Текст на странице продукта на правом фото !')),
                ('actions_page_left_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_page_left_image', to='common.media', verbose_name='Фото с лева на странице акции !')),
                ('actions_page_right_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_page_right_image', to='common.media', verbose_name='Фото с права на странице акции !')),
                ('contacts_page_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_page_image', to='common.media', verbose_name='Фото на странице контакты !')),
                ('main_gif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_page_header_gif', to='common.media', verbose_name='Гиф на главной странице в header !')),
                ('main_left_gif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_page_left_gif', to='common.media', verbose_name='Гиф на главной странице ниже акции с лева !')),
                ('main_right_gif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_page_right_gif', to='common.media', verbose_name='Гиф на главной странице ниже акции с права !')),
                ('our_clinic_gif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='our_clinic_gif', to='common.media', verbose_name='Гиф на странице о клинике в header !')),
                ('product_page_left_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_page_left_image', to='common.media', verbose_name='Фото с лева на странице продукта !')),
                ('product_page_right_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_page_right_image', to='common.media', verbose_name='Фото с права на странице продукта !')),
                ('products_page_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_page_image', to='common.media', verbose_name='Фото на странице продукты !')),
                ('service_page_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_page_image', to='common.media', verbose_name='Фото на странице сервисы !')),
                ('specialists_page_left_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialists_page_left_image', to='common.media', verbose_name='Фото с лева на странице специалисты !')),
                ('specialists_page_right_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialists_page_right_image', to='common.media', verbose_name='Фото с права на странице специалисты !')),
                ('vacancy_page_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_page_image', to='common.media', verbose_name='Фото на странице продукты !')),
            ],
            options={
                'verbose_name': 'Общие настройки',
                'verbose_name_plural': 'Общие настройки',
            },
        ),
    ]
