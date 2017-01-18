"""
Definition of models.
"""

from django.db import models

class Programme(models.Model):
    name = models.CharField(max_length=50)
    date_started = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'programme'

class Workout(models.Model):
    name = models.CharField(max_length=50)
    programme = models.ForeignKey(Programme)

    def __str__(self):
        return str(self.programme) + ': ' + self.name 

    class Meta:
        db_table = 'workout'

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'exercise'

class WorkoutDetail(models.Model):
    exercise = models.ForeignKey(Exercise)
    workout = models.ForeignKey(Workout)
    order = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField()
    reps = models.IntegerField()
    notes = models.CharField(max_length=500)

    class Meta:
        db_table = 'workoutdetail'

class WeightSet(models.Model):
    name = models.CharField(max_length=50)
    options = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'weightset'

class WeightConfig(models.Model):
    weight_set = models.ForeignKey(WeightSet)
    unit = models.CharField(max_length=2)
    total_weight = models.DecimalField(decimal_places=2, max_digits=10)
    config = models.CharField(max_length=50)

    class Meta:
        db_table = 'weightconfig'

class ProgrammeLog(models.Model):
    exercise = models.ForeignKey(Exercise)
    workout = models.ForeignKey(Workout)
    programme = models.ForeignKey(Programme)
    datestamp = models.DateField()
    set_no = models.IntegerField()
    weight = models.ForeignKey(WeightConfig, blank=True, null=True)
    reps = models.IntegerField()

    class Meta:
        db_table = 'programmelog'




