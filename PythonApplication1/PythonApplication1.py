import math
class Pessoa:

  def __init__(self, nome1, idade1, nome2, idade2):
      self.nome1 = nome1
      self.idade1 = idade1
      self.nome2 = nome2
      self.idade2 = idade2 
   
  def getPessoaMaisVelha(self):
      if(self.idade1 < self.idade2):
          return self.nome2
      elif(self.idade1 > self.idade2):
          return self.nome1
      else:
          return "Ambos tem a mesma idade: "+self.nome1+", "+self.nome2

class FuncionarioQuestao2:

  def __init__(self, nome1, salario1, nome2, salario2):
      self.nome1 = nome1
      self.salario1 = salario1
      self.nome2 = nome2
      self.salario2 = salario2 
   
  def getMediaSalario(self):
      return (self.salario1+self.salario2)/2

class Retangulo:

  def __init__(self, altura, largura):
      self.altura = altura
      self.largura = largura
   
  def getArea(self):
      return self.altura*self.largura

  def getPerimetro(self):
      return 2*(self.altura+self.largura)

  def getDiagonal(self):
      return  math.sqrt(((self.altura*self.altura)+(self.largura*self.largura)))

class Funcionario:

  def __init__(self, nome, salarioBruto, imposto):
      self.nome = nome
      self.salarioBruto = salarioBruto
      self.imposto = imposto
    
  def setPorcentagem(self, porcentagem):
      self.porcentagem = porcentagem

  def getFuncionario(self):
      return self.nome

  def getFuncionarioSalarioLiquido(self):
      return self.salarioBruto-self.imposto

  def getDadosAtualizados(self):
      return self.nome

  def getFuncionarioSalarioNovo(self):
      return (self.salarioBruto+(self.salarioBruto*(self.porcentagem/100)))-self.imposto

class Aluno:

  def __init__(self, nome, nota1, nota2, nota3):
      self.nome = nome
      self.nota1 = nota1
      self.nota2 = nota2
      self.nota3 = nota3

  def getNotaFinal(self):
      return self.nota1+self.nota2+self.nota3

  def getStatuAluno(self):
      if((self.nota1+self.nota2+self.nota3)>59):
          return "APROVADO"
      else:
          return "REPROVADO"
    
  def getFaltouNotaAluno(self):
      return 60-(self.nota1+self.nota2+self.nota3)

condicao = 0;

while(condicao !=9):
     print("Qual questão você quer visualizar? Digite 9, para sair do programa. ");
     print("QUESTÃO 1: Fazer um programa para ler os dados de duas pessoas, depois mostrar o nome da pessoa mais velha.");
     print("    ");
     print("QUESTÃO 2: Fazer um programa para ler nome e salário de dois funcionários. Depois, mostrar o salário médio dos funcionários.  ");
     print("    ");
     print("QUESTÃO 3: Fazer um programa para ler os valores da largura e altura de um retângulo. Em seguida, mostrar na tela o valor de sua área, perímetro e diagonal. Usar uma classe como mostrado no projeto ao lado.");
     print("    ");
     print("QUESTÃO 4: Fazer um programa para ler os dados de um funcionário (nome, salário bruto e imposto). Em seguida, mostrar os dados do funcionário (nome e salário líquido). Em seguida, aumentar o salário do funcionário com base em uma porcentagem dada (somente o salário bruto é afetado pela porcentagem) e mostrar novamente os dados do funcionário. ");
     print("    ");
     print("QUESTÃO 5: Fazer um programa para ler o nome de um aluno e as três notas que ele obteve nos três trimestres do ano (primeiro trimestre vale 30 e o segundo e terceiro valem 35 cada). Ao final, mostrar qual a nota final do aluno no ano. Dizer também se o aluno está APROVADO ou REPROVADO e, em caso negativo, quantos pontos faltam para o aluno obter o mínimo para ser aprovado (que é 60 pontos). Você deve criar uma classe Aluno para resolver este problema.");
     condicao = int(input("Alternativa?: "))
     if(condicao == 1):
         print('\n' * 30)
         print("Dados da primeira pessoa: ")
         NomePessoa1 = input("Nome: ")
         IdadePessoa1 = int(input("Idade: "))
         print("Dados da segunda pessoa: ")
         NomePessoa2 = input("Nome: ")
         IdadePessoa2 = int(input("Idade: "))
         p = Pessoa(NomePessoa1, IdadePessoa1, NomePessoa2, IdadePessoa2)
         print("Pessoa mais velha: "+ p.getPessoaMaisVelha())
         print("    ");
         print("Digite 1 para voltar ao menu principal ou digite qualquer outra coisa para sair: ")
         continuar = int(input("Continuar? "))
         if(continuar == 1):
              print('\n' * 30)
         else:
            break
     elif(condicao ==2):
         print('\n' * 30)
         print("Dados do primeiro funcionario: ")
         NomeFuncionario1 = input("Nome: ")
         IdadeFuncionario1 = float(input("Salário: "))
         print("Dados do segundo funcionario: ")
         NomeFuncionario2 = input("Nome: ")
         IdadeFuncionario2 = float(input("Salário: "))
         f = FuncionarioQuestao2(NomeFuncionario1, IdadeFuncionario1, NomeFuncionario2, IdadeFuncionario2)
         print("Salário médio = "+ str(f.getMediaSalario()))
         print("    ");
         print("Digite 1 para voltar ao menu principal ou digite qualquer outra coisa para sair: ")
         continuar = int(input("Continuar? "))
         if(continuar == 1):
              print('\n' * 30)
         else:
            break
     elif(condicao ==3):
         print('\n' * 30)
         print("Entre a largura e altura do retângulo: ")
         altura = float(input("Altura: "))
         largura = float(input("Largura: "))
         r = Retangulo(altura, largura)
         print("AREA = "+ str(r.getArea()))
         print("PERÍMETRO = "+ str(r.getPerimetro()))
         print("DIAGONAL = "+ str(r.getDiagonal()))
         print("    ");
         print("Digite 1 para voltar ao menu principal ou digite qualquer outra coisa para sair: ")
         continuar = int(input("Continuar? "))
         if(continuar == 1):
              print('\n' * 30)
         else:
            break
     elif(condicao ==4):
         print('\n' * 30)
         nome = input("Nome: ")
         salarioBruto = float(input("Salário Bruto: "))
         imposto = float(input("Imposto: "))
         f = Funcionario(nome, salarioBruto, imposto)
         print("Dados atualizado: "+ f.getFuncionario()+ ", R$ "+ str(f.getFuncionarioSalarioLiquido()))
         porcentagem = float(input("Digite a porcentagem para aumentar o salário: "))
         f.setPorcentagem(porcentagem)
         print("Dados atualizado: "+ f.getDadosAtualizados()+ ", R$ "+ str(f.getFuncionarioSalarioNovo()))
         
         print("    ")
         print("Digite 1 para voltar ao menu principal ou digite qualquer outra coisa para sair: ")
         continuar = int(input("Continuar? "))
         if(continuar == 1):
              print('\n' * 30)
         else:
            break
     elif(condicao ==5):
         print('\n' * 30)
         nota1 = 31
         nota2 = 36
         nota3 = 36
         nome = input("Nome do Aluno: ")
         print("Digite as 3 notas do aluno: ")
         while (nota1 >30):
            nota1 = float(input("Nota 1: "))
            if (nota1 >30):
                print("A 1° nota do aluno não deve superior a 30")
         while (nota2 >35):
            nota2 = float(input("Nota 2: "))
            if (nota2 >35):
                print("A 2° nota do aluno não deve superior a 35")       
         while (nota3 >35):
            nota3 = float(input("Nota 3: "))
            if (nota3 >30):
                print("A 3° nota do aluno não deve superior a 35")
         a = Aluno(nome, nota1, nota2, nota3)
         print("    ");
         print("NOTA FINAL = " + str(a.getNotaFinal()))
         if (a.getStatuAluno() == 'REPROVADO'):
             print(str(a.getStatuAluno()))
             print("FALTARAM "+str(a.getFaltouNotaAluno())+" PONTOS")
         else:  
            print(str(a.getStatuAluno()))
         print("    ")
         print("Digite 1 para voltar ao menu principal ou digite qualquer outra coisa para sair: ")
         continuar = int(input("Continuar? "))
         if(continuar == 1):
              print('\n' * 30)
         else:
            break
     elif(condicao ==9):
         print("Finalizado com sucesso")
         break
     else:
         print("Escolha uma alternativa valida...")    


