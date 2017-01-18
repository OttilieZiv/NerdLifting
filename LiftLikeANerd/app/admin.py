from django.contrib import admin
from .models import Exercise, Programme, ProgrammeLog, WeightConfig, WeightSet, Workout, WorkoutDetail

admin.site.register(Exercise)
admin.site.register(Programme)
admin.site.register(ProgrammeLog)
admin.site.register(WeightSet)
admin.site.register(WeightConfig)
admin.site.register(Workout)
admin.site.register(WorkoutDetail)
