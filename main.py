import mysql.connector


def menu():
    print('\nMENU')
    print('[1] Cadastrar\n[2] Mostrar cadastros\n[3] Atualizar cadastro\n[4] Excluir cadastro\n[0] Sair')


def createClient():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    nome = str(input('Nome: '))
    cpf = str(input('CPF (apenas números): '))
    telefone = str(input('Telefone (apenas números): '))
    email = str(input('Email: '))
    logradouro = str(input('Logradouro: '))
    numero = int(input('Número: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    uf = str(input('UF: '))
    cep = str(input('CEP (apenas números): '))

    save = int(input('Salvar?\n[1] Sim\n[2] Não\n'))
    if save == 1:
        cursor.execute('INSERT INTO cliente (`nome`, `cpf`, `telefone`, `email`, `logradouro`, `numero`, `bairro`, '
                       '`cidade`, `uf`, `cep`) VALUES ("%s", "%s", "%s", "%s", "%s", %d, "%s", "%s", "%s", '
                       '"%s")' % (nome, cpf, telefone, email, logradouro, numero, bairro, cidade, uf, cep))
        conexao.commit()
        cursor.close()
        conexao.close()
    print(f'Cadastrado o cliente de ID', cursor.lastrowid)


def readClient():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM cliente')
    resultado = cursor.fetchall()
    for row in resultado:
        print('ID: ', row[0])
        print('Nome: ', row[1])
        print('CPF: ', row[2])
        print('Telefone: ', row[3])
        print('Email: ', row[4])
        print(row[5], row[6], row[8], '-', row[9], row[10])
        print("\n")
    cursor.close()
    conexao.close()


def updateClient():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    nome = str(input('Nome: '))
    cpf = str(input('CPF (apenas números): '))
    telefone = str(input('Telefone (apenas números): '))
    email = str(input('Email: '))
    logradouro = str(input('Logradouro: '))
    numero = int(input('Número: '))
    bairro = str(input('Bairro: '))
    cidade = str(input('Cidade: '))
    uf = str(input('UF: '))
    cep = str(input('CEP (apenas números): '))
    id_cliente = int(input('Digite o ID do cliente que deseja atualizar: '))

    save = int(input('Salvar?\n[1] Sim\n[2] Não\n'))
    if save == 1:
        cursor.execute('UPDATE cliente SET nome = "%s", cpf = "%s", telefone = "%s", email = "%s", '
                       'logradouro = "%s", numero = %d, bairro = "%s", cidade = "%s", uf = "%s", cep = "%s", '
                       'WHERE id_cliente = %d' % (nome, cpf, telefone, email, logradouro, numero, bairro, cidade, uf,
                                                  cep, id_cliente))
        conexao.commit()
        cursor.close()
        conexao.close()


def deleteClient():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    ids = int(input('Insira o ID do cliente que deseja excluir: '))
    exc = int(input(f'Excluir cliente de ID = {ids}?\n[1] Sim\n[2] Não\n'))
    if exc == 1:
        cursor.execute(f'DELETE FROM cliente WHERE id_cliente = {ids}')
        conexao.commit()
        cursor.close()
        conexao.close()


def createBook():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    isbn = str(input('ISBN (apenas números): '))
    titulo = str(input('Nome: '))
    autor = str(input('Autor: '))
    genero = str(input('Gênero: '))
    editora = str(input('Editora: '))
    qtd_estoque = int(input('Quantidade no estoque: '))
    preco = float(input('Preço: '))

    save = int(input('Salvar?\n[1] Sim\n[2] Não\n'))
    if save == 1:
        cursor.execute('INSERT INTO livro (`isbn`, `titulo`, `autor`, `genero`, `editora`, `qtd_estoque`, `preco`) '
                       'VALUES ("%s", "%s", "%s", "%s", "%s", %d, %f)' % (isbn, titulo, autor, genero, editora,
                                                                          qtd_estoque, preco))
        conexao.commit()
        cursor.close()
        conexao.close()
    print(f'Cadastrado o livro de ISBN {isbn}')


def readBook():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM livro')
    resultado = cursor.fetchall()
    for row in resultado:
        print('ISBN: ', row[0])
        print('Nome: ', row[1])
        print('Autor: ', row[2])
        print('Gênero: ', row[3])
        print('Editora: ', row[4])
        print('Quantidade: ', row[5])
        print('Preço: ', row[6])
        print('\n')
    cursor.close()
    conexao.close()


def updateBook():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    isbn = str(input('ISBN (apenas números): '))
    titulo = str(input('Nome: '))
    autor = str(input('Autor: '))
    genero = str(input('Gênero: '))
    editora = str(input('Editora: '))
    qtd_estoque = int(input('Quantidade no estoque: '))
    preco = float(input('Preço: '))
    newisbn = int(input('Digite o ISBN do livro que deseja atualizar (apenas números): '))

    save = int(input('Salvar?\n[1] Sim\n[2] Não\n'))
    if save == 1:
        cursor.execute('UPDATE livro SET isbn = "%s", titulo = "%s", autor = "%s", genero = "%s", editora = "%s", '
                       f'qtd_estoque = %d, preco = %f WHERE isbn = {newisbn}' % (isbn, titulo, autor, genero, editora,
                                                                                 qtd_estoque, preco))
        conexao.commit()
        cursor.close()
        conexao.close()


def deleteBook():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin31ADMIN',
        database='livraria',
    )
    cursor = conexao.cursor()
    isbn = int(input('Insira o ISBN do livro que deseja excluir (apenas números): '))
    exc = int(input(f'Excluir livro de ISBN = {isbn}?\n[1] Sim\n[2] Não\n'))
    if exc == 1:
        cursor.execute(f'DELETE FROM livro WHERE isbn = {isbn}')
        conexao.commit()
        cursor.close()
        conexao.close()


option = 5
while option != 0:
    menu()
    option = int(input())

    if option == 1:
        while option == 1:
            ch = int(input('Cadastrar\n[1] Cliente\n[2] Livro\n'))
            if ch == 1:
                createClient()
            elif ch == 2:
                createBook()
            option = int(input('Continuar cadastrando?\n[1] Sim\n[2] Não\n'))

    elif option == 2:
        option = 1
        while option == 1:
            ch = int(input('Mostrar cadastro\n[1] Cliente\n[2] Livro\n'))
            if ch == 1:
                readClient()
            elif ch == 2:
                readBook()
            option = int(input('Continuar mostrando?\n[1] Sim\n[2] Não\n'))

    elif option == 3:
        option = 1
        while option == 1:
            ch = int(input('Atualizar cadastro\n[1] Cliente\n[2] Livro\n'))
            if ch == 1:
                updateClient()
            elif ch == 2:
                updateBook()
            option = int(input('Continuar atualizando?\n[1] Sim\n[2] Não\n'))

    elif option == 4:
        option = 1
        while option == 1:
            ch = int(input('Excluir cadastro\n[1] Cliente\n[2] Livro\n'))
            if ch == 1:
                deleteClient()
            elif ch == 2:
                deleteBook()
            option = int(input('Continuar excluindo?\n[1] Sim\n[2] Não\n'))
