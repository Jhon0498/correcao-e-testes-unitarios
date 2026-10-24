
class Turma:
    def __init__(self):
        # Inicia a lista de alunos com o mínimo e máximo
        self.turma = []
        self.menorNota = None
        self.maiorNota = None

    def cadastrarAlunos(self, alunos):
        # Percorre a lista de aluno recebida
        for i in alunos:
            # Ignora o que tiver fora de 0 a 10
            if not 0 <= i.nota <= 10:
                continue

            self.turma.append(i)

            # Atualiza a menor nota encontrada
            if (self.menorNota is None) or (self.menorNota.nota > i.nota):
                self.menorNota = i

            # Atualiza a maior nota encontrada
            if (self.maiorNota is None) or (self.maiorNota.nota < i.nota):
                self.maiorNota = i

    def mostrarAlunos(self):
        # Exibe a quantidade de alunos cadastrados com notas válidas
        print('Quantidade de alunos:', len(self.turma))

        # Exibe os dados de cada aluno
        for x in self.turma:
            print(x.mostrarAluno())
