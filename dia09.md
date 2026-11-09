# Dia 9

## 1. quantidade = int(sys.argv[2])
- **Dúvida:** não sabia o que era int(sys.argv[2]).
- **Resposta:** sys.argv é a lista de tudo o que eu escrevo no comando. O [0] é o nome do script, o [1] é a pasta e o [2] é a quantidade. Tudo chega como texto, e o int transforma o texto "5" no número 5.
- **Exemplo:** no cd formacao, formacao é o argumento.
- **Cuidado:** se a pessoa digitar algo que não é número inteiro, como abc ou 2.5, o int dá ValueError.

## 2. if len(sys.argv) not in (2, 3):
- **Dúvida:** não sabia o que era len nem o not in.
- **Resposta:** o len conta quantos itens tem a lista sys.argv. O not in (2, 3) quer dizer "não é 2 nem 3". Então a linha confere se eu escrevi o comando certo: só o script e a pasta (2 itens) ou o script, a pasta e a quantidade (3 itens). Se for outro número, mostra como usar e encerra.
- **Exemplo:** python3 tamanhos.py ~/Downloads 5 tem 3 itens, então passa.

## 3. except ValueError: quantidade = 0
- **Dúvida:** não entendia por que colocar 0 na quantidade quando dá erro.
- **Resposta:** se a pessoa digita algo que não é número, como abc, o int dá ValueError. O except segura o erro para o programa não travar e coloca 0 na quantidade. Depois, o if quantidade < 1 dá verdadeiro (0 é menor que 1), mostra a mensagem de erro e fecha o programa.
- **Por que 0 e não 10:** com 10, o teste 10 < 1 daria falso, e o programa mostraria 10 arquivos como se estivesse tudo certo. O 0 é um valor que não passa no teste, então o mesmo if serve para avisar o erro de texto (abc) e de número inválido (0 ou negativo).

## 4. pasta = os.path.expanduser(sys.argv[1])
- **Dúvida:** não sabia o que era expanduser.
- **Resposta:** o expanduser troca o til (~) pelo endereço completo da minha pasta pessoal, que é uma pasta que o Python consegue ler. O terminal entende o ~, mas o Python sozinho não entende.
- **Exemplo:** "~/Downloads" vira "/home/windows_11osvaldo/Downloads".

## 5. if not os.path.isdir(pasta):
- **Dúvida:** não sabia o que era os.path.isdir.
- **Resposta:** o isdir pergunta "isso é uma pasta?". O not inverte, então a linha diz: se não encontrar a pasta, mostra o aviso de erro. Também mostra o erro se eu passar um arquivo em vez de uma pasta.
- **Extra:** os é o sistema operacional e path é caminho. O ponto quer dizer "dentro de".