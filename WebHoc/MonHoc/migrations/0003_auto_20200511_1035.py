# Generated by Django 3.0.5 on 2020-05-11 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MonHoc', '0002_auto_20200508_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mon',
            name='GioiThieu',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='BaiHoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaBai', models.CharField(max_length=4)),
                ('TenBai', models.TextField()),
                ('NoiDung', models.FileField(null=True, upload_to='')),
                ('MaMon', models.CharField(max_length=4)),
                ('mon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MonHoc.Mon')),
            ],
        ),
    ]
