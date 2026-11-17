# 5 regras que eu nunca quebro em produção

1. Nunca coloco chave, senha ou token no Git, em chat, print ou vídeo. Segredo fica só no .env, e o .env está no .gitignore.
2. Nunca rodo sudo nem comando que eu não entendo no servidor. Pergunto antes.
3. Nunca testo com dado real de paciente. Uso dados inventados e o banco de teste (_test).
4. Nunca faço push direto na main nem clico em Merge. Trabalho num ramo e abro pull request; quem junta é o Rodrigo.
5. Nunca apago nada sem backup e sem confirmar duas vezes.

Se um .env for para um commit por engano: a chave está vazada. Trocar a chave na hora e avisar o Rodrigo.
