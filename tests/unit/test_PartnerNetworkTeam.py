from curses import use_env
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintAndReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_PartnerNetwork():

    fund_deposited = 80_000

    #owner = accounts[0]
    owner = get_account()
    TheRanchBullsMintAndReward = deploy_contract()

    ### set the address on each contract for to reference other contract ####

 
    # assert contract_balance == 0
    
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


    coinbase = accounts[31]
    coreTeam1 = accounts[32]
    coreTeam2 = accounts[33]


    people = {
        person_1: 'person_1',
        person_2: 'person_2',
        person_3: 'person_3',
        person_4: 'person_4',
        person_5: 'person_5',
        person_6: 'person_6',
        person_7: 'person_7',
        person_8: 'person_8',
        person_9: 'person_9',
        person_10: 'person_10',
        person_11: 'person_11',
        person_12: 'person_12',
 
    }



  
    starting_balance_of_each_account = 50_000 * 10**18


    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": coinbase})


    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

   
    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_usdc,{"from": owner})
    
    # print(f'usdc address : {mocked_usdc.address}')
    # print(f'dai address :  {mocked_dai.address}')
    # print(f'TotalSupplyOfTokens: {mocked_tokens_usdc.totalSupply()/10**18}')
    print(f'CoinbaseMock USDC Balance: {mocked_usdc.balanceOf(coinbase) / 10**6}')
 
    print(f'TheRanchBullsMintAndReward_ETH_balance: {TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) /10**18}')
  
    assert (mocked_usdc.balanceOf(coinbase) / 10**6) == 500_000



 
    #########################################################
    ####       Transfer USDC  each person                ####
    #########################################################
    

    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_2, 10_000 * 10**6, {"from": coinbase})
   
    mocked_usdc.transfer(person_3, 10_000 * 10**6, {"from": coinbase})
   
    mocked_usdc.transfer(person_4, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_5, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_6, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_7, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_8, 10_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_9, 10_000 * 10**6, {"from": coinbase})
  
    mocked_usdc.transfer(person_10, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_11, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_12, 10_000 * 10**6, {"from": coinbase})





    ### set coreTeam wallets ###
    TheRanchBullsMintAndReward.setCoreTeam_1_Address(coreTeam1,{"from": owner})
    TheRanchBullsMintAndReward.setCoreTeam_2_Address(coreTeam2,{"from": owner})

 
    # Owner unpauses contracts
    TheRanchBullsMintAndReward.togglePauseStatus({"from": owner})
    
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": owner})


   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')




    ######################################################
    ###       CHECK BEFORE ANYONE PARTNERS ARE SET   #####
    ######################################################


    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == False

    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_2}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == False
























    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})


    amt = 2
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    tx2 = TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_3})

    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_4})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_5})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_6})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})


    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_7})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_8})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_9})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    TheRanchBullsMintAndReward.setPartnerAddress(person_2, {"from": person_10})
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == True
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
 
    raffleBalanceOnMintContractBeforePickingWinnerRaffle1 = TheRanchBullsMintAndReward.dailyRaffleBalance.call() 


  
    assert TheRanchBullsMintAndReward.totalSupply() == 20
    assert TheRanchBullsMintAndReward.balanceOf(TheRanchBullsMintAndReward) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMintAndReward) == ((20 * 150) * (10 ** 6))
    assert TheRanchBullsMintAndReward.btcMinersBalanceTotal.call() ==   ((20 * 150) * (10 ** 6)) * .90
    assert TheRanchBullsMintAndReward.dailyRaffleBalance.call() ==  ((20 * 150) * (10 ** 6)) * 0.03
    assert TheRanchBullsMintAndReward.warChestBalance.call() ==  ((20 * 150) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.USDCRewardsBalanceTotal.call() == ((20 * 150) * (10 ** 6)) * 0.05
    assert TheRanchBullsMintAndReward.getNumberOfRafflePlayers() == 10

    assert TheRanchBullsMintAndReward.getRafflePlayer(0) == person_1
    assert TheRanchBullsMintAndReward.getRafflePlayer(1) == person_2



    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_1) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_2) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_3) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_4) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_5) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_6) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_7) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_8) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_9) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_10) == True
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_11) == False
    assert TheRanchBullsMintAndReward.getUserAlreadyInDailyRaffleStatus(person_12) == False







    ### Assert Totaly Supply Minted and How many NFTs each person should have ###
    assert TheRanchBullsMintAndReward.totalSupply() == 20
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_1)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_2)) == 2 
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_3)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_4)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_5)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_6)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_7)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_8)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_9)) == 2
    assert len(TheRanchBullsMintAndReward.walletOfOwner(person_10)) == 2




    ####### Person 10 has a change of heart and changes their partner to person_1 ########


    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_1) == 4
    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_2) == 4
    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_3) == 0


    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == False
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == True
    x = TheRanchBullsMintAndReward.setPartnerAddress(person_1, {"from": person_10})
    

    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == True
    assert TheRanchBullsMintAndReward.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == False


    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_1) == 5
    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_2) == 3
    assert  TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_3) == 0







    ######################################################################################
    ### Check if the partner that they person set has minted from the contract before  ###
    ######################################################################################


    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_1) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_2) == True
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_3) == True

    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_11) == False
    assert TheRanchBullsMintAndReward.getHaveTheyMintedBefore(person_12) == False
 


    print(f'team count person_1 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_1)}')
    print(f'team count person_2 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_2)}')
    print(f'team count person_3 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_3)}')
    print(f'team count person_4 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_4)}')
    print(f'team count person_5 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_5)}')
    print(f'team count person_6 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_6)}')
    print(f'team count person_7 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_7)}')
    print(f'team count person_8 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_8)}')
    print(f'team count person_9 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_9)}')
    print(f'team count person_10 : {TheRanchBullsMintAndReward.getPartnerNetworkTeamCount(person_10)}')
