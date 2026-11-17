# Como resolver um bug no Maestro (guia para quem está começando)

Tudo é feito no SEU notebook (Ubuntu/WSL), na pasta ~/maestro. Nunca no servidor.
O terminal do notebook começa com seu_usuario@DESKTOP. Se começar com netinho@srv..., você está no servidor: pare.

## 1. Reproduzir o bug
- Ligue o sistema de teste e abra http://localhost:3001/CRM.
- Faça o passo a passo até ver o erro. Tire print.
- Abra uma issue no GitHub: título curto e específico, Passos para reproduzir, Resultado esperado, Resultado obtido, Print.

## 2. Pedir a causa ao Claude Code (sem corrigir)
Na pasta ~/maestro, rode: claude
Cole: "Bug da issue #N: [o que acontece e o que deveria acontecer]. Encontre de onde vem, me mostre arquivo e linha e explique a causa em linguagem simples. NÃO corrija."
- Se o Claude disser "não vejo bug nessa linha", a sessão é nova: conte o sintoma completo de novo.
- Para ver a linha citada: sed -n '1010,1025p' "caminho/do/arquivo"

## 3. Criar o ramo da correção
    cd ~/maestro
    git status                      (tem que dizer "nothing to commit")
    git checkout netinho/rede       (o ramo onde o bug aparece, não necessariamente a main)
    git checkout -b fix/nome-curto  (ramo novo só para essa correção)

## 4. Pedir a correção mínima
Cole: "Corrija da forma mais mínima possível: [o comportamento certo]. Me mostre o diff antes de aplicar. Não faça commit."
- Leia o diff: linhas vermelhas saem, verdes entram. Mexeu em arquivos demais? Pergunte por quê.
- Se a função é usada em vários lugares, prefira corrigir só no lugar do bug.

## 5. Escrever e provar o teste
Cole: "Escreva um teste Vitest que falha com o bug e passa com a correção. Banco de teste: crm_maestro_test. Rode só esse arquivo. Depois desfaça a correção, mostre o teste falhando, e restaure. Não faça commit."
- O teste tem que FALHAR sem a correção e PASSAR com ela. Se passar nos dois, não testa nada.
- Rodar você mesmo: cd ~/maestro/app && CRM_TEST_DB=crm_maestro_test npx vitest run "caminho/do/teste"
- Sempre informe o banco de teste (CRM_TEST_DB). Sem ele, o teste limpa outro banco.
- Confira na tela: o bug sumiu? O caminho normal continua funcionando?

## 6. Enviar e abrir o pull request
    git status                      (confira: só os arquivos esperados)
    git add .
    git commit -m "corrige #N: descrição curta"   ("corrige #N" fecha a issue ao juntar)
    git push -u origin fix/nome-curto
- Abra o PR em github.com/admdocbr/maestro/compare/netinho/rede...fix/nome-curto
- Base certa: o ramo de onde você saiu.
- Descrição: causa, o que mudou, como testou.
- NUNCA clique em Merge. Quem junta é o Rodrigo.

## 7. Erros que eu cometi (e como evitar)
- Colei texto de explicação no terminal: "command not found". Cole só os comandos.
- Juntei dois comandos na mesma linha (git add .git status) ou terminei com \ (o terminal fica esperando com >). Um comando por linha; Ctrl+C cancela.
- Rodei comandos no servidor em vez do notebook. Olhe o começo da linha do terminal.
- Criei o ramo a partir da main, mas o código do bug só existia em netinho/rede. Pergunte ao Claude em que ramo o código está.
- Push recusado por "e-mail privado" (GH007): configure o e-mail disfarçado do GitHub (git config --global user.email "ID+usuario@users.noreply.github.com") e refaça com git commit --amend --reset-author --no-edit.
- Escrevi c= num campo da tela em vez de na barra de endereço do navegador.
- Cliquei duas vezes num botão de liga/desliga e achei que estava quebrado: dois cliques se anulam. Teste com um clique e confira depois do F5.
- Aprovei sem querer o plano do Claude que já ia escrever código: no dia de planejar, escolha "Tell Claude what to change".
- Nunca coloque chave, senha ou token em commit, chat, print ou vídeo.
