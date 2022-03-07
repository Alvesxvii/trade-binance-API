from configparser import ConfigParser
from binance.client import Client
from binance.enums import *
import time
import os


chaves_ini = ConfigParser()

# Define chaves.ini as the archive wich is gonna store the api keys
# The path is the current location of the app (root)
caminho_chaves_ini = r'chaves.ini'
chaves_ini.read(caminho_chaves_ini, encoding='UTF8')

# Pass the value of the stored info into api_key and api_secret
api_key = chaves_ini.get('CHAVES', 'api_key')
api_secret = chaves_ini.get('CHAVES', 'api_secret')

# Creates some kind of header, only for design and view purposes
def header():
    print('#################################################################################')
    print('#                                                                               #')
    print('#                              B I N A N C E - A P I                            #')
    print('#                                                                               #')
    print('#################################################################################')

# Creates some kind of menu, only for design and view purposes
def menu():
    print('#################################################################################')
    print('#                                                                               #')
    print('#                              B I N A N C E - A P I                            #')
    print('#                                                                               #')
    print('#################################################################################')
    print('#                                    M E N U                                    #')
    print('#                                                                               #')
    print('#                1- Exibir saldo        |       2- Criar ordem a mercado        #')
    print('#                3- Visualizar pares    |       4- Em breve                     #')
    print('#################################################################################')

# Some kind of test if the .ini file is correctly filled. Tough it isn't working 100% yet...
# binance.client raises an exception ever since the app is loaded with bad information given in that file.
# it won't let me check for missing data first. It's probably related to the fact that once the program loads
# it already discharge what's in chaves.ini. This is some point to check in the future along with some other
# try and except treatments that must be implemented later.
if api_key == '' or api_secret == '':

    header()
    print('Arquivo de configuração de chaves preenchido incorretamente ou algum dos valores encontra-se em branco.')
    print('Encerrando em: 5s')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Encerrando em: 4s')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Encerrando em: 3s')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Encerrando em: 2s')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Encerrando em: 1s')
    time.sleep(1)
    exit()

elif api_key != '' or api_secret != '':

    header()
    print('Chaves registradas com sucesso!')
    print('')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


client = Client(api_key, api_secret)

# This gets all the info about the account inside checando_status as a function that can be called later.
checando_status = client.get_account_status()

status = checando_status.get('data')

# This checks if the connection was successful with the given keys in chaves.ini
try:
    if status == 'Normal':
        header()
        print('')
        print('A conexão com a API foi estabelecida com sucesso!')
        print('')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
except ValueError:
    print('Impossível conectar-se. Houve um erro com a api_secret fornecida, ou com o IP permitido.')


print('')
detalhes = client.get_account()

# Currently hidden but this shows all data related to the account that can be accessible through the API
#for dado in detalhes:

#    print(dado)


# Function to show the balance of the account. Among all the available wallets, it will only show those wich
# the balance is greater than zero.
def MostraSaldos():

    menu()
    print('')
    ativos = detalhes['balances']

    for ativo in ativos:
        nome = ativo['asset']
        quantidade = ativo['free']

        if float(ativo['free']) > 0:

            print(f'Ativo: {nome} - {quantidade}')

    print('')


MostraSaldos()

# Function that places a real time market order. Must take care because once called this will execute whatever
# is passed inside ordem_compra (for buying) and ordem_venda (for selling) as long as there is available balance
# to do so.
def Criar_ordem_mercado():

    menu()
    print('')
    print('#ATENÇÃO: O ticker inicial é a referência!')
    print('#Exemplo: BNBBTC - Compra: Comprará BNB usando BTC / Venda: Venderá BNB ganhando BTC')
    print('#Exemplo: BTCBNB - Compra: Comprará BTC usando BNB / Venda: Venderá BTC ganhando BNB')
    print('')
    time.sleep(0.5)
    par = input(str('-> Digite o par de negociação: '))
    print('')
    operacao = int(input('-> Deseja comprar ou vender? - Digite: 1- Comprar / 2- Vender : '))
    print('')
    quantidade = float(input('-> Digite a quantidade a ser comprada/vendida: '))
    print('')

    if operacao == 1:

        ordem_compra = client.create_order(
            symbol=par,
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            #timeInForce=TIME_IN_FORCE_GTC,
            #price='0.00001',
            quantity=quantidade)


        print(f'Par: {ordem_compra["symbol"]} - Status: {ordem_compra["status"]} - Tipo de ordem: {ordem_compra["type"]} - Lado: {ordem_compra["side"]}')
        print(f'ID Ordem: {ordem_compra["orderId"]} - QTD Operada: {ordem_compra["executedQty"]}')
        print('')


    elif operacao == 2:

        ordem_venda = client.create_order(
            symbol=par,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            #timeInForce=TIME_IN_FORCE_GTC,
            #price='0.00001',
            quantity=quantidade)


        print(f'Par: {ordem_venda["symbol"]} - Status: {ordem_venda["status"]} - Tipo de ordem: {ordem_venda["type"]} - Lado: {ordem_venda["side"]}')
        print(f'ID Ordem: {ordem_venda["orderId"]} - QTD Operada: {ordem_venda["executedQty"]}')
        print('')

# Calls a little reminder of what pairs are traded in Binance.
def VisualizarPares():

    print('#################################################################################')
    print('#                                                                               #')
    print('#                              B I N A N C E - A P I                            #')
    print('#                                                                               #')
    print('#################################################################################')
    print('#                                                                               #')
    print('# 1- XNO (Nano) | 2- BNB (Binance Coin) | 3- USDT - (Tether) | 4- BTC (Bitcoin) #')
    print('#                                                                               #')
    print('#################################################################################')
    print('')

    visualizar_par = int(input('-> Qual moeda você gostaria de visualizar?: '))
    print('')

    if visualizar_par == 1: # Nano
        print('XNOBTC - Bitcoin')
        print('XNOUSDT - Dólar Tether')
        print('XNOBUSD - Binance USD')
        print('XNOETH - Ethereum')
        print('')
        menu()

    if visualizar_par == 2: # BNB
        print('BNBBTC - Bitcoin')
        print('BNBUSDT - Dólar Tether')
        print('BNBBUSD - Binance USD')
        print('BNBETH - Ethereum')
        print('BNBBRL - Real Brasileiro')
        print('BNBCAKE - Pancake Swap')
        print('')
        menu()

    if visualizar_par == 3: # USDT
        print('USDTBTC - Bitcoin')
        print('USDTCAKE - Pancake Swap')
        print('USDTDOGE - Dogecoin')
        print('')
        menu()

    if visualizar_par == 4: # BTC
        print('Qualquer moeda da Binance faz par com BTC. Basta saber o ticker.')
        print('')
        print('BTCUSDT - Dólar Tether')
        print('')
        menu()


# Loop to navigate through the options of the application.
while True:

    print('')
    opcao_menu = int(input('-> O que você deseja fazer?: '))
    print('\n' * 35)

    if opcao_menu == 1:
        MostraSaldos()

    if opcao_menu == 2:
        Criar_ordem_mercado()

    if opcao_menu == 3:
        VisualizarPares()





