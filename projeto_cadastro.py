import random

nome = input("Informe o nome do aluno: ")
sobrenome = input("Informe o sobrenome do aluno: ")
idade = int(input("Informe a idade do aluno: "))
email = input("Digite o email do aluno: ")
renda_fam = input("Informe a renda familiar do aluno em salários mínimos: ")
filiacao_mae = input("Informe o nome da mãe do aluno: ")
filiacao_pai = input("Informe o nome do pai do aluno: ")
cpf = int(input("Digite o CPF do aluno: "))
escolaridade = input("Selecione o nível de escolaridade do aluno: \n1-Ensino Fundamental\n2-Ensino Médio\n")
nota_enem = int(input("Insira a nota do ENEM: "))
txt = input("A matrícula do aluno é ")
matricula = int(input(random.randint(1000,9999) ))
cadastro = [nome,sobrenome, idade, email, renda_fam, filiacao_mae, filiacao_pai, cpf, escolaridade, nota_enem, matricula]
match escolaridade:
    case 1: print("O aluno está adiantado para fazer o ENEM.")
    case 2: print("O aluno está no tempo adequado.")

while idade < 16:
    print("O aluno é novo demais para fazer a prova.")
    idade = int(input("A partir dos 16 anos o aluno poderá fazer o ENEM."))


if nota_enem >= 500:
       print("O aluno passou na média.")
else:
       print("A nota do aluno está abaixo da média.")

def renda_fam(renda):
    if renda <= 1:
       print("O aluno ganhará bolsa de 100%!")
    elif renda <=2:
        print("O aluno ganhará bolsa de 50%!")
    elif renda <=3:
        print("O aluno ganhará bolsa de 30%!")
    elif renda > 4:
        print("O aluno não garante a bolsa.")

for x in cadastro:
    print(x)