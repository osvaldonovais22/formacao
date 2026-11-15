# Mapa do sistema Maestro

1. O que faz: é uma secretária com IA para médicos. Responde pacientes no WhatsApp, cuida da agenda e passa para um humano quando tem dúvida.
2. Cada médico tem seus próprios containers e seu próprio banco de dados, separado dos outros.
3. Tecnologia: TypeScript com Next.js e React, banco PostgreSQL via Prisma, IA da Anthropic, tudo rodando em Docker.
4. Por onde começa: app/src/middleware.ts, que recebe toda visita e decide para onde mandar a pessoa.
5. Depois do login, a primeira página é app/src/app/(app)/page.tsx.
6. Dados: o desenho do banco fica em app/prisma/schema.prisma. Os dados reais ficam no PostgreSQL de cada médico, nunca no código.
7. Configurações: o arquivo .env de cada consultório (nome, senhas, portas) e o docker-compose.yml (quais containers sobem).
8. Pasta app/src/app: as telas que o usuário vê e a API (o "backend", que é a parte que trabalha por trás).
9. Pasta app/src/lib: a regra de negócio, ou seja, IA, agenda, WhatsApp e pagamento.
10. Pasta deploy: scripts para criar, fazer backup e operar cada consultório no servidor.
