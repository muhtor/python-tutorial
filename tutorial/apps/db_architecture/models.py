from django.db import models


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.name}"


class UserServiceEvaluationRank(models.Model):
    RANK = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),)
    rank = models.IntegerField(choices=RANK, default=1)
    user = models.ForeignKey('UserPersonalInfo', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} | {self.service} | {self.rank}"


class UserPersonalInfo(models.Model):
    full_name = models.CharField(max_length=64)
    GENDER = (
        ('male', 'Erkak'),
        ('female', 'Ayol'),
    )
    gender = models.CharField(choices=GENDER, default='male', max_length=64)
    services = models.ManyToManyField(
        Service,
        through='UserServiceEvaluationRank',
        through_fields=('user', 'service'),
    )

    def __str__(self):
        return f"{self.full_name} | {self.get_rank()}"

    def get_service(self):
        return " / ".join([str(p) for p in self.services.all()])

    def get_rank(self):
        items = UserServiceEvaluationRank.objects.filter(user__full_name='MurodAli')
        result = ""
        for i in items:
            result += ' ' + str(i.service) + ' - ' + str(i.rank) + ' | '
        return result










