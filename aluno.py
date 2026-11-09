class AlunoClass:
  def __init__(self, nome, sobrenome, nota):    
    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);    

# no método _init na classe aluno recebo o nome, sobrenome e nota como strings e numero.
#O método mostrar aluno concatena o nome, sobrenome e nota, enquanto transforma a nota em string. 

def salvar(self, conexao, colecao):
        # self.__dict__ já transforma os atributos (nome, sobrenome, nota) em dicionário automaticamente
        x = conexao[colecao].insert_one(self.__dict__) #inserção
        return x.acknowledged

