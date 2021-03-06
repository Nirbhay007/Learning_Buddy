

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_user', '0001_initial'),
        ('theory', '__first__'),
        ('question', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cbt',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('cbt_slug', models.CharField(default='no slug', max_length=500)),
                ('cbt_category', models.CharField(max_length=500)),
                ('cbt_level', models.CharField(max_length=500)),
                ('duration', models.CharField(max_length=500)),
                ('actual_score', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('percentage', models.IntegerField(default=0)),
                ('corrections', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('app_user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='app_user.appuser')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('app_user_slug', models.CharField(
                    default='none', max_length=100)),
                ('cbt_id', models.CharField(default='none', max_length=100)),
                ('cbt_title', models.CharField(default='none', max_length=100)),
                ('cbt_type', models.CharField(default='none', max_length=100)),
                ('cbt_slug', models.CharField(default='none', max_length=100)),
                ('answers', models.CharField(default='none', max_length=100)),
                ('response_theory', models.TextField(default='none')),
                ('score', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('percentage', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CbtTheoryConnector',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('cbt', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='cbt.cbt')),
                ('theory', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='theory.theory')),
            ],
        ),
        migrations.CreateModel(
            name='CbtQuestionConnector',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('cbt', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='cbt.cbt')),
                ('question', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='question.question')),
            ],
        ),
        migrations.AddField(
            model_name='cbt',
            name='questions',
            field=models.ManyToManyField(
                through='cbt.CbtQuestionConnector', to='question.Question'),
        ),
        migrations.AddField(
            model_name='cbt',
            name='theorys',
            field=models.ManyToManyField(
                through='cbt.CbtTheoryConnector', to='theory.Theory'),
        ),
    ]
