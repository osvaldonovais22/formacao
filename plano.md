# Plano - botão da IA no rodapé do chat (fase 23)

Tarefa: o botão de baixo diz "IA respondendo — clique para silenciar" mesmo com a IA do consultório desligada.
Decisão de produto (a confirmar com o Rodrigo): com o consultório desligado, o botão diz "IA desligada no consultório", continua clicável e o clique segue mudando só a chave do paciente.
Não muda API, tipo nem banco: o dado iaDoConsultorioLigada já chega na tela (PR #28).

## Passos
- [x] 1. Criar app/src/app/(app)/atendimentos/botao-da-ia.ts com a função estadoDoBotaoIa(detail), que devolve texto, título, destaque e pressionado para os 4 casos (paciente on/off x consultório on/off).
- [x] 2. Criar botao-da-ia.test.ts com os 4 casos e rodar ANTES de ligar no botão: o caso paciente on + consultório off tem que mostrar "IA desligada no consultório".
- [x] 3. Em chat-panel.tsx (botão nas linhas 1442-1461), trocar o uso de iaLigada por estadoDoBotaoIa(detail). A função alternarIa não muda.
- [x] 4. Rodar só os testes de atendimentos/ (CRM_TEST_DB=crm_maestro_test, um de cada vez).
- [x] 5. Testar na tela: consultório desligado -> botão diz "IA desligada no consultório"; clicar não quebra nada; conversa com atendente continua igual.
- [x] 6. Commit, push e pull request com base no ramo do PR #28.

## O que pode dar errado
- O valor do consultório só atualiza ao recarregar a conversa (mesmo comportamento do cabeçalho).
- Com o consultório desligado, clicar não muda o texto do botão, só a chave do paciente; o título explica.
- Cortado por excesso: reorganizar linha-do-cabecalho.ts (não é necessário para esta tarefa).
