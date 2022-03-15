from curses.ascii import US
from unittest import mock
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint



def test_funding_and_withdrawal_of_mint_contract():


    owner = get_account()
    person_1 = get_account(index=1)
    TheRanchBullsMint = deploy_mint_contract()

    contract_balance = TheRanchBullsMint.getBalance({"from": owner})
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    assert contract_balance == 0
    

    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": owner})
    mocked_dai = MockedTokens_DAI.deploy(Web3.toWei(500_000, "ether"), {"from": person_1})


    print(f'Owners Mock USDC Balance: {mocked_usdc.balanceOf(owner) / 10**6}')
    print(f'Onwers Mock DAI Balance: {mocked_dai.balanceOf(owner) / 10**18}')
 

    assert (mocked_usdc.balanceOf(owner) / 10**6) == 500_000
    assert (mocked_dai.balanceOf(person_1) / 10**18) == 500_000




    ###############################################################
    ###        Owner Funds the contract back with USDC          ###
    ###############################################################
    #######################################
    ##  assert no assets on the contract ##
    #######################################
    assert TheRanchBullsMint.getBalance({"from": owner}) == 0
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address)  == 0
    assert TheRanchBullsMint.checkTokenBalance(mocked_dai.address)  == 0

    #########################################################
    ##  fund money back into the contract to pay the bulls ##
    #########################################################
    funds_deposited_owner = 10_000 * 10 ** 6
    mocked_usdc.transfer(TheRanchBullsMint.address,funds_deposited_owner, {"from": owner})


    assert TheRanchBullsMint.getBalance({"from": owner}) == 0
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address)  == funds_deposited_owner
    assert TheRanchBullsMint.checkTokenBalance(mocked_dai.address)  == 0

   
    #################################################################################
    ###        Person_1 Funds the contract back with DAI and ETH to Contract      ###
    #################################################################################

    funds_deposited_person_1_DAI = 100_000 * 10 ** 18
    funds_deposited_person_1_ETH = 25_000 * 10 ** 18
    mocked_dai.transfer(TheRanchBullsMint.address,funds_deposited_person_1_DAI, {"from": person_1})
    TheRanchBullsMint.fund({"from": person_1, "value": funds_deposited_person_1_ETH})

    assert TheRanchBullsMint.getBalance({"from": owner}) == funds_deposited_person_1_ETH
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address)  == funds_deposited_owner
    assert TheRanchBullsMint.checkTokenBalance(mocked_dai.address)  == funds_deposited_person_1_DAI


    ###############################################################
    #### Owner withdraws 5_000 coins from ETH, USDC, DAI  #########
    ###############################################################

    USDC_5K = 5_000 * 10 ** 6
    DAI_5K = 5_000 * 10 ** 18
    ETH_5K = 5_000 * 10 ** 18


    contract_eth_start = TheRanchBullsMint.getBalance({"from": owner})
    contract_usdc_start = TheRanchBullsMint.checkTokenBalance(mocked_usdc.address) 
    contract_dai_start = TheRanchBullsMint.checkTokenBalance(mocked_dai.address)

    assert  contract_eth_start == 25_000 * 10 ** 18
    assert contract_usdc_start == 10_000 * 10 ** 6
    assert contract_dai_start  == 100_000 * 10 ** 18

    owner_eth_start = owner.balance()
    owner_usdc_start =  mocked_usdc.balanceOf(owner) 
    owner_dai_start = mocked_dai.balanceOf(owner)

    assert owner_eth_start == 50_000 * 10 ** 18 
    assert owner_usdc_start == 490_000 * 10 ** 6
    assert owner_dai_start == 0 

    TheRanchBullsMint.withdraw(ETH_5K, {"from": owner})
    TheRanchBullsMint.withdrawToken(mocked_usdc.address, USDC_5K, {"from": owner})
    TheRanchBullsMint.withdrawToken(mocked_dai.address, DAI_5K, {"from": owner})

    assert TheRanchBullsMint.getBalance({"from": owner}) == contract_eth_start - ETH_5K
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address) == contract_usdc_start - USDC_5K
    assert TheRanchBullsMint.checkTokenBalance(mocked_dai.address) == contract_dai_start - DAI_5K

    assert owner.balance() == owner_eth_start + ETH_5K
    assert mocked_usdc.balanceOf(owner) ==  owner_usdc_start + USDC_5K
    assert mocked_dai.balanceOf(owner) ==  owner_dai_start + DAI_5K





    #####################################################
    ### check if person_1 has any withdraw privileges ###
    #####################################################
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.withdraw(ETH_5K, {"from": person_1})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.withdrawToken(mocked_usdc.address, USDC_5K, {"from": person_1})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.withdrawToken(mocked_dai.address, DAI_5K, {"from": person_1})



    #############################
    ### final balances check ####
    #############################
    
    assert TheRanchBullsMint.getBalance({"from": owner}) == contract_eth_start - ETH_5K
    assert TheRanchBullsMint.checkTokenBalance(mocked_usdc.address) == contract_usdc_start - USDC_5K
    assert TheRanchBullsMint.checkTokenBalance(mocked_dai.address) == contract_dai_start - DAI_5K




