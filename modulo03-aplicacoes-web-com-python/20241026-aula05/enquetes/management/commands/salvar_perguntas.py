import datetime
import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from enquetes.models import Pergunta, Opcao

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

            for pergunta in conteudo:
                
                nova_pergunta = Pergunta(
                    texto=pergunta.get("pergunta"),
                    data_publicacao=datetime.datetime.now(datetime.timezone.utc)
                )

                nova_pergunta.save()

                for opcao in pergunta.get("opcoes"):
                    Opcao(
                        pergunta=nova_pergunta,
                        texto=opcao.get("texto"),
                        votos=int(opcao.get("votos"))
                    ).save()


        except Exception as exc_info:
            self.stderr.write(f"Erro ao salvar: {exc_info}")