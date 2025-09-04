import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if o['truncate']: Livro.objects.all().delete()

        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["autor"] = 
        df["editora"] =
        df["isbn"] = pd.to_numeric(df["isbn"], errors= "coerce", downcast="integer")
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_pub"] = pd.to_numeric(df["ano_pub"], errors= "coerce", downcast="integer")
        df["paginas"] = pd.to_numeric(df["paginas"], errors= "coerce", downcast="integer")
        df["preco"] = pd.to_numeric(df["preco"], errors= "coerce", downcast="integer")
        df["estoque"] = pd.to_numeric(df["estoque"], errors= "coerce", downcast="integer")
        df["desconto"] = pd.to_numeric(df["desconto"], errors= "coerce", downcast="integer")
        df["disponivel"] = df["disponivel"].map({"True": True, "False": False})
        df["dimensoes"] = df["dimensoes"].astype(str).str.strip()
        df["peso"] = pd.to_numeric(df["peso"], errors= "coerce", downcast="integer")



