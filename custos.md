# Custos do Claude (fase 26)

Preços por milhão de tokens (platform.claude.com/docs/en/about-claude/pricing, 16/11/2026):

| Modelo | Entrada | Saída | Entrada em cache |
|---|---|---|---|
| Opus 5.5 | US$ 4 | US$ 20 | US$ 0,20 |
| Sonnet 5.5 | US$ 2 | US$ 10 | US$ 0,10 |
| Haiku 5.5 | US$ 0,10 | US$ 0,50 | US$ 0,01 |

Conta: 1.000 pedidos/mês, cada um com 2.000 tokens de entrada e 500 de saída
(= 2 milhões de entrada + 0,5 milhão de saída por mês).

| Modelo | Sem cache | Com 90% da entrada em cache |
|---|---|---|
| Opus 5.5 | US$ 18,00 | US$ 11,16 |
| Sonnet 5.5 | US$ 9,00 | US$ 5,58 |
| Haiku 5.5 | US$ 0,45 | US$ 0,29 |

(A conta com cache ignora o custo de gravar o cache na primeira vez.)

Conclusão:
1. Assinatura basta para uma pessoa usando o Claude no dia a dia (app e Claude Code): preço fixo, sem surpresa.
2. A API compensa quando um sistema chama o Claude sozinho, como o Maestro respondendo pacientes: paga só o que usa e escolhe o modelo.
3. A saída custa mais que a entrada, e o cache derruba o custo da parte repetida; para tarefa simples, Haiku custa uma fração do Opus.
