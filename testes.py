
import unittest
import aluno as a
import turma as t


class turmaTest(unittest.TestCase):

    def setUp(self):
        # Exibe o nome do teste que está sendo executado.
        print('Teste', self._testMethodName, 'sendo executado...')

        # Cria a lista de alunos para os testes.
        self.alunos = []

        # Cadastra alunos com notas válidas e inválidas.
        self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10))
        self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8))
        self.alunos.append(a.Aluno('Melissa', 'Teixeira', -1))
        self.alunos.append(a.Aluno('Angela', 'Teixeira', 7))

        # Cria a turma e cadastra os alunos.
        self.turmaObject = t.Turma()
        self.turmaObject.cadastrarAlunos(self.alunos)

    def tearDown(self):
        # Exibe o nome do teste finalizado.
        print('Teste', self._testMethodName, 'finalizado.')

    def testMaior(self):
        # Verifica se a maior nota foi encontrada corretamente.
        self.assertEqual(
            10,
            self.turmaObject.maiorNota.nota,
            'Erro ao encontrar maior nota'
        )

    def testMenor(self):
        # Verifica se a menor nota foi encontrada corretamente.
        self.assertEqual(
            7,
            self.turmaObject.menorNota.nota,
            'Erro ao encontrar menor nota'
        )

    def testIntervalo(self):
        print('Testar se o intervalo de notas está correto.')

        # Verifica se todas as notas cadastradas estão entre 0 e 10.
        for aluno in self.turmaObject.turma:
            self.assertGreaterEqual(aluno.nota, 0)
            self.assertLessEqual(aluno.nota, 10)

        # Verifica se a aluna com nota inválida não foi cadastrada.
        self.assertNotIn(
            self.alunos[2],
            self.turmaObject.turma,
            'Aluno com nota inválida foi cadastrado'
        )

        # Verifica se somente os três alunos com notas válidas foram cadastrados.
        self.assertEqual(3, len(self.turmaObject.turma))

    def testLimitesNotas(self):
        # Testa se as notas 0 e 10 são aceitas.
        turmaLimites = t.Turma()

        alunosLimites = [
            a.Aluno('Aluno', 'Zero', 0),
            a.Aluno('Aluno', 'Dez', 10)
        ]

        turmaLimites.cadastrarAlunos(alunosLimites)

        # Verifica se os dois alunos foram cadastrados.
        self.assertEqual(2, len(turmaLimites.turma))

        # Verifica se a nota 0 é considerada a menor.
        self.assertEqual(0, turmaLimites.menorNota.nota)

        # Verifica se a nota 10 é considerada a maior.
        self.assertEqual(10, turmaLimites.maiorNota.nota)

    def testTurmaVazia(self):
        # Testa o comportamento de uma turma sem alunos.
        turmaVazia = t.Turma()

        # Verifica se a turma começa vazia.
        self.assertEqual(0, len(turmaVazia.turma))

        # Verifica se não existem menor e maior nota.
        self.assertIsNone(turmaVazia.menorNota)
        self.assertIsNone(turmaVazia.maiorNota)

    def testNotasIguais(self):
        # Testa uma turma em que todos os alunos possuem a mesma nota.
        turmaIgual = t.Turma()

        alunosIguais = [
            a.Aluno('Ana', 'Silva', 8),
            a.Aluno('João', 'Silva', 8)
        ]

        turmaIgual.cadastrarAlunos(alunosIguais)

        # Verifica se a menor e a maior nota são iguais a 8.
        self.assertEqual(8, turmaIgual.menorNota.nota)
        self.assertEqual(8, turmaIgual.maiorNota.nota)

        # Verifica se os dois alunos foram cadastrados.
        self.assertEqual(2, len(turmaIgual.turma))


if __name__ == "__main__":
    # Executa todos os testes unitários deste arquivo.
    unittest.main()
