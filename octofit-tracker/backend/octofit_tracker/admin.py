from django.contrib import admin
from .models import Team, Activity, Leaderboard, Workout

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'team')

class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('team', 'points')

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty')

admin.site.register(Team, TeamAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Leaderboard, LeaderboardAdmin)
admin.site.register(Workout, WorkoutAdmin)
