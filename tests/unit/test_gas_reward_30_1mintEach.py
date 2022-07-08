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






def test_gas_30_mints_rewards_and_maint():


    coinbase = accounts[10001]
    defender_wallet = accounts[10002]
    multisig = accounts[10003]

    btcMinersSafe = accounts[10006]
    hostingSafe = accounts[10007]


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





    TheRanchBullsMintAndReward = deploy_contract()
    deployer = TheRanchBullsMintAndReward.owner.call()

    coreTeam1 = TheRanchBullsMintAndReward.coreTeam_1.call()
    coreTeam2 = TheRanchBullsMintAndReward.coreTeam_2.call()


 
    ################################################################
    ## assert the deployer can transfer ownership of the contract ##
    ################################################################

    tx_transfer_ownership = TheRanchBullsMintAndReward.transferOwnership(multisig)
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





    #########################################################
    ####       Transfer USDC  each person                ####
    #########################################################
    

    mocked_usdc.transfer(person_1, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_2, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_3, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_4, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_5, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_6, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_7, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_8, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_9, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_10, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_11, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_12, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_13, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_14, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_15, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_16, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_17, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_18, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_19, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_20, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_21, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_22, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_23, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_24, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_25, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_26, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_27, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_28, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_29, 100_000 * 10**6, {"from": coinbase})
    mocked_usdc.transfer(person_30, 100_000 * 10**6, {"from": coinbase})
   

    change_pause_status = TheRanchBullsMintAndReward.setPauseStatus(False, {"from": multisig})
  
    #owner starts the public sale
    TheRanchBullsMintAndReward.togglePublicSaleStatus({"from": multisig})


   
    def price_needed(count):
        return (count * TheRanchBullsMintAndReward.mintingCost() * 10 ** 6)

 

    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_1})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_2})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_3})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_4})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_5})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_6})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_7})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_8})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_9})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_10})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_11})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_11, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_12})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_12, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_13})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_13, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_14})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_14, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_15})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_15, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_16})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_16, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_17})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_17, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_18})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_18, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_19})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_19, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_20})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_20, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_21})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_21, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_22})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_22, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_23})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_23, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_24})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_24, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_25})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_25, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_26})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_26, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_27})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_27, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_28})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_28, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_29})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_29, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsMintAndReward.address, price_needed(amt),{"from":person_30})
    TheRanchBullsMintAndReward.mint(amt,raffleEntryBool,{"from": person_30, "value":  price_needed(amt)})




    TheRanchBullsMintAndReward.transferFrom(person_1, person_5, 1, {"from": person_1}) 
    TheRanchBullsMintAndReward.transferFrom(person_2, person_5, 2, {"from": person_2}) 
    TheRanchBullsMintAndReward.transferFrom(person_3, person_5, 3, {"from": person_3})
    TheRanchBullsMintAndReward.transferFrom(person_4, person_5, 4, {"from": person_4})
    TheRanchBullsMintAndReward.transferFrom(person_5, person_5, 5, {"from": person_5})
    TheRanchBullsMintAndReward.transferFrom(person_6, person_5, 6, {"from": person_6})
    TheRanchBullsMintAndReward.transferFrom(person_7, person_5, 7, {"from": person_7})
    TheRanchBullsMintAndReward.transferFrom(person_8, person_5, 8, {"from": person_8})
    TheRanchBullsMintAndReward.transferFrom(person_9, person_5, 9, {"from": person_9})
    TheRanchBullsMintAndReward.transferFrom(person_10, person_5, 10, {"from": person_10})










   


    print(f'Total Mints: {TheRanchBullsMintAndReward.totalSupply()}')
   


    
    print("#######################################################################################")
    print(f'\t\t\t\t\t BEFORE FUNDING AND UPDATING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_9})  }')



    print("\n")


    print(f'coreTeam_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_9})  }')

    print("\n")

    print(f'coreTeam_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_1})  }')
    print(f'person_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_2})  }')
    print(f'person_3 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_3})  }')
    print(f'person_4 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_4})  }')
    print(f'person_5 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_5})  }')
    print(f'person_6 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_6})  }')
    print(f'person_7 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_7})  }')
    print(f'person_8 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_8})  }')
    print(f'person_9 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_9})  }')









    print(f'Wallet of person_1: {TheRanchBullsMintAndReward.walletOfOwner(person_1)}')
    print(f'Wallet of person_1: {TheRanchBullsMintAndReward.walletOfOwner(person_1)}') 
    print(f'Wallet of person_2: {TheRanchBullsMintAndReward.walletOfOwner(person_2)}') 
    print(f'Wallet of person_3: {TheRanchBullsMintAndReward.walletOfOwner(person_3)}')
    print(f'Wallet of person_4: {TheRanchBullsMintAndReward.walletOfOwner(person_4)}')
    print(f'Wallet of person_5: {TheRanchBullsMintAndReward.walletOfOwner(person_5)}')
    print(f'Wallet of person_6: {TheRanchBullsMintAndReward.walletOfOwner(person_6)}')
    print(f'Wallet of person_7: {TheRanchBullsMintAndReward.walletOfOwner(person_7)}')
    print(f'Wallet of person_8: {TheRanchBullsMintAndReward.walletOfOwner(person_8)}')
    print(f'Wallet of person_9: {TheRanchBullsMintAndReward.walletOfOwner(person_9)}')
    print(f'Wallet of person_10: {TheRanchBullsMintAndReward.walletOfOwner(person_10)}')
    print(f'Wallet of person_11: {TheRanchBullsMintAndReward.walletOfOwner(person_11)}')
    print(f'Wallet of person_12: {TheRanchBullsMintAndReward.walletOfOwner(person_12)}')
    print(f'Wallet of person_13: {TheRanchBullsMintAndReward.walletOfOwner(person_13)}')
    print(f'Wallet of person_14: {TheRanchBullsMintAndReward.walletOfOwner(person_14)}')
    print(f'Wallet of person_15: {TheRanchBullsMintAndReward.walletOfOwner(person_15)}')
    print(f'Wallet of person_16: {TheRanchBullsMintAndReward.walletOfOwner(person_16)}')
    print(f'Wallet of person_17: {TheRanchBullsMintAndReward.walletOfOwner(person_17)}')
    print(f'Wallet of person_18: {TheRanchBullsMintAndReward.walletOfOwner(person_18)}')
    print(f'Wallet of person_19: {TheRanchBullsMintAndReward.walletOfOwner(person_19)}')
    print(f'Wallet of person_20: {TheRanchBullsMintAndReward.walletOfOwner(person_20)}')
    print(f'Wallet of person_21: {TheRanchBullsMintAndReward.walletOfOwner(person_21)}')
    print(f'Wallet of person_22: {TheRanchBullsMintAndReward.walletOfOwner(person_22)}')
    print(f'Wallet of person_23: {TheRanchBullsMintAndReward.walletOfOwner(person_23)}')
    print(f'Wallet of person_24: {TheRanchBullsMintAndReward.walletOfOwner(person_24)}')
    print(f'Wallet of person_25: {TheRanchBullsMintAndReward.walletOfOwner(person_25)}')
    print(f'Wallet of person_26: {TheRanchBullsMintAndReward.walletOfOwner(person_26)}')
    print(f'Wallet of person_27: {TheRanchBullsMintAndReward.walletOfOwner(person_27)}')
    print(f'Wallet of person_28: {TheRanchBullsMintAndReward.walletOfOwner(person_28)}')
    print(f'Wallet of person_29: {TheRanchBullsMintAndReward.walletOfOwner(person_29)}')
    print(f'Wallet of person_30: {TheRanchBullsMintAndReward.walletOfOwner(person_30)}')



    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 1                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = TheRanchBullsMintAndReward.setStockYardInfo(1,1,15, {"from": multisig})
   
    tx_set_stockyard = TheRanchBullsMintAndReward.setStockYardInfo(2,16,30, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {TheRanchBullsMintAndReward.stockyardInfo(0)}')
    print(f'stockyard_1: {TheRanchBullsMintAndReward.stockyardInfo(1)}')
    print(f'stockyard_2: {TheRanchBullsMintAndReward.stockyardInfo(2)}')
    print(f'stockyard_3: {TheRanchBullsMintAndReward.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0322',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = TheRanchBullsMintAndReward.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(TheRanchBullsMintAndReward.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / TheRanchBullsMintAndReward.totalSupply())
    assert TheRanchBullsMintAndReward.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    TheRanchBullsMintAndReward.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    TheRanchBullsMintAndReward.setReadyToReward({"from": multisig})


    


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    TheRanchBullsMintAndReward.setPauseStatus(True, {"from": defender_wallet})

   



    assert TheRanchBullsMintAndReward.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################

    ### check if we can reward the same stockyard twice or skip a stockyard on accident

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})

    reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = TheRanchBullsMintAndReward.rewardBulls(3,{"from": defender_wallet})

    
    reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(reward_tx.info())





    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = TheRanchBullsMintAndReward.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())



    #######################################
    ####         LIQUIDATION        #######
    #######################################
    
    if TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet}) > 0 :
        liquidate = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": defender_wallet})
        print(liquidate.info())
        liquidation_transfer = liquidate.events['Transfer']['value']
    else: 
        print("NO LIQUIDATION NEEDED")








    return


    print("#######################################################################################")
    print(f'\t\t\t\t\t AFTER REWARDING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees due: {TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_9})  }')



    print("\n")


    print(f'coreTeam_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_1})  }')
    print(f'person_2 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_2})  }')
    print(f'person_3 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_3})  }')
    print(f'person_4 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_4})  }')
    print(f'person_5 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_5})  }')
    print(f'person_6 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_6})  }')
    print(f'person_7 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_7})  }')
    print(f'person_8 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_8})  }')
    print(f'person_9 total maintenance fees standing: {TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_9})  }')

    print("\n")

    print(f'coreTeam_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":coreTeam1})  }')
    print(f'coreTeam_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":coreTeam2})  }')
    print(f'person_1 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_1})  }')
    print(f'person_2 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_2})  }')
    print(f'person_3 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_3})  }')
    print(f'person_4 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_4})  }')
    print(f'person_5 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_5})  }')
    print(f'person_6 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_6})  }')
    print(f'person_7 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_7})  }')
    print(f'person_8 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_8})  }')
    print(f'person_9 WBTC balance: {TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_9})  }')



    expected_bonus_for_owners_not_having_a_partner = (TheRanchBullsMintAndReward.payPerNftForTheMonth.call() * 0.01) * 30


    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":coreTeam1}) == ((total_to_deposit * 0.08)) + expected_bonus_for_owners_not_having_a_partner
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":coreTeam2}) == ((total_to_deposit * 0.02)) + expected_bonus_for_owners_not_having_a_partner

    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_1}) == (((total_to_deposit * 0.90) * .98) / 30) 
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_2}) == (((total_to_deposit * 0.90) * .98) / 30) 
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_3}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_4}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_5}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_6}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_7}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_8}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_9}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_10}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_11}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_12}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_13}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_14}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_15}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_16}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_17}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_18}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_19}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_20}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_21}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_22}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_23}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_24}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_25}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_26}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_27}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_28}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_29}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_30}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcBalanceForTheOwner({"from":person_32}) == 0



    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam1}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":coreTeam2}) == 0 
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_1}) == 1 
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_2}) == 1 
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_3}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_4}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_5}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_6}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_7}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_8}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_9}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_10}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_11}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_12}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_13}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_14}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_15}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_16}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_17}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_18}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_19}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_20}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_21}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_22}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_23}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_24}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_25}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_26}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_27}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_28}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_29}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_30}) == 1
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_31}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesStandingForTheOwner({"from":person_31}) == 0



    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam1}) == 0 
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":coreTeam2}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_1}) == 12000000 
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_2}) == 12000000 
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_3}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_4}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_5}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_6}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_7}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_8}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_9}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_10}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_11}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_12}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_13}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_14}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_15}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_16}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_17}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_18}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_19}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_20}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_21}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_22}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_23}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_24}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_25}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_26}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_27}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_28}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_29}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_30}) == 12000000
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_31}) == 0
    assert TheRanchBullsMintAndReward.getMaintenanceFeesForTheOwner({"from":person_32}) == 0
























































    return





































































    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})



    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False


    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (12*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (12*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 1
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0



    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == ((1*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == ((1*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == ((1*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0





    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 2                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to send funds to the stockyard  ###########
    #################################################################

    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(1,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())





    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(2,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())


    
    assert tx_fundBulls.events["LoadedFundsIntoStockyard"]["amountDeposited"] == total_to_deposit

    print(tx_fundBulls.info())

  

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################


    #######################
    ###      REWARD     ###
    #######################
    TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})

  
    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(fund_and_reward_tx.info())

    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(fund_and_reward_tx.info())


    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})



    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False


    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (24*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (24*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == (24*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 2
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0



    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == ((2*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == ((2*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == ((2*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == ((2*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0


    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 3                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to send funds to the stockyard  ###########
    #################################################################

    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(1,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())





    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(2,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())


    
    assert tx_fundBulls.events["LoadedFundsIntoStockyard"]["amountDeposited"] == total_to_deposit

    print(tx_fundBulls.info())

  

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################


    #######################
    ###      REWARD     ###
    #######################
    TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})

  
    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(fund_and_reward_tx.info())

    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(fund_and_reward_tx.info())


    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})


    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False

    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == (36*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == (36*10**6) 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == (36*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 3
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0


    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == ((3*10**8 * 0.90) / 15) * 0.98   
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == ((3*10**8 * 0.90) / 15) * 0.98  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == ((3*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == ((3*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0








    ################################################
    ##### Person 7 pays their maintenance fees #####
    ################################################
    
    usdc_rewards_7 = TheRanchBullsMintAndReward.getUsdcRewardBalanceForAddress({"from": person_7})
    maint_fees_7 = TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7)

    print(f'usdc person_7: {usdc_rewards_7}')
    print(f'maint_fees_person_7 {maint_fees_7}')

    if usdc_rewards_7 < maint_fees_7:
        amt_to_approve = maint_fees_7 - usdc_rewards_7
        mocked_usdc.approve(TheRanchBullsMintAndReward.address, amt_to_approve ,{"from":person_7})


    pay_maint_fees_person_7 = TheRanchBullsMintAndReward.payMaintanenceFees({"from": person_7})
    print(pay_maint_fees_person_7.info())

    assert pay_maint_fees_person_7.events["Transfer"]["value"] == maint_fees_7 - usdc_rewards_7






    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 4                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################



    #################################################################
    ######### owner needs to send funds to the stockyard  ###########
    #################################################################

    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(1,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())





    amount_to_send = 1 * wbtc_decimals 
    print(f'money to approve : {amount_to_send}')
    total_to_deposit = amount_to_send

    mocked_wbtc.approve(TheRanchBullsMintAndReward,total_to_deposit, {"from":multisig})
    tx_fundBulls = TheRanchBullsMintAndReward.fundBulls(2,total_to_deposit, {"from": multisig})
    print(tx_fundBulls.info())


    
    assert tx_fundBulls.events["LoadedFundsIntoStockyard"]["amountDeposited"] == total_to_deposit

    print(tx_fundBulls.info())

  

    TheRanchBullsMintAndReward.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert TheRanchBullsMintAndReward.calculatedMonthlyMaintenanceFee.call() == 12*10**6


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################


    #######################
    ###      REWARD     ###
    #######################
    TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})

  
    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(1,{"from": defender_wallet})
    print(fund_and_reward_tx.info())

    fund_and_reward_tx = TheRanchBullsMintAndReward.rewardBulls(2,{"from": defender_wallet})
    print(fund_and_reward_tx.info())


    ################################
    ###  UPDATE MAINTENANCE FEES ###
    ################################
 
    tx_update_fees = TheRanchBullsMintAndReward.updateMaintenanceFeesForTheMonth({"from": defender_wallet})
    print(tx_update_fees.info())


    finishing_identifier = tx_update_fees.events["MaintenanceFeeUpdatingEvent"]["sectionMessage"]

    assert 'STEP2DONE' in finishing_identifier


    ###############################
    ###  UPDATE MONTHS BEHIND   ###
    ################################

    tx_updateMonthsBehind = TheRanchBullsMintAndReward.updateMonthsBehindMaintenanceFeeDueDate({"from": defender_wallet})
    print(tx_updateMonthsBehind.info())

    finishing_identifier = tx_updateMonthsBehind.events["MaintenanceFeeEvent"]["sectionMessage"]

    assert 'STEP3DONE' in finishing_identifier



    tx_getLiquidityArrayLength = TheRanchBullsMintAndReward.getLiquidatedArrayLength({"from": defender_wallet})

    if tx_getLiquidityArrayLength < 1:
        print("Liquidation Not Needed")
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})
    else: 
        ############## LIQUIDATION #############
        print(f'Liquidation needed: Account to liquidate is __{tx_getLiquidityArrayLength}__')
        liquidation_event = TheRanchBullsMintAndReward.liquidateOutstandingAccounts({"from": multisig})
        print(liquidation_event.info())
        TheRanchBullsMintAndReward.togglePauseStatus({"from": defender_wallet})






    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert TheRanchBullsMintAndReward.paused.call() == False

    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_1) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_2) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_3) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_4) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_5) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_6) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_7) == (12*10**6)
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_8) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_9) == 0  
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_10) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_11) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_12) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_13) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_14) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_15) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_16) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_17) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_18) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_19) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_20) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_21) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_22) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_23) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_24) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_25) == 0 
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_26) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_27) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_28) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_29) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_30) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_31) == 0
    assert TheRanchBullsMintAndReward.totalMaintanenceFeesDue(person_32) == 0


    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_1) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_2) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_3) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_4) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_5) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_6) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_7) == 1 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_8) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_9) == 0  
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_10) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_11) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_12) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_13) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_14) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_15) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_16) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_17) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_18) == 0 
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_19) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_20) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_21) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_22) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_23) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_24) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_25) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_26) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_27) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_28) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_29) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_30) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_31) == 0
    assert TheRanchBullsMintAndReward.monthsBehindMaintenanceFeeDueDate(person_32) == 0


    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_1}) == 0  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_2}) == 0  
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_3}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_4}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_5}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_6}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_7}) == ((4*10**8 * 0.90) / 15) * 0.98
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_8}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_9}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_10}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_11}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_12}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_13}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_14}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_15}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_16}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_17}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_18}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_19}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_20}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_21}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_22}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_23}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_24}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_25}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_26}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_27}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_28}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_29}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_30}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_31}) == 0
    assert TheRanchBullsMintAndReward.getWbtcRewardBalanceForAddress({"from": person_32}) == 0


