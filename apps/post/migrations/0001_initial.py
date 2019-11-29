# Generated by Django 2.2.6 on 2019-11-29 01:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('post_type', models.CharField(max_length=25)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.PostBase')),
                ('tipo', models.CharField(choices=[('PODA', 'Poda'), ('FALTA_CANTERO', 'Falta Cantero'), ('EXTRACCION', 'Extraccion'), ('ARBOL_EXISTENTE', 'Arbol Existente'), ('MANTENIMIENTO', 'Mantenimiento')], max_length=25)),
                ('text', models.TextField(max_length=500)),
            ],
            bases=('post.postbase',),
        ),
        migrations.CreateModel(
            name='PostInformativo',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.PostBase')),
                ('text', models.TextField(max_length=1000)),
            ],
            bases=('post.postbase',),
        ),
        migrations.CreateModel(
            name='PostImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PostBase')),
            ],
        ),
    ]
