# Generated by Django 3.1.4 on 2021-01-09 19:46

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RareUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(null=True, upload_to='avatars')),
                ('created_on', models.DateField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.TextField()),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', related_query_name='author', to='rareapi.rareuser')),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', related_query_name='follower', to='rareapi.rareuser')),
            ],
        ),
        migrations.AddField(
            model_name='rareuser',
            name='subscriptions',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_ids', related_query_name='subscription_author_id', to='rareapi.subscription'),
        ),
        migrations.AddField(
            model_name='rareuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('content', models.TextField()),
                ('publication_date', models.TextField()),
                ('header_img_url', models.TextField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='post', to='rareapi.category')),
                ('reactions', models.ManyToManyField(related_name='posts', related_query_name='post', to='rareapi.Reactions')),
                ('tags', models.ManyToManyField(related_name='posts', related_query_name='post', to='rareapi.Tag')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='rareapi.rareuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('subject', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_authors', related_query_name='subscription_author', to='rareapi.rareuser')),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', related_query_name='posts', to='rareapi.post')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
