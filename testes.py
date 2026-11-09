import unittest;
from aluno import AlunoClass; 
from turma import TurmaClass;
from conexao import ConexaoClass;
import mongomock;


class alunoTest(unittest.TestCase):
  @mongomock.patch(servers=(('localhost.com', 27017),))
  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.aluno = AlunoClass('Fabio', 'Teixeira', 10);
    self.turma = TurmaClass();
    self.turma.cadastrarAlunos([self.aluno]);
    self.conexao = ConexaoClass.conexaoMongoDB(self, url = 'localhost.com', banco = 'faculdade')

  def test_salvarAluno(self):   
        resposta = self.aluno.salvar(conexao = self.conexao, colecao = 'aluno');  
        self.assertEqual(True, resposta, 'Aluno cadastrado incorretamente!');
    
#instancia o aluno, chama o .salvar() passando a conexão simulada pelo @mongomock.patch 
#valida com o self.assertEqual(True, resposta, ...) se o retorno foi bem-sucedido.
#assertEqual compara o primeiro argumento (True, que é o que eu espero) com o segundo argumento (resposta, que é o valor real retornado pelo método .salvar()).
#Se por algum motivo o método .salvar() retornar False (ou algo diferente de True), o teste vai falhar.
#É nesse momento que o Python exibe a mensagem 'Aluno cadastrado incorretamente!'
  
  def test_salvarTurma(self):   
    resposta = self.turma.salvar(conexao = self.conexao, colecao = 'turma');  
    self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!');

if __name__ == "__main__":
  unittest.main()
