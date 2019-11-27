biblioteca = {}
alunos={}
livrosEmprestados = {}
aluno = []

index = input("digite o que deseja fazer: "+
              "\n"+"1 - cadastrar livros"+
              "\n"+"2 - cadastrar alunos"+
              "\n"+"3 - consultar aluno"+
              "\n"+"4 - consultar livro"+
              "\n"+"5 - empréstimo"+
              "\n"+"6 - devolução e pagamento"+
              "\n"+"7 - relatório"+
              "\n"+"8 - sair"+
              "\n")
#-----------------------------------------------------------------------------------------------

while index != "8":
    if index == "1":
        print()
        qtdLivros = int(input("digite a quantidade de livros que deseja cadastrar: "))
        print()
        for l in range(qtdLivros):
            print()
            nomeLivro = input("digite o nome do livro que deseja cadastrar: ").upper()
            exemplarLivro = int(input("digite quantos exemplares do livro "+nomeLivro+" estão disponíveis: "))
            biblioteca[nomeLivro] = exemplarLivro

    if index =="2":
        print()
        qtdAlunos = int(input("digite a quantidade de alunos que deseja cadastrar: "))
        for a in range(qtdAlunos):
            print()
            nomeAluno = input("digite o nome do aluno: ").upper()
            matriculaAluno = int(input("digite a matrícula de "+nomeAluno+ " : "))
            aluno.append(nomeAluno)
        alunos[matriculaAluno] = nomeAluno

    if index == "3":
        print()
        consultaMatriculaAluno = int(input("digite a matrcula do aluno que deseja consultar: "))
        if consultaMatriculaAluno in alunos.keys():
            print()
            print("o aluno está cadastrado!")
        else:
            print()
            print("o aluno não etá cadastrado!")

    if index == "4":
        print()
        consultaQtdLivros = input("digite o nome do livro que deseja consultar: ").upper()
        if consultaQtdLivros in biblioteca.keys():
            print()
            print("há exemplares disponíveis!")
            print("quantidade: ", exemplarLivro)
        else:
            print()
            print("não há exemplares disponíveis!")

    if index == "5":
        dataEmprestimo = input("digite a data do empréstimo: ")
        print()
        print("livros disponíveis: ")
        print()
        print(biblioteca)
        print()
        emprestimoAluno = input("digite a matricula do aluno: ")
        qtdLivro = int(input("digite a quantidade de livros que " + emprestimoAluno + " deseja retirar:"))
        listaLivro = []
        for q in range(qtdLivro):
            print()
            emprestimoLivro = input("digite o nome do livro que " + emprestimoAluno + " deseja retirar: ").upper()
            if emprestimoAluno in biblioteca.keys():
                 qtdEmprestimo = int(input("digite quantos livros de " + emprestimoLivro + " o aluno deseja retirar: "))
                 listaLivro.append(emprestimoLivro)
                 exemplarLivro -= qtdEmprestimo
                 dataDevolucao = input("digite a data de devolução: ")

            else:
                print()
                print("não há livros disponíveis!")

        livrosEmprestados[emprestimoAluno] = listaLivro
        print()
        print("quantidade de exemplares disponíveis: ", exemplarLivro)
        print("quantidade de livros emprestados: ", livrosEmprestados)
        if livrosEmprestados > 3:
             print()
             print("o aluno nao pode pegar livros emprestados, pois ultrapassou o limite")

    if index == "6":
        pagamento = 0
        multa = 0
        devolucaoAluno = input("digite matricula do aluno: ")
        if devolucaoAluno in livrosEmprestados.keys():
            dataEntrega = int(input('digite a data de entrega do aluno ' + devolucaoAluno + ' : '))
            print(livrosEmprestados[devolucaoAluno])
            devolvendo = input('digite o nome do livro que deseja desvolver: ')
            if devolvendo in livrosEmprestados[devolucaoAluno]:
                if dataEntrega != dataDevolucao:
                    print('devolução fora do prazo!', '\n',
                          devolucaoAluno + ' será penalizado com uma multa de R$30,00 para cada mês')
                    if dataEntrega > 1:
                        pagamento += 1
                        multa = pagamento * 30
                        print(multa, pagamento)
                else:
                    livrosEmprestados[devolucaoAluno].remove(devolvendo)
                    print(livrosEmprestados[devolucaoAluno])
                    print('ainda está dentro do prazo!')

    if index == "7":
        print()
        print("livros: ", livrosEmprestados)
        print()
        print("numero de livros emprestados: ", exemplarLivro)

    print()
    index = input("digite o que deseja fazer: "+
              "\n"+"1 - cadastrar livros ok"+
              "\n"+"2 - cadastrar alunos ok"+
              "\n"+"3 - consultar aluno ok"+
              "\n"+"4 - consultar livro ok"+
              "\n"+"5 - empréstimo"+
              "\n"+"6 - devolução e pagamento"+
              "\n"+"7 - relatório"+
              "\n"+"8 - sair"+
              "\n")

print()
print(" por utilizar o programa!")