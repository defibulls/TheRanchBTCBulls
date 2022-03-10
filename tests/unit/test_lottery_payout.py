from calendar import c
from unittest import mock
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint



def test_lottery_winners():

    fund_deposited = 80_000

    #owner = accounts[0]
    owner = get_account()
    TheRanchBullsMint = deploy_mint_contract()
    TheRanchBullsAirDrop = deploy_AirDrop_contract()

    contract_balance = TheRanchBullsMint.getBalance({"from": owner})
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    print(f'TheRanchBullsAirDrop_contract_adddress: {TheRanchBullsAirDrop.address}')
    assert contract_balance == 0
    
    person_0 = accounts[99]
    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]
    person_4 = accounts[4]
    person_5 = accounts[5]
    person_6 = accounts[6]
    person_7 = accounts[7]
    person_8 = accounts[8]
    person_9 = accounts[9]
    person_10 = accounts[10]
    person_11 = accounts[11]
    person_12 = accounts[12]
    person_13 = accounts[13]
    person_14 = accounts[14]
    person_15 = accounts[15]
    person_16 = accounts[16]
    person_17 = accounts[17]
    person_18 = accounts[18]
    person_19 = accounts[19]
    person_20 = accounts[20]
    person_21 = accounts[21]
    person_22 = accounts[22]
    person_23 = accounts[23]
    person_24 = accounts[24]
    person_25 = accounts[25]
    person_26 = accounts[26]
    person_27 = accounts[27]
    person_28 = accounts[28]
    person_29 = accounts[29]
    person_30 = accounts[30]
    person_31 = accounts[31]
    person_32 = accounts[32]
    person_33 = accounts[33]
    person_34 = accounts[34]
    person_35 = accounts[35]
    person_36 = accounts[36]
    person_37 = accounts[37]
    person_38 = accounts[38]
    person_39 = accounts[39]
    person_40 = accounts[40]


    coinbase = accounts[96]
    dev1 = accounts[97]
    dev2 = accounts[98]


    starting_balance_of_each_account = 50_000 * 10**18



    ##########################################
    ## Give each person mocked USDC and DAI ##
    ##########################################


    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": coinbase})
    mocked_dai = MockedTokens_DAI.deploy(Web3.toWei(500_000, "ether"), {"from": coinbase})


    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

    # TheRanchBullsMint.setCentennialAirDropTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenDecimals(6,{"from": owner})
    
    # print(f'usdc address : {mocked_usdc.address}')
    # print(f'dai address :  {mocked_dai.address}')
    # print(f'TotalSupplyOfTokens: {mocked_tokens_usdc.totalSupply()/10**18}')
    print(f'CoinbaseMock USDC Balance: {mocked_usdc.balanceOf(coinbase) / 10**6}')
    print(f'CoinbaseMock DAI Balance: {mocked_dai.balanceOf(coinbase) / 10**18}')
 
    print(f'TheRanchBullsMint_ETH_balance: {TheRanchBullsMint.getBalance()/10**18}')
  
    assert (mocked_usdc.balanceOf(coinbase) / 10**6) == 500_000
    assert (mocked_dai.balanceOf(coinbase) / 10**18) == 500_000


 
    #########################################################
    ####       Transfer USDC and DAI to each person      ####
    #########################################################
    

    mocked_usdc.transfer(person_0, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_0, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_1, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_2, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_2, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_3, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_3, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_4, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_4, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_5, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_5, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_6, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_6, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_7, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_7, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_8, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_8, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_9, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_9, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_10, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_10, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_11, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_11, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_12, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_12, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_13, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_13, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_14, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_14, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_15, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_15, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_16, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_16, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_17, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_17, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_18, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_18, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_19, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_19, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_20, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_20, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_21, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_21, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_22, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_22, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_23, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_23, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_24, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_24, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_25, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_25, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_26, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_26, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_27, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_27, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_28, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_28, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_29, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_29, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_30, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_30, 10_000 * 10**18, {"from": coinbase})  
    mocked_usdc.transfer(person_31, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_31, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_32, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_32, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_33, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_33, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_34, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_34, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_35, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_35, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_36, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_36, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_37, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_37, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_38, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_38, 10_000 * 10**18, {"from": coinbase})
    mocked_usdc.transfer(person_39, 10_000 * 10**6, {"from": coinbase})
    mocked_dai.transfer(person_39, 10_000 * 10**18, {"from": coinbase})

    # starting_balance_of_each_account = 50_000 * 10**18
    

    
    # Owner unpauses contract
    tx_unpause_contract = TheRanchBullsMint.togglePauseStatus({"from": owner})

    #owner starts the public sale
    tx_start_public_sale = TheRanchBullsMint.togglePublicSaleStatus({"from": owner})
    tx_unlimited_mints_approval = TheRanchBullsMint.adjustMintsPerWallet(1000,{"from": owner})

    persons = 40
    mints_per_person = 10
    mints_per_tx = 5
    price_needed_for_approval = (mints_per_person * 250) * 10 ** 6
    price_needed_to_mint = (mints_per_tx * 250) * 10 ** 6
    
    nft_count_sold = mints_per_person * persons


    print(f'\nBEFORE: person_0 ETH Balance: {person_0.balance()/10**18}')
    print(f'BEFORE: person_0 usdc Balance: {mocked_usdc.balanceOf(person_0) / 10**6}')
    print(f'BEFORE: person_0 dai  Balance: {mocked_dai.balanceOf(person_0) / 10**18}')

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_0})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_0})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_0})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_1})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_1})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_1})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_2})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_2})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_2})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_3})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_3})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_3})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_4})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_4})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_4})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_5})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_5})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_5})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_6})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_6})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_6})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_7})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_7})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_7})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_8})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_8})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_8})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_9})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_9})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_9})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_10})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_10})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_10})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_11})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_11})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_11})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_12})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_12})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_12})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_13})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_13})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_13})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_14})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_14})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_14})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_15})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_15})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_15})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_16})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_16})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_16})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_17})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_17})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_17})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_18})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_18})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_18})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_19})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_19})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_19})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_20})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_20})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_20})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_21})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_21})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_21})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_22})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_22})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_22})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_23})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_23})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_23})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_24})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_24})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_24})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_25})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_25})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_25})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_26})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_26})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_26})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_27})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_27})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_27})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_28})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_28})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_28})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_29})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_29})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_29})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_30})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_30})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_30})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_31})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_31})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_31})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_32})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_32})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_32})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_33})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_33})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_33})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_34})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_34})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_34})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_35})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_35})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_35})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_36})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_36})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_36})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_37})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_37})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_37})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_38})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_38})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_38})

    mocked_usdc.approve(TheRanchBullsMint.address, price_needed_for_approval,{"from":person_39})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_39})
    TheRanchBullsMint.mint(mints_per_tx,{"from": person_39})


    print(f'\nAFTER: person_0 ETH Balance: {person_0.balance()/10**18}')
    print(f'AFTER: person_0 usdc Balance: {mocked_usdc.balanceOf(person_0) / 10**6}')
    print(f'AFTER: person_0 dai  Balance: {mocked_dai.balanceOf(person_0) / 10**18}')

    assert TheRanchBullsMint.totalSupply() == 400


    ##############################################################
    ### Check starting Balances on the contract after minting ####
    ##############################################################


    contract_ETH_balance_after_minting_sale = TheRanchBullsMint.getBalance({"from": owner})
    print(f'\n{nft_count_sold}_nfts_sold, ETH contract balance: {contract_ETH_balance_after_minting_sale  / 10**18 }')

    balance_of_usdc_tokens = TheRanchBullsMint.checkTokenBalance(mocked_usdc.address)    
    print(f'{nft_count_sold}_nfts_sold, USDC contract balance: {balance_of_usdc_tokens  / 10**6 }')

    balance_of_dai_tokens = TheRanchBullsMint.checkTokenBalance(mocked_dai.address)    
    print(f'{nft_count_sold}_nfts_sold, DAI contract balance: {balance_of_dai_tokens  / 10**18 }')

    assert contract_ETH_balance_after_minting_sale == 0
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address)  == 100_000 * 10**6
    assert TheRanchBullsMint.checkTokenBalance(mocked_dai.address)  == 0



    ##############################################################
    ####   Owner withdraws and invests funds into projects    ####
    ##############################################################
    assert mocked_usdc.balanceOf(owner) / 10**6 == 0
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address) == 100_000 * 10 ** 6


    amount = TheRanchBullsMint.checkTokenBalance(mocked_usdc.address) 
    TheRanchBullsMint.withdrawToken(mocked_usdc.address, amount, {"from": owner})

    assert mocked_usdc.balanceOf(owner) / 10**6 == 100_000
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address) == 0







    ##################
    #### Set Devs ####
    ##################
    # set dev1 / dev2 address 
    tx_set_dev1 = TheRanchBullsAirDrop.setdev1(dev1,{"from": owner})
    tx_see_dev1 = TheRanchBullsAirDrop.see_Dev1_address()
    assert tx_see_dev1 == dev1

    tx_set_dev2 = TheRanchBullsAirDrop.setdev2(dev2,{"from": owner})
    tx_see_dev2 = TheRanchBullsAirDrop.see_Dev2_address()
    assert tx_see_dev2 == dev2
    assert tx_see_dev2 != tx_see_dev1



    ################################################
    #####      Fund the contract with Link     #####
    ################################################
    fund_with_link(TheRanchBullsAirDrop)


 

    ###############################################################
    ### Funds the Contract back with money from the investments ###
    ###############################################################
    #######################################
    ##  assert no assets on the contract ##
    #######################################
    assert TheRanchBullsAirDrop.getBalance({"from": owner}) == 0
    assert TheRanchBullsAirDrop.checkTokenBalance(mocked_usdc.address)  == 0
    assert TheRanchBullsAirDrop.checkTokenBalance(mocked_dai.address)  == 0
    #########################################################
    ##  fund money back into the contract to pay the bulls ##
    #########################################################
    funds_deposited = fund_deposited * 10 ** 6
    mocked_usdc.transfer(TheRanchBullsAirDrop.address,funds_deposited, {"from": owner})


    assert TheRanchBullsAirDrop.getBalance({"from": owner}) == 0
    assert TheRanchBullsAirDrop.checkTokenBalance(mocked_usdc.address)  == funds_deposited
    assert TheRanchBullsAirDrop.checkTokenBalance(mocked_dai.address)  == 0

   

    ##############################################
    ## Set the centennialAirDrop token address ###
    ##############################################

    TheRanchBullsAirDrop.setRewardTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsAirDrop.setRewardTokenDecimals(6,{"from": owner})


    ##############################################
    ##     Set the Minting contract address    ###
    ##############################################

    TheRanchBullsAirDrop.setTheRanchBullsMintAddress(TheRanchBullsMint.address,{"from": owner})

    ########################
    ### Reward the Bulls ###
    ########################
    
    
    
    tx_openAwardState = TheRanchBullsAirDrop.openAwardState({"from": owner})
    tx_centennialAirDrop = TheRanchBullsAirDrop.centennialAirDrop({"from": owner})
    tx_centennialAirDrop.wait(1)

    print(f'{"#"*50} EMIT DATA {"#"*50}')
    print(tx_centennialAirDrop.events)
    print(f'\n{"#"*100}\n\n')

    print(tx_centennialAirDrop.events["centennial_Air_Drop"]["giveawayId"])
    print(tx_centennialAirDrop.events["centennial_Air_Drop"]["payout_cut"])
    print(tx_centennialAirDrop.events["centennial_Air_Drop"]["winners"])
    print(f'{"#"*50} EMIT DATA {"#"*50}')

    print('\n\n')
    

    #####################################################
    ## Check ownership of NFT from both contract calls ##
    #####################################################
    
    assert TheRanchBullsMint.ownerOf(1) == TheRanchBullsAirDrop.verifyNFTOwnerOf(1,{"from": owner})
    assert TheRanchBullsMint.ownerOf(12) == TheRanchBullsAirDrop.verifyNFTOwnerOf(12,{"from": owner})
    assert TheRanchBullsMint.ownerOf(123) == TheRanchBullsAirDrop.verifyNFTOwnerOf(123,{"from": owner})
    assert TheRanchBullsMint.ownerOf(136) == TheRanchBullsAirDrop.verifyNFTOwnerOf(136,{"from": owner})
    assert TheRanchBullsMint.ownerOf(136) != TheRanchBullsAirDrop.verifyNFTOwnerOf(116,{"from": owner}) 


    print(f'\nBeginning Balance before airdrop: {funds_deposited/10**6}')

    ########################
    ### Assert dev cuts  ###
    ########################


    dev1_balance = mocked_usdc.balanceOf(dev1) / 10**6
    dev2_balance = mocked_usdc.balanceOf(dev2) / 10**6

    print(f'dev1 usdc Balance: {dev1_balance}')
    print(f'dev2 usdc Balance: {dev2_balance}')

    assert ((mocked_usdc.balanceOf(dev1)  + mocked_usdc.balanceOf(dev2)) / 10**6) == (funds_deposited / 10**6) * 0.20

    weekly_winners = list(tx_centennialAirDrop.events["centennial_Air_Drop"]["winners"])


    
    print(f'\n\n{len(weekly_winners)} Winners:  {weekly_winners}\n\n')


    minting_cost_total = 250 * mints_per_person  #cost * countOfMints
    payout_reward = tx_centennialAirDrop.events["centennial_Air_Drop"]["payout_cut"]/10**6

    print(f'payout_reward: {payout_reward}')

    payout_total = payout_reward * 100
    print(f'payout_total: {payout_total}')
    assert payout_total + dev1_balance + dev2_balance == funds_deposited /10 ** 6
    
    





    #########################################################################
    wins_per_person = {}

    for i in range(persons):
        wins_per_person[f"person_{i}"] = {}
        wins_per_person[f"person_{i}"]["win_total"] = 0
        wins_per_person[f"person_{i}"]["winning_numbers"] = []


    person_mint_mapping = {
        (1,10):"0",
        (11,20):"1",
        (21,30):"2",
        (31,40):"3",
        (41,50):"4",
        (51,60):"5",
        (61,70):"6",
        (71,80):"7",
        (81,90):"8",
        (91,100):"9",
        (101,110):"10",
        (111,120):"11",
        (121,130):"12",
        (131,140):"13",
        (141,150):"14",
        (151,160):"15",
        (161,170):"16",
        (171,180):"17",
        (181,190):"18",
        (191,200):"19",
        (201,210):"20",
        (211,220):"21",
        (221,230):"22",
        (231,240):"23",
        (241,250):"24",
        (251,260):"25",
        (261,270):"26",
        (271,280):"27",
        (281,290):"28",
        (291,300):"29",
        (301,310):"30",
        (311,320):"31",
        (321,330):"32",
        (331,340):"33",
        (341,350):"34",
        (351,360):"35",
        (361,370):"36",
        (371,380):"37",
        (381,390):"38",
        (391,400):"39"
    }

    for num in weekly_winners:
        for spread,person in person_mint_mapping.items():
            if num >= spread[0] and num <= spread[1]:
                wins_per_person[f'person_{person}']["win_total"] += 1
                wins_per_person[f"person_{person}"]["winning_numbers"].append(num)

    
    pprint.pprint(wins_per_person)
    ###########################################################################


    print(f'person_0 ETH Balance: {person_0.balance()/10**18}')
    print(f'person_0 usdc Balance: {mocked_usdc.balanceOf(person_0) / 10**6}')

    print(f'person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')

    print(f'person_2 ETH Balance: {person_2.balance()/10**18}')
    print(f'person_2 usdc Balance: {mocked_usdc.balanceOf(person_2) / 10**6}')




    wins = int(((mocked_usdc.balanceOf(person_0) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_0) / 10**6) - 7500)
    print(f'person_0: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_0']["win_total"]
    assert wins * payout_reward == increase 
    if len(wins_per_person['person_0']["winning_numbers"]) >= 1: 
        assert person_0 == TheRanchBullsMint.ownerOf(wins_per_person['person_0']["winning_numbers"][0])

    
    wins = int(((mocked_usdc.balanceOf(person_1) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_1) / 10**6) - 7500)
    print(f'person_1: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_1']["win_total"]
    assert wins * payout_reward == increase 
    if len(wins_per_person['person_1']["winning_numbers"]) >= 1: 
        assert person_1 == TheRanchBullsMint.ownerOf(wins_per_person['person_1']["winning_numbers"][0])


        wins = int(((mocked_usdc.balanceOf(person_0) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_0) / 10**6) - 7500)
    print(f'person_0: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_0']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_0']["winning_numbers"]) >= 1:
        assert person_0 == TheRanchBullsMint.ownerOf(wins_per_person['person_0']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_1) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_1) / 10**6) - 7500)
    print(f'person_1: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_1']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_1']["winning_numbers"]) >= 1:
        assert person_1 == TheRanchBullsMint.ownerOf(wins_per_person['person_1']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_2) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_2) / 10**6) - 7500)
    print(f'person_2: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_2']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_2']["winning_numbers"]) >= 1:
        assert person_2 == TheRanchBullsMint.ownerOf(wins_per_person['person_2']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_3) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_3) / 10**6) - 7500)
    print(f'person_3: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_3']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_3']["winning_numbers"]) >= 1:
        assert person_3 == TheRanchBullsMint.ownerOf(wins_per_person['person_3']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_4) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_4) / 10**6) - 7500)
    print(f'person_4: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_4']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_4']["winning_numbers"]) >= 1:
        assert person_4 == TheRanchBullsMint.ownerOf(wins_per_person['person_4']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_5) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_5) / 10**6) - 7500)
    print(f'person_5: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_5']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_5']["winning_numbers"]) >= 1:
        assert person_5 == TheRanchBullsMint.ownerOf(wins_per_person['person_5']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_6) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_6) / 10**6) - 7500)
    print(f'person_6: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_6']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_6']["winning_numbers"]) >= 1:
        assert person_6 == TheRanchBullsMint.ownerOf(wins_per_person['person_6']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_7) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_7) / 10**6) - 7500)
    print(f'person_7: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_7']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_7']["winning_numbers"]) >= 1:
        assert person_7 == TheRanchBullsMint.ownerOf(wins_per_person['person_7']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_8) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_8) / 10**6) - 7500)
    print(f'person_8: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_8']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_8']["winning_numbers"]) >= 1:
        assert person_8 == TheRanchBullsMint.ownerOf(wins_per_person['person_8']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_9) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_9) / 10**6) - 7500)
    print(f'person_9: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_9']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_9']["winning_numbers"]) >= 1:
        assert person_9 == TheRanchBullsMint.ownerOf(wins_per_person['person_9']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_10) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_10) / 10**6) - 7500)
    print(f'person_10: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_10']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_10']["winning_numbers"]) >= 1:
        assert person_10 == TheRanchBullsMint.ownerOf(wins_per_person['person_10']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_11) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_11) / 10**6) - 7500)
    print(f'person_11: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_11']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_11']["winning_numbers"]) >= 1:
        assert person_11 == TheRanchBullsMint.ownerOf(wins_per_person['person_11']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_12) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_12) / 10**6) - 7500)
    print(f'person_12: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_12']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_12']["winning_numbers"]) >= 1:
        assert person_12 == TheRanchBullsMint.ownerOf(wins_per_person['person_12']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_13) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_13) / 10**6) - 7500)
    print(f'person_13: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_13']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_13']["winning_numbers"]) >= 1:
        assert person_13 == TheRanchBullsMint.ownerOf(wins_per_person['person_13']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_14) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_14) / 10**6) - 7500)
    print(f'person_14: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_14']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_14']["winning_numbers"]) >= 1:
        assert person_14 == TheRanchBullsMint.ownerOf(wins_per_person['person_14']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_15) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_15) / 10**6) - 7500)
    print(f'person_15: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_15']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_15']["winning_numbers"]) >= 1:
        assert person_15 == TheRanchBullsMint.ownerOf(wins_per_person['person_15']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_16) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_16) / 10**6) - 7500)
    print(f'person_16: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_16']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_16']["winning_numbers"]) >= 1:
        assert person_16 == TheRanchBullsMint.ownerOf(wins_per_person['person_16']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_17) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_17) / 10**6) - 7500)
    print(f'person_17: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_17']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_17']["winning_numbers"]) >= 1:
        assert person_17 == TheRanchBullsMint.ownerOf(wins_per_person['person_17']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_18) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_18) / 10**6) - 7500)
    print(f'person_18: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_18']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_18']["winning_numbers"]) >= 1:
        assert person_18 == TheRanchBullsMint.ownerOf(wins_per_person['person_18']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_19) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_19) / 10**6) - 7500)
    print(f'person_19: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_19']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_19']["winning_numbers"]) >= 1:
        assert person_19 == TheRanchBullsMint.ownerOf(wins_per_person['person_19']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_20) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_20) / 10**6) - 7500)
    print(f'person_20: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_20']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_20']["winning_numbers"]) >= 1:
        assert person_20 == TheRanchBullsMint.ownerOf(wins_per_person['person_20']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_21) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_21) / 10**6) - 7500)
    print(f'person_21: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_21']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_21']["winning_numbers"]) >= 1:
        assert person_21 == TheRanchBullsMint.ownerOf(wins_per_person['person_21']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_22) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_22) / 10**6) - 7500)
    print(f'person_22: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_22']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_22']["winning_numbers"]) >= 1:
        assert person_22 == TheRanchBullsMint.ownerOf(wins_per_person['person_22']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_23) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_23) / 10**6) - 7500)
    print(f'person_23: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_23']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_23']["winning_numbers"]) >= 1:
        assert person_23 == TheRanchBullsMint.ownerOf(wins_per_person['person_23']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_24) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_24) / 10**6) - 7500)
    print(f'person_24: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_24']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_24']["winning_numbers"]) >= 1:
        assert person_24 == TheRanchBullsMint.ownerOf(wins_per_person['person_24']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_25) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_25) / 10**6) - 7500)
    print(f'person_25: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_25']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_25']["winning_numbers"]) >= 1:
        assert person_25 == TheRanchBullsMint.ownerOf(wins_per_person['person_25']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_26) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_26) / 10**6) - 7500)
    print(f'person_26: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_26']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_26']["winning_numbers"]) >= 1:
        assert person_26 == TheRanchBullsMint.ownerOf(wins_per_person['person_26']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_27) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_27) / 10**6) - 7500)
    print(f'person_27: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_27']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_27']["winning_numbers"]) >= 1:
        assert person_27 == TheRanchBullsMint.ownerOf(wins_per_person['person_27']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_28) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_28) / 10**6) - 7500)
    print(f'person_28: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_28']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_28']["winning_numbers"]) >= 1:
        assert person_28 == TheRanchBullsMint.ownerOf(wins_per_person['person_28']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_29) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_29) / 10**6) - 7500)
    print(f'person_29: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_29']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_29']["winning_numbers"]) >= 1:
        assert person_29 == TheRanchBullsMint.ownerOf(wins_per_person['person_29']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_30) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_30) / 10**6) - 7500)
    print(f'person_30: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_30']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_30']["winning_numbers"]) >= 1:
        assert person_30 == TheRanchBullsMint.ownerOf(wins_per_person['person_30']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_31) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_31) / 10**6) - 7500)
    print(f'person_31: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_31']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_31']["winning_numbers"]) >= 1:
        assert person_31 == TheRanchBullsMint.ownerOf(wins_per_person['person_31']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_32) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_32) / 10**6) - 7500)
    print(f'person_32: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_32']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_32']["winning_numbers"]) >= 1:
        assert person_32 == TheRanchBullsMint.ownerOf(wins_per_person['person_32']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_33) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_33) / 10**6) - 7500)
    print(f'person_33: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_33']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_33']["winning_numbers"]) >= 1:
        assert person_33 == TheRanchBullsMint.ownerOf(wins_per_person['person_33']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_34) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_34) / 10**6) - 7500)
    print(f'person_34: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_34']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_34']["winning_numbers"]) >= 1:
        assert person_34 == TheRanchBullsMint.ownerOf(wins_per_person['person_34']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_35) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_35) / 10**6) - 7500)
    print(f'person_35: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_35']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_35']["winning_numbers"]) >= 1:
        assert person_35 == TheRanchBullsMint.ownerOf(wins_per_person['person_35']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_36) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_36) / 10**6) - 7500)
    print(f'person_36: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_36']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_36']["winning_numbers"]) >= 1:
        assert person_36 == TheRanchBullsMint.ownerOf(wins_per_person['person_36']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_37) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_37) / 10**6) - 7500)
    print(f'person_37: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_37']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_37']["winning_numbers"]) >= 1:
        assert person_37 == TheRanchBullsMint.ownerOf(wins_per_person['person_37']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_38) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_38) / 10**6) - 7500)
    print(f'person_38: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_38']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_38']["winning_numbers"]) >= 1:
        assert person_38 == TheRanchBullsMint.ownerOf(wins_per_person['person_38']["winning_numbers"][0])


    wins = int(((mocked_usdc.balanceOf(person_39) / 10**6) - 7500) / payout_reward)
    increase = ((mocked_usdc.balanceOf(person_39) / 10**6) - 7500)
    print(f'person_39: wins: {wins}     $_increase: {increase}')
    assert wins == wins_per_person['person_39']["win_total"]
    assert wins * payout_reward == increase
    if len(wins_per_person['person_39']["winning_numbers"]) >= 1:
        assert person_39 == TheRanchBullsMint.ownerOf(wins_per_person['person_39']["winning_numbers"][0])



