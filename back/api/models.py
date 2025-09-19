from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255) # id é criado automaticamente (PK)
    sobrenome = models.CharField(max_length=255)
    data_nasc = models.DateField(null=True, blank=True)
    nacion = models.CharField(max_length=30, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True) # textField não tem tamanho definido

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
    

class Editora(models.Model):
    editora = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True)
    endereco = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)   # não precisa necessariamente preencher, por isso null = True

    def __str__(self):
        return self.editora

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE) # cascade se apagar, atualiza em varias tabelas 
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50)
    descricao = models.TextField()
    idioma = models.CharField(default='Português')  # se nao definir idioma, ele fica em portugues
    ano_pub = models.IntegerField() # integer = numeros inteiros apenas
    paginas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    desconto = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    dimensoes = models.CharField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.livro