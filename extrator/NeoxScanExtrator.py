from utils.class_robo.robo import Robo
from models.robo_models import OptionsRobo


class NeoxScanExtrator:
    def __init__(self):
        self.robo = Robo(OptionsRobo('GET', 'https://neoxscans.net/', False))

    def extrair(self):
        self.primeiro_acesso()

    def primeiro_acesso(self):
        pass