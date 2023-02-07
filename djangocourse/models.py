from django.db import models


# Create your models here.

class Client(models.Model):
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    middle_name = models.CharField(max_length=250, verbose_name='Отчество')
    email = models.CharField(max_length=250, verbose_name='Почта')
    comment = models.CharField(max_length=250, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    theme = models.CharField(max_length=250, verbose_name='тема')
    text = models.CharField(max_length=250, verbose_name='текст')

    def __str__(self):
        return f'{self.theme}'


class DistributionList(models.Model):
    STATUS_CREATED = 'created'
    STATUS_LAUNCHED = 'launched'
    STATUS_COMPLETED = 'completed'
    STATUSES = (
        (STATUS_CREATED, 'создано'),
        (STATUS_LAUNCHED, 'запущено'),
        (STATUS_COMPLETED, 'завершено')
    )

    PERIOD_DAY = 'day'
    PERIOD_WEEK = 'week'
    PERIOD_MONTH = 'month'
    PERIODS = (
        (PERIOD_DAY, 'день'),
        (PERIOD_WEEK, 'неделя'),
        (PERIOD_MONTH, 'месяц')
    )
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    message = models.ForeignKey('Message', on_delete=models.CASCADE)
    time = models.TimeField(null=True)
    periodicity = models.CharField(choices=PERIODS, default=PERIOD_DAY, max_length=10, verbose_name='Период')
    status = models.CharField(choices=STATUSES, default=STATUS_CREATED, max_length=10, verbose_name='Статус')


# class DistributionSettings(models.Model):
#     STATUS_CREATED = 'created'
#     STATUS_LAUNCHED = 'launched'
#     STATUS_COMPLETED = 'completed'
#     STATUSES = (
#         (STATUS_CREATED, 'создано'),
#         (STATUS_LAUNCHED, 'запущено'),
#         (STATUS_COMPLETED, 'завершено')
#     )
#
#     PERIOD_DAY = 'day'
#     PERIOD_WEEK = 'week'
#     PERIOD_MONTH = 'month'
#     PERIODS = (
#         (PERIOD_DAY, 'день'),
#         (PERIOD_WEEK, 'неделя'),
#         (PERIOD_MONTH, 'месяц')
#     )
#
#     id = models.AutoField(primary_key=True, verbose_name='ID')
#     time = models.TimeField()
#     periodicity = models.CharField(choices=PERIODS, default=PERIOD_DAY, max_length=10, verbose_name='Период')
#     status = models.CharField(choices=STATUSES, default=STATUS_CREATED, max_length=10, verbose_name='Статус')
#
#
# class DistributionMessage(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name='ID')
#     theme = models.CharField(max_length=250, verbose_name='тема')
#     text = models.CharField(max_length=250, verbose_name='текст')
#
#
# class DistributionTry(models.Model):
#     STATUS_SUCCESS = 'success'
#     STATUS_FAIL = 'fail'
#     STATUSES = (
#         (STATUS_SUCCESS, 'успех'),
#         (STATUS_FAIL, 'провал')
#     )
#     REPORT_YES = 'yes'
#     REPORT_NO = 'no'
#     REPORTS = (
#         (REPORT_YES, 'да'),
#         (REPORT_NO, 'нет')
#     )
#     date_time = models.DateTimeField()
#     status = models.CharField(choices=STATUSES, max_length=10, verbose_name='Статус')
#     server_return = models.CharField(choices=REPORTS, max_length=5, verbose_name='Ответ')
