import random

class Pessoa:
    def __init__(self, cpf, idade, raca, genero, nacionalidade, nome):
        self.cpf = cpf
        self.idade = idade
        self.raca = raca
        self.genero = genero
        self.nacionalidade = nacionalidade
        self.nome = nome

class Discente(Pessoa):
    def __init__(self, cpf, idade, raca, genero, nacionalidade, nome,renda, pcd, financiamento, codigoEmec, status, anoMatricula, CR):
        super().__init__(cpf, idade, raca, genero, nacionalidade, nome)
        self.renda = renda
        self.pcd = pcd
        self.financiamento = financiamento
        self.codigoEmec = codigoEmec
        self.status = status
        self.anoMatricula = anoMatricula
        self.CR = CR

class Docente(Pessoa):
    def __init__(self, cpf, idade, raca, genero, nacionalidade, nome, titularidade):
        super().__init__(cpf, idade, raca, genero, nacionalidade, nome)
        self.titularidade = titularidade
    
    def mostrar_informacoes(self):
        print("=== Informações do Docente ===")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Gênero: {self.genero}")
        print(f"Nacionalidade: {self.nacionalidade}")
        print(f"Titularidade: {self.titularidade}")

def gerador_de_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(11)])

def gerar_raca():
    racas = ['Branca', 'Negra', 'Parda', 'Amarela', 'Indígena']
    return random.choice(racas)

def gerar_genero():
    generos = ['Masculino', 'Feminino']
    return random.choice(generos)

def gerar_nacionalidade():
    if random.random() < 0.9:
        return 'Brasileira'
    else:
        nacionalidades = ['Portugal', 'Argentina', 'Colombia', 'Mexico', 'Franca', 'Alemanha', 'Austria', 'EUA', 'Japao', 'China', 'Russia' ]
        return random.choice(nacionalidades)
    
def gerar_idade_prof():
    pesos = [1 if 30 <= i < 50 or 60 < i <= 75 else 5 for i in range(30, 76)]
    return random.choices(range(30, 76), weights=pesos, k=1)[0]

def gerar_titularidade():
    titularidades = ['Adjunto', 'Substituto', 'Agregado', 'Titular', 'Emerito']
    return random.choice(titularidades)

def gerar_nome():
    nomes_masculinos = [
    "Adriano", "Alan", "Alexandre", "André", "Antonio", "Bruno", "Caio", "Carlos",
    "César", "Daniel", "Diego", "Eduardo", "Fábio", "Felipe", "Fernando", "Francisco",
    "Gabriel", "Guilherme", "Gustavo", "Henrique", "Hugo", "Igor", "João", "José",
    "Juliano", "Leonardo", "Lucas", "Luís", "Marcelo", "Marcos", "Mateus", "Matheus",
    "Miguel", "Nicolas", "Pedro", "Rafael", "Ricardo", "Rodrigo", "Samuel", "Thiago", "Tiago", "Vinícius"
]

    nomes_femininos = [
    "Adriana", "Alice", "Amanda", "Ana", "Beatriz", "Bianca", "Bruna", "Camila",
    "Carla", "Catarina", "Clara", "Daniela", "Elaine", "Elisa", "Eduarda", "Fernanda", "Gabriela",
    "Helena", "Isabela", "Jéssica", "Joana", "Juliana", "Larissa", "Laura", "Letícia", "Lívia",
    "Luana", "Luiza", "Manuela", "Maria", "Maria Clara", "Maria Eduarda", "Mariana", "Natália", "Patrícia", "Paula",
    "Raquel", "Renata", "Rita", "Sabrina", "Sara", "Tatiana", "Thaís", "Valéria", "Vanessa", "Yasmin"
    ]

    sobrenomes = [
    "Almeida", "Alves", "Andrade", "Araujo", "Barbosa", "Barros", "Batista", "Borges", 
    "Campos", "Cardoso", "Carvalho", "Castro", "Cavalcanti", "Costa", "Dias", "Duarte", 
    "Fernandes", "Ferreira", "Freitas", "Garcia", "Gomes", "Gonçalves", "Lima", "Lopes", 
    "Machado", "Martins", "Melo", "Mendes", "Monteiro", "Moraes", "Moreira", "Nogueira", 
    "Oliveira", "Pereira", "Pinto", "Ramos", "Rezende", "Ribeiro", "Rocha", "Santos", 
    "Silva", "Souza", "Teixeira", "Vieira"
    ]

    # Escolher se será masculino ou feminino
    if random.random() < 0.5:
        nome = random.choice(nomes_masculinos)
        genero = 'M'
    else:
        nome = random.choice(nomes_femininos)
        genero = 'F'
    
    sobrenome1 = random.choice(sobrenomes)
    sobrenome2 = random.choice(sobrenomes)
    
    # Garantir que os dois sobrenomes sejam diferentes
    while sobrenome1 == sobrenome2:
        sobrenome2 = random.choice(sobrenomes)
    
    nome_completo = f"{nome} {sobrenome1} {sobrenome2}"
    
    return nome_completo, genero

def cria_docente():
    cpf = gerador_de_cpf()
    idade = gerar_idade_prof()
    nome, genero = gerar_nome()
    raca = gerar_raca()
    nacionalidade = gerar_nacionalidade()
    titularidade = gerar_titularidade()
    return Docente(cpf, idade, raca, genero, nacionalidade, nome, titularidade)

def main():
    #Fazendo um elemento da classe Docente
    docente = cria_docente()
    docente.mostrar_informacoes()
        
    

if __name__ == '__main__':
    main()