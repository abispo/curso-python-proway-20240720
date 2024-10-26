import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

import requests

class Command(BaseCommand):
    help = "Faz o download de perguntas"

    def add_arguments(self, parser):
        parser.add_argument("url", type=str)

    def handle(self, *args, **options):
        try:
            url = options.get("url")

            resposta = requests.get(
                url
            )

            if resposta.status_code != 200:
                self.stdout.write(
                    f"Não foi possível baixar o arquivo: Status code {resposta.status_code}"
                )

            else:
                downloads_dir = os.path.join(settings.BASE_DIR, "downloads")
                if not os.path.exists(downloads_dir):
                    os.mkdir(downloads_dir)

                caminho_arquivo = os.path.join(downloads_dir, "enquetes.json")

                with open(caminho_arquivo, 'w', encoding="utf-8") as arquivo:
                    arquivo.write(
                        json.dumps(resposta.json())
                    )

        except Exception as exc_info:
            self.stderr.write(f"Erro ao baixar arquivo: {exc_info}")