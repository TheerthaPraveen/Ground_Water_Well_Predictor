from django.apps import AppConfig

#configure and register the Django app named prediction
# ensures proper registartion with the Djangos appliction registry.
class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prediction'
