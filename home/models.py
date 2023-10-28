from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    chat_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Определение отношений
    targets = models.ManyToManyField('Target', related_name='users')
    notes = models.ManyToManyField('Note', related_name='users')
    tasks = models.ManyToManyField('Task', related_name='users')
    finance = models.OneToOneField('Finance', on_delete=models.CASCADE)


class Target(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField()
    is_finished = models.BooleanField(default=False)


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    data = models.TextField()


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField()
    tags = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    text = models.TextField()


class Finance(models.Model):
    finance_predictions = models.ManyToManyField('FinancePrediction', related_name='finance')
    finance_operations = models.ManyToManyField('FinanceOperation', related_name='finance')


class FinancePrediction(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey('FinanceCategory', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class FinanceCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()


class FinanceOperation(models.Model):
    id = models.AutoField(primary_key=True)
    is_income = models.BooleanField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField()
    category = models.ForeignKey('FinanceCategory', on_delete=models.CASCADE)
    date = models.DateTimeField()
