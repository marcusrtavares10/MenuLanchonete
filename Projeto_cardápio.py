"""
Projeto Cárdapio em Python
"""
print('=-' * 20)
print('         SEJA BEM-VINDO!!!')
print('=-' * 20)
print('       LANCHONETE DO TAVINHO')
print('-='*20)
print("""   =-=-=-=-=-=-=CARDÁPIO=-=-=-=-=-=-=
   | 1. Cachorro-quente = R$ 10,00  |
   | 2. Hamburguer = R$ 15,00       |
   | 3. X-Salada = R$ 13,00         |
   | 4. X-Tudo = R$ 18,00           |
   | 5. Coca-cola = R$ 5,00         |
   | 6. Sorvete = R$ 3,00           |""")
print('-='*20)
print()
pedido = input('Deseja fazer pedido? [s] [n]: ').lower()
q = 0
total = 0
if pedido == 's':
    while pedido == 's':
        p = int(input('Digite o codigo do produto: '))
        q = int(input('Digite a quantidade: '))
        if p == 1:
            total = total + (q * 10)
        elif p == 2:
            total = total + (q * 15)
        elif p == 3:
            total = total + (q * 13)
        elif p == 4:
            total = total + (q * 18)
        elif p == 5:
            total = total + (q * 5)
        elif p == 6:
            total = total + (q * 3)
        else:
            print('Opção inválida!')
        pedido = input('Deseja fazer outro pedido? [s] [n]: ').lower()

    print()
print('Sua conta ficou em R$ {} reais'.format(total))
print()
print('OBRIGADO PELA PREFERÊNCIA E VOLTE SEMPRE!')
