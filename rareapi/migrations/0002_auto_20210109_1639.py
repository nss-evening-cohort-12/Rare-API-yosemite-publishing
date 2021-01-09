# Generated by Django 3.1.4 on 2021-01-09 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_authors', related_query_name='subscription_author', to='rareapi.rareuser'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField()),
                ('ended_on', models.DateTimeField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', related_query_name='author', to='rareapi.rareuser')),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', related_query_name='follower', to='rareapi.rareuser')),
            ],
        ),
    ]