import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

import requests

class Command(BaseCommand):
    help = "Salva as perguntas no banco de dados"

    def add_arguments(self, parser):
        parser.add_argument("arquivo", type=str)

    def handle(self, *args, **options):
        try:
            arquivo = options.get("arquivo")
            caminho_arquivo = os.path.join(
                settings.BASE_DIR,
                "downloads",
                arquivo
            )

            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = json.load(arquivo)
                self.stdout.write(json.dumps(conteudo))

        except Exception as exc_info:
            self.stderr.write(f"Erro ao baixar arquivo: {exc_info}")