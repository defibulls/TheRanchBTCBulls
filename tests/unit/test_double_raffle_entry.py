from curses import use_env
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_reward import deploy_reward_contract
from web3 import Web3
import time, pytest
import pprint
import math






def test_double_raffle_entry():

    fund_deposited = 80_000

    #owner = accounts[0]
    owner = get_account()
    TheRanchBullsMint = deploy_mint_contract()
    TheRanchBullsReward = deploy_reward_contract()

    ### set the address on each contract for to reference other contract ####

    TheRanchBullsMint.setRewardContractAddress(TheRanchBullsReward, {"from": owner})
    TheRanchBullsReward.setTheRanchBullsMintAddress(TheRanchBullsMint, {"from": owner})

    contract_balance = TheRanchBullsMint.balanceOf(TheRanchBullsMint)
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    print(f'TheRanchBullsReward_contract_adddress: {TheRanchBullsReward.address}')
    assert contract_balance == 0
    
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
    person_31 = accounts[34]


    coinbase = accounts[31]
    coreTeam1 = accounts[32]
    coreTeam2 = accounts[33]
    # dev1 = accounts[97]
    # dev2 = accounts[98]

  
    starting_balance_of_each_account = 50_000 * 10**18

    # ##########################################
    # ## Give each person mocked USDC and DAI ##
    # ##########################################


    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": coinbase})


    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

   
    TheRanchBullsMint.setMintingTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenDecimals(6,{"from": owner})
    
    # print(f'usdc address : {mocked_usdc.address}')
    # print(f'dai address :  {mocked_dai.address}')
    # print(f'TotalSupplyOfTokens: {mocked_tokens_usdc.totalSupply()/10**18}')
    print(f'CoinbaseMock USDC Balance: {mocked_usdc.balanceOf(coinbase) / 10**6}')
 
    print(f'TheRanchBullsMint_ETH_balance: {TheRanchBullsMint.balanceOf(TheRanchBullsMint) /10**18}')
  
    assert (mocked_usdc.balanceOf(coinbase) / 10**6) == 500_000



 
    #########################################################
    ####       Transfer USDC and DAI to each person      ####
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

    mocked_usdc.transfer(person_13, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_14, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_15, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_16, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_17, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_18, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_19, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_20, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_21, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_22, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_23, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_24, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_25, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_26, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_27, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_28, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_29, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_30, 10_000 * 10**6, {"from": coinbase})



    ### set coreTeam wallets ###
    TheRanchBullsMint.setCoreTeam1Address(coreTeam1,{"from": owner})
    TheRanchBullsMint.setCoreTeam2Address(coreTeam2,{"from": owner})

 
    # Owner unpauses contracts
    tx_unpause_contract_mint = TheRanchBullsMint.togglePauseStatus({"from": owner})
    tx_unpause_contract_reward = TheRanchBullsReward.togglePauseStatus({"from": owner})

    #owner starts the public sale
    tx_start_public_sale = TheRanchBullsMint.togglePublicSaleStatus({"from": owner})


    def price_needed(count):
        return (count * TheRanchBullsMint.mintingCost() * 10 ** 6)

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')


    assert TheRanchBullsMint.balanceOf(TheRanchBullsMint) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMint) == 0
    assert TheRanchBullsMint.btcMinersBalance.call() == 0
    assert TheRanchBullsMint.USDCRewardsBalance.call() == 0
    assert TheRanchBullsMint.dailyRaffleBalance.call() == 0
    assert TheRanchBullsMint.getNumberOfRafflePlayers() == 0
    assert TheRanchBullsMint.totalSupply() == 0
    assert TheRanchBullsMint.getUserAlreadyInDailyRaffleStatus(person_1) == False



    return

    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(TheRanchBullsMint.address, price_needed(amt),{"from":person_1})
    tx1 = TheRanchBullsMint.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})
    #print(tx1.info())

    

    assert TheRanchBullsMint.balanceOf(TheRanchBullsMint) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMint) == 300 * 10 ** 6
    assert TheRanchBullsMint.btcMinersBalance.call() == (300 * 10 ** 6) * .95
    assert TheRanchBullsMint.USDCRewardsBalance.call() == (300 * 10 ** 6) * .05
    assert TheRanchBullsMint.dailyRaffleBalance.call() == (300 * 10 ** 6) * .03
    assert TheRanchBullsMint.getNumberOfRafflePlayers() == 1
    assert TheRanchBullsMint.totalSupply() == 2
    assert TheRanchBullsMint.getRafflePlayer(0) == person_1
    assert TheRanchBullsMint.getUserAlreadyInDailyRaffleStatus(person_1) == True





    amt = 2
    mocked_usdc.approve(TheRanchBullsMint.address, price_needed(amt),{"from":person_1})
    tx2 = TheRanchBullsMint.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})



    assert TheRanchBullsMint.balanceOf(TheRanchBullsMint) == 0
    assert mocked_usdc.balanceOf(TheRanchBullsMint) == 600 * 10 ** 6
    assert TheRanchBullsMint.btcMinersBalance.call() == (600 * 10 ** 6) * .95
    assert TheRanchBullsMint.USDCRewardsBalance.call() == (600 * 10 ** 6) * .05
    assert TheRanchBullsMint.dailyRaffleBalance.call() == (600 * 10 ** 6) * .03
    assert TheRanchBullsMint.getNumberOfRafflePlayers() == 1
    assert TheRanchBullsMint.totalSupply() == 4
    assert TheRanchBullsMint.getRafflePlayer(0) == person_1
    assert TheRanchBullsMint.getUserAlreadyInDailyRaffleStatus(person_1) == True

    


     ## This doesn't work anymore now that the function is internal ###
    # ### something has to clear the userInDailyRaffle mapping first. 
    # TheRanchBullsMint.resetUserInDailyRaffle()

    # assert TheRanchBullsMint.getNumberOfRafflePlayers() == 1
    # assert TheRanchBullsMint.totalSupply() == 4
    # assert TheRanchBullsMint.getRafflePlayer(0) == person_1
    # assert TheRanchBullsMint.getUserAlreadyInDailyRaffleStatus(person_1) == False






