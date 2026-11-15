# Dia 14 - Roteiro: o Maestro de ponta a ponta (20 min)

## 1. O que é e para quem (3 min)
- O Maestro é uma secretária com IA para o médico que atende sozinho.
- O paciente fala pelo WhatsApp. A IA responde, marca consulta na agenda e chama um humano quando não tem certeza.
- Cada médico tem seus próprios containers e seu próprio banco. Um consultório não vê o outro.

## 2. Por onde o dado entra (4 min)
- O paciente manda uma mensagem no WhatsApp.
- O container WAHA (a peça que conversa com o WhatsApp) recebe e avisa o app por uma rota da API, em app/src/app/api/.
- Antes de qualquer tela, o middleware.ts confere quem é a pessoa e de qual consultório ela é.

## 3. O que acontece com ele (6 min)
- A mensagem é gravada no PostgreSQL, nas tabelas Conversation e Message.
- A IA (lib/agent.ts) lê a configuração do médico (AiConfig) e os fatos que ele cadastrou (lib/kb-local.ts).
- Se o paciente quer marcar consulta, entram lib/agendamento.ts e o Google Agenda.
- Áudio vira texto pelo Whisper.

## 4. Por onde sai (4 min)
- A resposta volta pelo WAHA para o WhatsApp do paciente.
- A conversa aparece para a equipe na tela de atendimentos/inbox.
- Se a IA não tiver certeza, a conversa passa para um humano.

## 5. O que eu ainda não entendo (3 min)
- Container e Docker: sei que cada médico tem os seus, mas não sei explicar bem o que é um container.
- Como exatamente o WAHA avisa o app que chegou mensagem (o tal "webhook").
- O que é o Prisma e por que as mudanças no banco (migrations) são escritas à mão.
- Diferença entre o meu notebook (WSL), o servidor (VPS) e o GitHub: onde cada coisa roda.
- Git ainda me confunde: commit, push, amend e o erro do e-mail privado que tive na fase 12.
- Os três arquivos de login (auth.ts, auth.edge.ts, auth.config.ts) e a troca do NextAuth pelo Cognito.
- Como rodar os testes sem quebrar nada no servidor.

## Respostas depois da sessão
- (preencher depois de falar com o Rodrigo)
