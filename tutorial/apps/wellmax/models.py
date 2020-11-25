from django.db import models
from django.utils.html import format_html
from django.db.models.signals import pre_save
from .utils import unique_key_generator
# Create your models here.


class UserInfo(models.Model):
    GENDER = (('male', 'Мужчина'), ('female', 'Женщина'),)
    unique_id = models.CharField(max_length=120, null=True, blank=True, unique=True)
    full_name = models.CharField(max_length=255, verbose_name='Ф.И.О.')
    gender = models.CharField(choices=GENDER, max_length=50, default='male', verbose_name='Пол')
    room = models.IntegerField(verbose_name='Номер Комнаты')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return '{}'.format(self.full_name)


class UserServiceEvaluation(models.Model):
    RANK = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),)
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    service1_rank = models.IntegerField(choices=RANK, default=1, verbose_name='Доброжелательность и оперативность '
                                                                              'персонала')
    service2_rank = models.IntegerField(choices=RANK, default=1, verbose_name='Обслуживание в  ресторане и '
                                                                              'разнообразие блюд')
    service3_rank = models.IntegerField(choices=RANK, default=1, verbose_name='Чистота и  оборудование номера')
    service4_rank = models.IntegerField(choices=RANK, default=1, verbose_name='Летний бар и бассейн')
    feedback = models.TextField(verbose_name='отзыв', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def service_1(self):
        return self.get_percent(instance=self.service1_rank)

    def service_2(self):
        return self.get_percent(instance=self.service2_rank)

    def service_3(self):
        return self.get_percent(instance=self.service3_rank)

    def service_4(self):
        return self.get_percent(instance=self.service4_rank)

    @staticmethod
    def get_percent(instance=None):
        if instance:
            percentage = ((instance / 10) * 10)
        else:
            percentage = 0
        return format_html(
            '''
            <progress value="{0}" max="10"></progress>
            <span style="font-weight:bold">{0}</span>
            ''',
            percentage
        )


def pre_save_user(sender, instance, *args, **kwargs):
    if not instance.unique_id:
        instance.unique_id = unique_key_generator(instance)
pre_save.connect(pre_save_user, sender=UserInfo)

