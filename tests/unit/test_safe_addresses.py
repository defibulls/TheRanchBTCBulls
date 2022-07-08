from curses import use_env
from curses.ascii import FF
from distutils import core
from unittest import mock
from pyrsistent import v
from scripts.helpful_scripts import get_account, get_contract, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintReward, MockedTokens_USDC, MockedTokens_WBTC, network, config, MockV3Aggregator, accounts, exceptions, chain
from scripts.deploy_mintAndReward import deploy_contract
from scripts.deploy_v2mocks import deploy_v2mocks
from web3 import Web3
import time, pytest
import pprint
import math






def test_roles():

    fund_deposited = 80_000

 
    coinbase = accounts[101]
    defender_wallet = accounts[102]
    multisig = accounts[103]
    coreTeam1_new = accounts[104]
    coreTeam2_new = accounts[105]

  
    btcMinersSafe = accounts[106]
    hostingSafe = accounts[107]


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


    coinbase = accounts[10001]
    defender_wallet = accounts[10002]
    multisig = accounts[10003]

    btcMinersSafe = accounts[10006]
    hostingSafe = accounts[10007]







    TheRanchBullsMintAndReward = deploy_contract()
    deployer = TheRanchBullsMintAndReward.owner.call()

    coreTeam1 = TheRanchBullsMintAndReward.coreTeam_1.call()
    coreTeam2 = TheRanchBullsMintAndReward.coreTeam_2.call()


 
    ################################################################
    ## assert the deployer can transfer ownership of the contract ##
    ################################################################

    tx_transfer_ownership = TheRanchBullsMintAndReward.transferOwnership(multisig, {"from": deployer})
    print(tx_transfer_ownership.info())

    assert TheRanchBullsMintAndReward.owner.call() != deployer
    assert TheRanchBullsMintAndReward.owner.call() == multisig




    assert TheRanchBullsMintAndReward.paused.call() == True


    mocked_usdc = MockedTokens_USDC.deploy(1_000_000_000 * 10**6, {"from": coinbase})
    mocked_wbtc = MockedTokens_WBTC.deploy(10 * 10**8, {"from": multisig})

    TheRanchBullsMintAndReward.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    TheRanchBullsMintAndReward.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    TheRanchBullsMintAndReward.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    TheRanchBullsMintAndReward.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})





    current_hostingSafe_address = TheRanchBullsMintAndReward.hostingSafe.call()
    current_btcMinersSafe_address = TheRanchBullsMintAndReward.btcMinersSafe.call()

    print(f'current hosting safe: {current_hostingSafe_address}')
    print(f'current btc miners safe: {current_btcMinersSafe_address}')

    assert TheRanchBullsMintAndReward.paused.call() == True

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.setSafeAddresses('0x0000000000000000000000000000000000000000',btcMinersSafe ,{"from": multisig})
        
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.setSafeAddresses(hostingSafe,'0x0000000000000000000000000000000000000000',{"from": multisig})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMintAndReward.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": coreTeam1_new})

    TheRanchBullsMintAndReward.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})

 
    assert  TheRanchBullsMintAndReward.hostingSafe.call() == hostingSafe
    assert  TheRanchBullsMintAndReward.btcMinersSafe.call() ==  btcMinersSafe