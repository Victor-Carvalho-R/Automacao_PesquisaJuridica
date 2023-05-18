# Automacao_PesquisaJuridica
Todos os dados são criados para fins didáticos. Um código de automação que seleciona o Estado correspondente à pessoa e realiza uma pesquisa com o objetivo de localizar algum processo. No fim, o algorítmo mostra quantos processos encontrados e quantos não encontrados.

O código utiliza uma tabela com os dados a serem usados nas pesquisas e a trata removendo uma coluna vazia. Logo depois começa um loop que segue um passo a passo para o preenchimento do formulário. Esses passos são:
- Mover o mouse para abrir as opções dos estados;
- Direcionar o navegador para a aba aberta mais recente;
- Preencher as informações;
- Aceitar um alerta ao terminar o questionário;
- Adicionar o processo atual como encontrado ou não;
- Voltar para a aba de seleção de estados.

Após a repetição, o código mostra o resultado de quantos processos foram ou não encontrados.
