class TurmaClass:
  def __init__(self):
    self.turma = []; #Uma lista de alunos da turma (self.turma).
    self.menorNota = None; #Um objeto representando o aluno com a menor nota
    self.maiorNota = None; #Um objeto representando o aluno com a maior nota

  def cadastrarAlunos(self, alunos):    
    for i in alunos:      #percorre por cada aluno
      if(i.nota <= 10 and i.nota >= 0): #verifica se a nota está entre 0 e 10
        self.turma.append(i); #adiciona na lista de alunos da turma
        if((self.menorNota == None) or (self.menorNota.nota > i.nota)): #se a menor nota for maior que a nota do aluno atual
          self.menorNota = i; #menor nota é do aluno atual   
        if((self.maiorNota == None) or (self.maiorNota.nota < i.nota)): #se a maior nota for menor que a do aluno atual
          self.maiorNota = i;  #maior nota é do aluno atual         

  def mostrarAlunos(self):  
    print('Quantidade de alunos:', len(self.turma)); #conta os elementos totais da lista
    for x in self.turma:      
      print(x.mostrarAluno()); 

  #esse metodo faz uma conversao manual para dicionario e depois insere 
  def salvar(self, conexao, colecao):    
    mydict = self.__dict__;
    mydict['turma'] = [i.__dict__ for i in self.turma] #Percorre a lista de alunos e transforma cada objeto aluno da lista em um dicionário individual
    mydict['menorNota'] = self.menorNota.__dict__; #Pega o objeto do aluno com a menor nota e o transforma em dicionário.
    mydict['maiorNota'] = self.maiorNota.__dict__;#Pega o objeto do aluno com a maior nota e o transforma em dicionário
    x = conexao[colecao].insert_one(mydict)    #insere
    return x.acknowledged;

