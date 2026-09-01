import os  # 'import' traz o módulo 'os' (sistema operacional) para usar a função 'os.path.exists' mais adiante

# CORES (Códigos de escape ANSI armazenados em variáveis do tipo string para estilizar o texto do terminal)
CYAN = "\033[96m"  # Variável string para a cor ciano claro
GREEN = "\033[92m"  # Variável string para a cor verde claro
BLUE = "\033[94m"  # Variável string para a cor azul claro
YELLOW = "\033[93m"  # Variável string para a cor amarela
RED = "\033[91m"  # Variável string para a cor vermelha clara
GRAY = "\033[90m"  # Variável string para a cor cinza
MAGENTA = "\033[95m"  # Variável string para a cor roxa/magenta
WHITE = "\033[97m"  # Variável string para a cor branca
RESET = "\033[0m"  # Variável string que remove todas as cores e restaura o padrão do terminal

ARQUIVO = "alunos.txt"  # Variável constante que guarda o nome do arquivo de texto que servirá de banco de dados

def separador(char: str = "=", largura: int = 45):  # 'def' define a função, com parâmetros que possuem tipagem (str, int) e valores padrão ('=' e 45)
    print(f"{CYAN}{char * largura}{RESET}")  # 'print' exibe uma f-string que aplica a cor CYAN, multiplica o caractere pela largura e aplica o RESET

def exibir_menu():  # 'def' define a função 'exibir_menu' que não recebe parâmetros e serve para desenhar a interface
    separador()  # Executa a função 'separador()' usando os argumentos padrão dela
    print(f"{CYAN}{'SISTEMA DE ALUNOS':^45}{RESET}")  # 'print' com f-string usando o modificador ':^45' para centralizar o texto em um bloco de 45 espaços
    separador()  # Executa novamente a função 'separador()' para fechar o cabeçalho do menu

    print(f"{GREEN}1 - Cadastrar aluno{RESET}")  # 'print' exibe a opção 1 concatenada com a variável de cor verde e redefinida com o reset
    print(f"{BLUE}2 - Listar alunos{RESET}")  # 'print' exibe a opção 2 concatenada com a variável de cor azul e redefinida com o reset
    print(f"{YELLOW}3 - Alterar aluno{RESET}")  # 'print' exibe a opção 3 concatenada com a variável de cor amarela e redefinida com o reset
    print(f"{RED}4 - Excluir aluno{RESET}")  # 'print' exibe a opção 4 concatenada com a variável de cor vermelha e redefinida com o reset
    print(f"{GRAY}0 - Sair{RESET}")  # 'print' exibe a opção 0 concatenada com a variável de cor cinza e redefinida com o reset
    print()  # 'print()' sem argumentos serve exclusivamente para pular uma linha na tela

def cadastrar_aluno():  # 'def' cria a função que encapsula toda a lógica de inserção de novos dados
    print(f"\n{YELLOW}===== CADASTRAR ALUNO ====={RESET}")  # 'print' exibe o título da ação usando '\n' para pular linha e a cor amarela
    
    while True:
        nome = input("Digite o nome do aluno: ").strip()  # 'input()' recebe o texto digitado e '.strip()' remove espaços inúteis no início e fim da string
        if not nome:
            print(f"{RED}O nome não pode ficar em branco.{RESET}")
        elif nome.isdigit():
            print(f"{RED}O nome não pode ser composto apenas por números.{RESET}")
        else:
            break

    while True:  # 'while True' inicia um laço de repetição infinito que só será interrompido manualmente
        try:  # 'try' abre um bloco de teste para capturar erros de conversão que o usuário possa causar
            nota = float(input("Digite a nota do aluno: ").strip())  # 'input' lê, '.strip()' limpa e 'float()' tenta converter o texto para número decimal
            break  # 'break' interrompe o laço 'while' imediatamente se a conversão do float funcionar sem erros
        except ValueError:  # 'except' captura especificamente o erro 'ValueError' caso o 'float()' receba letras em vez de números
            print(f"{RED}Digite apenas números.{RESET}")  # 'print' exibe o aviso de erro formatado na cor vermelha

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:  # 'with' gerencia o arquivo, 'open()' abre no modo append ('a') com charset 'utf-8', apelidando-o de 'arquivo'
        arquivo.write(f"{nome};{nota}\n")  # Método '.write()' grava a f-string contendo as variáveis separadas por ';' e adiciona o quebra-linha '\n'

    print(f"{GREEN}Aluno cadastrado com sucesso!{RESET}")  # 'print' exibe a mensagem de sucesso colorida em verde

def listar_alunos():  # 'def' define a função responsável por ler, tratar e formatar os dados do arquivo na tela
    if not os.path.exists(ARQUIVO):  # 'if not' inverte o booleano de 'os.path.exists()', que verifica se o arquivo físico NÃO existe no computador
        print(f"{RED}Nenhum aluno cadastrado ainda.{RESET}")  # 'print' avisa em vermelho que o banco de dados/arquivo ainda não foi criado
        return  # 'return' encerra a execução da função imediatamente, impedindo o código abaixo de rodar

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:  # 'with' abre o arquivo de forma segura em modo leitura ('r') com codificação UTF-8
        linhas = arquivo.readlines()  # Método '.readlines()' lê o arquivo inteiro e transforma cada linha em um elemento de uma lista de strings

    if not linhas:  # 'if not' avalia se a lista 'linhas' está vazia (retorna True se estiver vazia)
        print(f"{YELLOW}Nenhum aluno cadastrado ainda.{RESET}")  # 'print' avisa em amarelo que o arquivo existe mas está sem nenhum texto dentro
        return  # 'return' encerra a função já que não há dados para listar

    separador()  # Chama a função visual para desenhar a linha divisória superior da listagem
    print(f"{CYAN}{'ALUNOS CADASTRADOS':^45}{RESET}")  # 'print' centraliza o título da listagem em um intervalo de 45 caracteres na cor ciano
    separador()  # Chama a função visual para desenhar a linha divisória inferior do cabeçalho da listagem

    print(f"\n{WHITE}{'NOME':<25} {'NOTA':>6}   STATUS{RESET}")  # 'print' formata as colunas: NOME alinhado à esquerda ('<25') e NOTA à direita ('>6')
    print("-" * 45)  # 'print' exibe uma linha tracejada multiplicando o caractere '-' por 45 vezes

    for linha in linhas:  # 'for' inicia um laço que vai percorrer item por item (linha por linha) de dentro da lista 'linhas'
        linha = linha.strip()  # '.strip()' limpa os espaços em branco e o caractere invisível de quebra de linha '\n' da linha atual

        if linha:  # 'if' checa se a linha atual não está em branco para evitar erros de processamento
            nome, nota = linha.split(";")  # '.split(";")' quebra a string onde houver ';' e o operador '=' desempacota os dois pedaços nas variáveis 'nome' e 'nota'
            nota = float(nota)  # Converte a string 'nota' que veio do arquivo de volta para o tipo numérico 'float'

            status = "APROVADO" if nota >= 6 else "REPROVADO"  # Operador ternário: atribui "APROVADO" se a nota for maior/igual a 6, senão atribui "REPROVADO"
            cor_status = GREEN if nota >= 6 else RED  # Operador ternário: escolhe a variável de cor 'GREEN' para aprovados ou 'RED' para reprovados

            print(  # 'print' estruturado em várias linhas para exibir as informações alinhadas e coloridas dinamicamente
                f"{WHITE}{nome:<25}{RESET} "  # Exibe o nome do aluno em branco, ocupando obrigatoriamente 25 espaços alinhado à esquerda
                f"{cor_status}{nota:>6.1f}{RESET}   "  # Exibe a nota formatada com uma casa decimal ('.1f'), ocupando 6 espaços à direita, na cor do status
                f"{cor_status}{status}{RESET}"  # Exibe o texto do status ("APROVADO"/"REPROVADO") com a sua respectiva cor correspondente
            )

    print()  # 'print' insere uma quebra de linha para separar a tabela do encerramento
    separador()  # Executa a função do separador visual para indicar o fim da tabela impressa

def alterar_aluno():  # 'def' inicia a função encarregada de buscar, modificar e sobrescrever dados de um aluno específico
    if not os.path.exists(ARQUIVO):  # 'if' associado ao 'not' valida se o arquivo não existe em disco
        print(f"{RED}Nenhum aluno cadastrado ainda.{RESET}")  # 'print' avisa que a operação é impossível por falta de um arquivo existente
        return  # Interrompe e sai da função 'alterar_aluno'

    print(f"\n{CYAN}===== ALTERAR ALUNO ====={RESET}")  # 'print' exibe o título da funcionalidade na cor ciano

    nome_busca = input("Digite o nome do aluno que deseja alterar: ").strip()  # Coleta o nome via 'input()' e limpa espaços extras usando '.strip()'

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:  # Abre o arquivo original no modo de leitura ('r') usando o gerenciador de contexto 'with'
        linhas = arquivo.readlines()  # Carrega todas as linhas textuais do arquivo para a memória dentro da variável lista 'linhas'

    alunos = []  # Inicializa uma lista vazia chamada 'alunos' para armazenar temporariamente as linhas limpas
    encontrado = False  # Variável do tipo booleana (flag) iniciada como 'False' para controlar se o alvo foi localizado ou não

    for linha in linhas:  # Laço 'for' para iterar sobre cada registro textual bruto recuperado do arquivo
        linha = linha.strip()  # Remove caracteres invisíveis (como o '\n') de cada linha analisada

        if linha:  # Garante que linhas vazias acidentais no arquivo de texto não sejam inseridas na lista
            alunos.append(linha)  # Método '.append()' adiciona a linha limpa no final da lista 'alunos'

    novos_alunos = []  # Inicializa uma lista vazia para construir o novo conjunto de dados que substituirá o antigo arquivo

    for registro in alunos:  # Laço 'for' que varre cada string armazenada na lista temporária 'alunos'
        nome, nota = registro.split(";")  # Divide o registro atual no caractere ';' separando os valores nas variáveis 'nome' e 'nota'

        if nome.lower() == nome_busca.lower():  # '.lower()' converte ambos os nomes para minúsculo, permitindo uma comparação que ignora maiúsculas/minúsculas
            encontrado = True  # Altera o estado da flag para 'True', indicando que o aluno solicitado foi encontrado no sistema

            while True:
                novo_nome = input("Digite o novo nome: ").strip()  # Solicita e limpa o novo nome atualizado do estudante via 'input().strip()'
                if not novo_nome:
                    print(f"{RED}O nome não pode ficar em branco.{RESET}")
                elif novo_nome.isdigit():
                    print(f"{RED}O nome não pode ser composto apenas por números.{RESET}")
                else:
                    break

            while True:  # Abre um loop infinito de validação para garantir a digitação correta da nova nota numérica
                try:  # Inicia o bloco de monitoramento contra erros de entrada ('ValueError')
                    nova_nota = float(input("Digite a nova nota: ").strip())  # Captura, limpa e tenta transformar a nova entrada em float
                    break  # Quebra o laço 'while' se a conversão para float funcionar sem erros
                except ValueError:  # Bloco acionado caso o usuário insira caracteres não numéricos na nota
                    print(f"{RED}Digite apenas números.{RESET}")  # Exibe aviso em vermelho instruindo o usuário sobre o erro de digitação

            novos_alunos.append(f"{novo_nome};{nova_nota}")  # Monta a nova string formatada e a insere na lista de atualizados via '.append()'
        else:  # Bloco executado para todos os outros alunos que não eram o alvo da alteração
            novos_alunos.append(registro)  # Mantém o registro original intacto, adicionando-o direto na lista 'novos_alunos'

    if not encontrado:  # Verifica se a flag 'encontrado' permaneceu 'False' após rodar todo o laço de busca
        print(f"{RED}Aluno não encontrado.{RESET}")  # 'print' informa em vermelho que nenhum registro correspondia ao nome pesquisado
        return  # Sai da função sem alterar o arquivo de texto

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:  # Abre o arquivo no modo escrita ('w'), o que apaga o arquivo antigo para reescrevê-lo do zero
        for aluno in novos_alunos:  # Laço 'for' percorre cada string formatada de dentro da lista atualizada 'novos_alunos'
            arquivo.write(f"{aluno}\n")  # Escreve o registro atualizado inserindo manualmente a quebra de linha '\n' no arquivo

    print(f"{GREEN}Aluno alterado com sucesso!{RESET}")  # 'print' confirma o sucesso da alteração exibindo o texto em verde

def excluir_aluno():  # 'def' define a função responsável por remover um registro específico da base de dados textuais
    if not os.path.exists(ARQUIVO):  # Condicional 'if not' verifica se o arquivo físico não existe no diretório atual
        print(f"{RED}Nenhum aluno cadastrado ainda.{RESET}")  # Avisa na tela que não existem dados disponíveis para sofrer exclusão
        return  # Finaliza e sai da função imediatamente

    print(f"\n{RED}===== EXCLUIR ALUNO ====={RESET}")  # 'print' renderiza a identificação da tela atual estilizada com a cor vermelha

    nome_busca = input("Digite o nome do aluno que deseja excluir: ").strip()  # Captura o termo de busca textual e higieniza com '.strip()'

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:  # Abre o arquivo em formato de leitura ('r') utilizando o escopo seguro 'with'
        linhas = arquivo.readlines()  # Copia todas as linhas do arquivo e as armazena no formato de lista de strings na variável 'linhas'

    alunos = []  # Cria uma estrutura de lista vazia para isolar e processar as linhas limpas do arquivo
    for linha in linhas:  # Laço 'for' navega por cada uma das linhas carregadas do arquivo de texto
        linha = linha.strip()  # Trata a string removendo quebras de linha ou recuos em branco nas extremidades

        if linha:  # Avalia se a linha possui caracteres válidos antes de processá-la
            alunos.append(linha)  # Adiciona a linha válida dentro do array/lista 'alunos' por meio do método '.append()'

    novos_alunos = []  # Inicializa a lista que guardará todos os alunos, com exceção daquele que será excluído
    encontrado = False  # Flag booleana configurada como falsa para monitorar se a exclusão foi realizada com sucesso

    for registro in alunos:  # Laço 'for' percorre todos os cadastros existentes na lista temporária 'alunos'
        nome, nota = registro.split(";")  # Divide o texto no ponto de divisão ';' distribuindo os pedaços nas variáveis 'nome' e 'nota'

        if nome.lower() == nome_busca.lower():  # Compara os dois nomes transformados em minúsculo por '.lower()' para validar a igualdade
            encontrado = True  # Altera o estado da flag para verdadeiro, sinalizando que a exclusão foi processada internamente
        else:  # Caso o nome do registro atual seja diferente do nome digitado pelo usuário
            novos_alunos.append(registro)  # Transfere o registro que deve ser mantido diretamente para a lista 'novos_alunos'

    if not encontrado:  # Condicional que valida se a flag 'encontrado' continuou falsa até o fim do loop
        print(f"{RED}Aluno não encontrado.{RESET}")  # Exibe uma mensagem em cor vermelha alertando a ausência do registro procurado
        return  # Aborta os procedimentos da função sem mexer no arquivo físico

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:  # Abre o arquivo no modo 'write' ('w'), limpando todo o conteúdo anterior para gravação limpa
        for aluno in novos_alunos:  # Laço 'for' itera sobre cada registro que sobrou na lista filtrada 'novos_alunos'
            arquivo.write(f"{aluno}\n")  # Escreve a linha do aluno sobrevivente no arquivo concatenando o caractere de quebra de linha '\n'

    print(f"{GREEN}Aluno excluído com sucesso!{RESET}")  # 'print' sinaliza na tela em verde que o processo de remoção foi concluído

while True:  # Loop 'while True' inicia o motor principal do programa, rodando de forma perpétua até encontrar um 'break'
    exibir_menu()  # Invoca e renderiza a função do menu principal na tela a cada ciclo do laço

    opcao = input(f"{MAGENTA}Escolha uma opção: {RESET}").strip()  # Coleta a opção digitada, injeta cor magenta na pergunta e limpa com '.strip()'

    if opcao == "1":  # 'if' verifica se o caractere digitado corresponds textualmente a "1"
        cadastrar_aluno()  # Invoca a execução da função de cadastro de alunos se a condição for verdadeira

    elif opcao == "2":  # 'elif' avalia se a string digitada é exatamente igual a "2"
        listar_alunos()  # Invoca o fluxo da função de listagem de alunos na tela se a condição for verdadeira

    elif opcao == "3":  # 'elif' avalia se a string digitada é exatamente igual a "3"
        alterar_aluno()  # Despacha o processamento para a função de edição/alteração de dados cadastrais

    elif opcao == "4":  # 'elif' avalia se a string digitada é exatamente igual a "4"
        excluir_aluno()  # Despacha o processamento para a função encarregada de deletar registros

    elif opcao == "0":  # 'elif' checa se o usuário escolheu o caractere "0" para encerrar a aplicação
        print(f"{YELLOW}Encerrando o sistema. Até logo!{RESET}")  # Exibe em amarelo a mensagem de despedida do sistema no console
        break  # Interrompe o loop infinito 'while True', finalizando a execução de todo o programa Python

    else:  # Bloco executado de forma padrão caso a entrada não combine com nenhuma das condições numéricas acima
        print(f"{RED}Opção inválida. Tente novamente.{RESET}")  # Imprime uma mensagem de erro em vermelho instruindo nova tentativa