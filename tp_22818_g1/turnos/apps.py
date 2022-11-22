from django.apps import AppConfig


class TurnosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'turnos'

#para el mapa
class MapConfig(AppConfig):
    name = 'map'
