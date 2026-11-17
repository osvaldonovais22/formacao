# Balanço do Exame Genin

## Roteiro da apresentação (30 min - tela primeiro, fala depois)
1. (5 min) A tarefa funcionando como usuário: abrir "osvaldo neto", clicar no botão da IA e mostrar "paciente ativo" / "paciente silenciado".
2. (5 min) O plano e como foi executado: plano.md com as caixinhas marcadas, 1 commit por passo.
3. (5 min) O PR #31 e os testes rodando ao vivo (7 passed).
4. (5 min) O que aprendi nos 30 dias.
5. (5 min) Onde ainda sou fraco.
6. (5 min) Salário que acho justo e por quê.

## O que aprendi nos 30 dias
- Usar o terminal (Ubuntu/WSL) e separar notebook, servidor e GitHub.
- Git no dia a dia: ramo, commit, push e pull request, sem mexer na main.
- O ciclo de um bug: reproduzir, abrir issue, achar a causa com o Claude Code, corrigir o mínimo, provar com teste que falha sem a correção e passa com ela, abrir PR.
- Planejar antes de codar e executar um passo por commit.
- Testar como usuário e transformar cada estranheza em issue.
- Segurança: segredo só no .env, .gitignore, nunca dado real de paciente.
- Custo do Claude: tokens, assinatura x API, cache.

## Onde ainda sou fraco
- Ler código sozinho: ainda dependo do Claude para explicar o que cada arquivo faz.
- Terminal: ainda erro colando texto errado, juntando comandos ou rodando no lugar errado.
- Escrever sozinho os pedidos ao Claude, as issues e os PRs: ainda preciso de modelo.
- Banco de dados e Docker: sei usar, ainda não sei explicar por dentro.
- Plano: ler um arquivo de lib/ por dia e explicar com minhas palavras antes de perguntar ao Claude.

## Entregas
- PRs com teste: #28 (corrige #25), #29 (corrige #26), #30 (corrige #27), #31 (botão da IA, corrige #32).
- Arquivos: mapa.md, dia14.md, estranhezas.md, skill.md, plano.md, custos.md, regras.md, dia28.md, como-resolver-bug.md.

## Proposta de salário
- Opção 1 - CLT, remoto: R$ 3.000 por mês.
- Opção 2 - PJ, remoto: R$ 4.000 por mês (sem 13º, férias pagas, FGTS e INSS da empresa; eu pago impostos e contador).

Por quê:
- Já faço o ciclo completo de um bug, do teste como usuário até o PR com teste.
- Ainda preciso de orientação, por isso peço no começo da faixa de júnior do mercado (CLT R$ 3.000 a 5.500; PJ R$ 4.000 a 7.000).
- A bolsa de aprovação é R$ 2.700; minha proposta fica perto disso.

Crescimento: revisar depois do Chunin, com alvo de CLT R$ 4.000 a 5.000 ou PJ R$ 5.500 a 7.000.
