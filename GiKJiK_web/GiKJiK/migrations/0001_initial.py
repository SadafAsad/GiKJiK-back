# Generated by Django 3.0.8 on 2020-07-30 20:13

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
            name='Class',
            fields=[
                ('name', models.CharField(max_length=225)),
                ('class_id', models.CharField(max_length=225, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(default='Offline', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='WhiteBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='white_boards', to='GiKJiK.Class')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, max_length=225, upload_to='')),
                ('django_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
                ('online_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='online_users', to='GiKJiK.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Quize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('date', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(default='Not Started', max_length=225)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_quizes', to='GiKJiK.Class')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_quizes', to='GiKJiK.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=225)),
                ('solution', models.CharField(blank=True, max_length=225)),
                ('point', models.IntegerField()),
                ('quize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='GiKJiK.Quize')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='GiKJiK.Class')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_news', to='GiKJiK.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_grades', to='GiKJiK.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='std_grades', to='GiKJiK.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_classes', to='GiKJiK.UserProfile'),
        ),
        migrations.AddField(
            model_name='class',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='member_classes', to='GiKJiK.UserProfile'),
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='teacher_classes', to='GiKJiK.UserProfile'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=225)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='GiKJiK.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chat_room', to='GiKJiK.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=225)),
                ('ans_state', models.CharField(choices=[('0', 'Correct'), ('1', 'Wrong'), ('2', 'Not Answered')], default='2', max_length=225)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='GiKJiK.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='std_answers', to='GiKJiK.UserProfile')),
            ],
        ),
    ]
