# Generated by Django 2.0.7 on 2018-07-19 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='code',
            field=models.CharField(max_length=255, verbose_name='代码'),
        ),
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=100, verbose_name='地名'),
        ),
        migrations.AlterField(
            model_name='area',
            name='parent',
            field=models.IntegerField(verbose_name='父级编号(关联自已)'),
        ),
        migrations.AlterField(
            model_name='area',
            name='type',
            field=models.IntegerField(choices=[(0, '国家'), (1, '省'), (2, '市'), (3, '区县')], verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='note',
            name='addtime',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Category', verbose_name='来源'),
        ),
        migrations.AlterField(
            model_name='note',
            name='message',
            field=models.TextField(verbose_name='消息'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.User', verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='user',
            name='about',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='关于我'),
        ),
        migrations.AlterField(
            model_name='user',
            name='addtime',
            field=models.DateTimeField(auto_now=True, verbose_name='注册时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvc.Area', verbose_name='地区'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='face',
            field=models.ImageField(blank=True, default='', upload_to='face/%Y/%m/%d', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='friend',
            field=models.ManyToManyField(related_name='_user_friend_+', to='mvc.User', verbose_name='朋友'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='realname',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='个人主页'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, verbose_name='用户名'),
        ),
    ]