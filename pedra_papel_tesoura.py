#  - JOGO DE PEDRA, PAPEL E TESOURA
# - Com historico de partidas

import random
import json
from datetime import datetime

Arquivo_historico = 'historico_partidas.json' # - Arquivo JSON que contém o historico de partidas
opcoes = ['pedra', 'papel', 'tesoura'] 

def carregar_historico():
    try:
        with open(Arquivo_historico, 'r', encoding = 'utf-8') as f: # - Abre o arquivo em modo leitura
            return json.load(f) # - Converte JSON para objeto Python
    except FileNotFoundError: # - Se o arquivo não existe
        return [] # - Retorna vazio
    
def salvar_historico(historico): # - Salva os dados no arquivo JSON
    with open (Arquivo_historico, 'w', encoding='utf-8') as f: # - Abre o arquivo em modo escrita
        json.dump(historico, f, indent = 4, ensure_ascii = False) # - Python para JSON
        
def mostrar_historico(): # - Historico de partidas
    historico = carregar_historico()
    
    if not historico:
        print('\n Nenhuma partida registrada ainda.')
        return

    print('Historico de partidas' + '-' * 40)
    # - Formato em que sera organizado o arquivo de partidas (historico)
    for i, partida in enumerate(historico, start=1):
        print(f'\nPartida {i}')
        print(f'Data: {partida['data']}')
        print(f'Placar final: Jogador {partida['placar_jogador']} X {partida['placar_computador']} Computador')
        print(f'Vencedor: {partida['vencedor']}')
        print(f'Rodadas: ')
        for r in partida['rodadas']:
            print(f'Rodada {r['rodada']}: Jogador = {r['jogador']} |' f'Computador ={r['computador']} | Vencedor = {r['vencedor']}')
            print('-' * 40 + '\n')
            
def determinar_vencedor(jogador,computador): # - Casos de vitória e derrota
    if jogador == computador:
        return "Empate!"
    elif((jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel')):
        return 'jogador'
    else:
        return 'computador'
    
def jogar():
    placar_jogador = 0
    placar_computador = 0
    rodada_atual = 1
    rodadas = []
    
    print('Nova partida iniciada! (Melhor de 3)')
    
    while placar_jogador < 2 and placar_computador < 2: 
        print(f'Rodada {rodada_atual}')
        print('Escolha: pedra, papel ou tesoura')
        
        escolha_jogador = input('Sua escolha: ').lower().strip()
        
        if escolha_jogador not in opcoes:
            print('Escolha inválida. Tente novamente.')
            continue
        
        escolha_computador = random.choice(opcoes)
        
        vencedor_rodada = determinar_vencedor(escolha_jogador, escolha_computador)
        
        if vencedor_rodada == 'jogador':
            placar_jogador += 1
            vencedor_texto = 'jogador'
            print('Você ganhou a rodada!')
            
        elif vencedor_rodada == 'computador':
            placar_computador += 1
            vencedor_texto = 'computador'
            print('O computador ganhou a rodada.')
            
        else:
            vencedor_texto = 'Empate'
            print('Rodada empatada.')
            
        print(f'Você: {escolha_jogador} | Computador: {escolha_computador}')
        print(f'Placar: Você {placar_jogador} X {placar_computador} Computador')
        
        rodadas.append({
            'rodada': rodada_atual, 'jogador': escolha_jogador, 'computador': escolha_computador, 'vencedor': vencedor_texto
        })
        
        rodada_atual += 1
        
    if placar_jogador > placar_computador: # - Vitoria do jogador
        vencedor_partida = 'Jogador'
        print('Parabéns! Você venceu a partida!')
    
    else: # - Vitoria computador
        vencedor_partida = 'Computador'
        print('O computador venceu a partida!')
     
    partida = { 
        'data':datetime.now().strftime('%d/%M/%Y %H:%M:%D'), 
        'placar_jogador': placar_jogador,
        'placar_computador': placar_computador,
        'vencedor': vencedor_partida,
        'rodadas': rodadas
    } 
    
    historico = carregar_historico()
    historico.append(partida)
    salvar_historico(historico)
    
def menu(): # - Menu do jogo com suas opções
    while True:
        print('PEDRA, PAPEL E TESOURA')
        print('1 Jogar nova partida')
        print('2 Ver historico de partidas')
        print('3 Sair')
        
        opcao = input('Escolha uma opção: ').strip()
        
        if opcao == '1':
            jogar()
        elif opcao == '2':
            mostrar_historico()
        elif opcao == '3':
            print('Até a próxima! Bye bye.')
            break
        else:
            print('Opção inválida. Tente novamente.')
            
if __name__ == "__main__":
    menu()