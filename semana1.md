# Semana 1

## cat sem nome de arquivo
- **O que tentei:** digitei `cat` sozinho e depois `ls`, e nada funcionou.
- **O que não lembrei:** o `cat` precisa do nome do arquivo. Sem ele, fica esperando eu digitar.
- **Como destravei:** apertei Ctrl+Z, mas isso só pausa. O certo é Ctrl+C, que cancela.

## mv sem o nome novo
- **O que tentei:** `mv` só com o nome da pasta.
- **O que não lembrei:** o `mv` precisa de duas coisas: o nome atual e o nome novo.
- **Como destravei:** `mv nome-antigo nome-novo`.

## ~ e caminho sem comando
- **O que tentei:** digitei só `~` e, depois, só o caminho de um arquivo.
- **O que não lembrei:** o `~` e o caminho são endereços, não comandos. Precisa de um comando na frente (`cd`, `rm`, `mkdir`).
- **Como destravei:** `cd ~`, e comando + caminho.

## cd para a pasta errada
- **O que tentei:** `cd formacao` estando dentro de outra pasta.
- **O que não lembrei:** o `cd` procura a pasta dentro de onde eu estou.
- **Como destravei:** `cd ..` para subir um nível.

## Arquivo × pasta
- **O que tentei:** `mkdir etapa2`, mas já existia um arquivo com esse nome, criado com `touch`.
- **O que não lembrei:** `touch` cria arquivo, `mkdir` cria pasta. Não dá para transformar um no outro.
- **Como destravei:** apaguei o arquivo com `rm` e criei a pasta com `mkdir`. Conferi com `tree -d`.

## Ctrl+D fechou o terminal
- **O que tentei:** apertei Ctrl+D e o terminal fechou.
- **O que não lembrei:** Ctrl+C cancela, Ctrl+Z pausa, Ctrl+D fecha.
- **Como destravei:** reabri o terminal e voltei com `cd formacao`.

## for dentro do else (revisao.py)
- **O que tentei:** os números de 1 a 5 não apareciam.
- **O que não lembrei:** o recuo muda o que o programa faz. O `for` estava recuado, dentro do `else`, e não rodava.
- **Como destravei:** tirei os espaços do `for` para ele encostar na margem.

## Divisão por zero no imc.py
- **O que tentei:** testei o script com altura 0 e deu `ZeroDivisionError`.
- **O que não lembrei:** 0 é um número, então passava pelo `try`.
- **Como destravei:** colei o erro no Claude Code e pedi para aceitar só valores maiores que zero.

## Claude Code no modo automático
- **O que tentei:** o Claude Code criou o arquivo sem pedir aprovação.
- **O que não lembrei:** existe o modo de permissão, e estava em "auto mode".
- **Como destravei:** troquei para "manual mode" com Shift+Tab.

## semana1.md na pasta errada
- **O que tentei:** `code semana1.md` estando em `~`.
- **O que não lembrei:** o arquivo é criado na pasta em que o terminal está.
- **Como destravei:** fui para `formacao` e usei `code .` para abrir a pasta inteira.
