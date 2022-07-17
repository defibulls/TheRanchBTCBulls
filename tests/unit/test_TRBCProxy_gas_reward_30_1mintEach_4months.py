
import pprint
import math
from urllib.request import proxy_bypass
import pytest


from brownie import (
    TheRanchBTCBullsCommunity,
    TheRanchBTCBullsCommunityV2,
    TRBCProxy,
    Contract,
    network,
    config,
    accounts,
    exceptions,
    MockedTokens_USDC,
    MockedTokens_WBTC
)
from scripts.helpful_scripts import get_account, encode_function_data, upgrade, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_TRBCProxy_gas_reward_30_1mintEach_4months():



    deployer = accounts[0]

    account = get_account()
    TRBC = TheRanchBTCBullsCommunity.deploy(
        {"from": deployer},
    )

   
    # proxy_admin = ProxyAdmin.deploy(
    #     {"from": owner},
    # )
    box_encoded_initializer_function = encode_function_data()
    proxy = TRBCProxy.deploy(
        TRBC.address,
        # proxy_admin.address,
        box_encoded_initializer_function,
        {"from": deployer, "gas_limit": 2000000},
    )
    TRBCV2 = TheRanchBTCBullsCommunityV2.deploy(
        {"from": deployer},
    )


    proxy_TRBC = Contract.from_abi("TheRanchBTCBullsCommunity", proxy.address, TRBC.abi)


    coinbase = accounts[10001]
    defender_wallet = accounts[10002]
    multisig = accounts[10003]

    btcMinersSafe = accounts[10006]
    hostingSafe = accounts[10007]
    coreTeam1 = accounts[10004]
    coreTeam2 = accounts[10005]



    mocked_usdc = MockedTokens_USDC.deploy(1_000_000_000 * 10**6, {"from": coinbase})
    mocked_wbtc = MockedTokens_WBTC.deploy(10 * 10**8, {"from": multisig})






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
   





    proxy_TRBC.initialize({"from": multisig })
    TRBC.initialize({"from": multisig })



    print(f'deployer: {deployer}')
    print(f'multisig : {multisig}')
    print(f'owner of proxy_TRBC  : {proxy_TRBC.owner.call()}')
    print(f'owner of TRBC  : {TRBC.owner.call()}')


    DEFAULT_ADMIN_ROLE = proxy.DEFAULT_ADMIN_ROLE.call()

    proxy.hasRole(DEFAULT_ADMIN_ROLE, deployer) == True
    proxy.hasRole(DEFAULT_ADMIN_ROLE, multisig) == False

    proxy.grantRole(DEFAULT_ADMIN_ROLE,multisig,{"from": deployer})
    proxy.revokeRole(DEFAULT_ADMIN_ROLE,deployer,{"from": multisig})

    print(proxy.hasRole(DEFAULT_ADMIN_ROLE, deployer))
    print(proxy.hasRole(DEFAULT_ADMIN_ROLE, multisig))

    proxy.hasRole(DEFAULT_ADMIN_ROLE, deployer) == False
    proxy.hasRole(DEFAULT_ADMIN_ROLE, multisig) == True


    proxy_TRBC.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    proxy_TRBC.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    proxy_TRBC.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    proxy_TRBC.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})
    proxy_TRBC.setCoreTeamAddresses(coreTeam1,coreTeam2,{"from": multisig})



    print("Things needed to unpause the contract")
    print("--------------------------------------")

    print(f' coreTeam1: {proxy_TRBC.coreTeam_1.call()}')
    print(f' coreTeam2: {proxy_TRBC.coreTeam_2.call()}')
    print(f' usdc contract : {proxy_TRBC.usdcTokenContract.call()}')
    print(f' wbtc contract : {proxy_TRBC.wbtcTokenContract.call()}')
    print(f' hosting safe address  : {proxy_TRBC.hostingSafe.call()}')
    print(f' btcMinersSafe address  : {proxy_TRBC.btcMinersSafe.call()}')
    print(f'nftPerAddressLimit: {proxy_TRBC.nftPerAddressLimit.call()}')
    print(f'mintingCost: {proxy_TRBC.mintingCost.call()}')




    print("Things needed to unpause the contract")
    print("--------------------------------------")

    print(f' coreTeam1: {TRBC.coreTeam_1.call()}')
    print(f' coreTeam2: {TRBC.coreTeam_2.call()}')
    print(f' usdc contract : {TRBC.usdcTokenContract.call()}')
    print(f' wbtc contract : {TRBC.wbtcTokenContract.call()}')
    print(f' hosting safe address  : {TRBC.hostingSafe.call()}')
    print(f' btcMinersSafe address  : {TRBC.btcMinersSafe.call()}')
    print(f'nftPerAddressLimit: {TRBC.nftPerAddressLimit.call()}')
    print(f'mintingCost: {TRBC.mintingCost.call()}')




 
    assert proxy_TRBC.nftPerAddressLimit.call() == 50
    assert proxy_TRBC.wbtcTokenDecimals.call() == 8
    assert proxy_TRBC.usdcTokenDecimals.call() == 6

    assert proxy_TRBC.mintingCost.call() == 350
    assert proxy_TRBC.publicSaleLive.call() == False
    assert proxy_TRBC.paused.call() == True

    assert proxy_TRBC.coreTeam_1.call() == coreTeam1
    assert proxy_TRBC.coreTeam_2.call() == coreTeam2




    assert proxy_TRBC.paused.call() == True
    assert TRBC.paused.call() == True


    assert proxy_TRBC.publicSaleLive.call() == False
    assert TRBC.publicSaleLive.call() == False



    proxy_TRBC.setPauseStatus(False, {"from": multisig})
 
    #owner starts the public sale
    proxy_TRBC.togglePublicSaleStatus({"from": multisig})




    assert proxy_TRBC.paused.call() == False
    assert TRBC.paused.call() == True


    assert proxy_TRBC.publicSaleLive.call() == True
    assert TRBC.publicSaleLive.call() == False



    
    def price_needed(count):
        return (count * proxy_TRBC.mintingCost() * 10 ** 6)

 

    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_1})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_2})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_3})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_4})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_5})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_6})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_7})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_8})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_9})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_10})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_11})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_11, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_12})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_12, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_13})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_13, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_14})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_14, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_15})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_15, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_16})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_16, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_17})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_17, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_18})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_18, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_19})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_19, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_20})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_20, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_21})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_21, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_22})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_22, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_23})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_23, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_24})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_24, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_25})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_25, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_26})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_26, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_27})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_27, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_28})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_28, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_29})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_29, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_30})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_30, "value":  price_needed(amt)})






    print(f'Total Mints: {proxy_TRBC.totalSupply()}')
   


    
    print("#######################################################################################")
    print(f'\t\t\t\t\t BEFORE FUNDING AND UPDATING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_1})  }')
    print(f'person_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_2})  }')
    print(f'person_3 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_3})  }')
    print(f'person_4 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_4})  }')
    print(f'person_5 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_5})  }')
    print(f'person_6 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_6})  }')
    print(f'person_7 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7})  }')
    print(f'person_8 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_8})  }')
    print(f'person_9 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_9})  }')



    print("\n")


    print(f'coreTeam_1 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_1})  }')
    print(f'person_2 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_2})  }')
    print(f'person_3 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_3})  }')
    print(f'person_4 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_4})  }')
    print(f'person_5 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_5})  }')
    print(f'person_6 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_6})  }')
    print(f'person_7 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_7})  }')
    print(f'person_8 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_8})  }')
    print(f'person_9 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_9})  }')

    print("\n")

    print(f'coreTeam_1 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam1})  }')
    print(f'coreTeam_2 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam2})  }')
    print(f'person_1 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_1})  }')
    print(f'person_2 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_2})  }')
    print(f'person_3 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_3})  }')
    print(f'person_4 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_4})  }')
    print(f'person_5 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_5})  }')
    print(f'person_6 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_6})  }')
    print(f'person_7 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_7})  }')
    print(f'person_8 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_8})  }')
    print(f'person_9 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_9})  }')









    print(f'Wallet of person_1: {proxy_TRBC.walletOfOwner(person_1)}')
    print(f'Wallet of person_1: {proxy_TRBC.walletOfOwner(person_1)}') 
    print(f'Wallet of person_2: {proxy_TRBC.walletOfOwner(person_2)}') 
    print(f'Wallet of person_3: {proxy_TRBC.walletOfOwner(person_3)}')
    print(f'Wallet of person_4: {proxy_TRBC.walletOfOwner(person_4)}')
    print(f'Wallet of person_5: {proxy_TRBC.walletOfOwner(person_5)}')
    print(f'Wallet of person_6: {proxy_TRBC.walletOfOwner(person_6)}')
    print(f'Wallet of person_7: {proxy_TRBC.walletOfOwner(person_7)}')
    print(f'Wallet of person_8: {proxy_TRBC.walletOfOwner(person_8)}')
    print(f'Wallet of person_9: {proxy_TRBC.walletOfOwner(person_9)}')
    print(f'Wallet of person_10: {proxy_TRBC.walletOfOwner(person_10)}')
    print(f'Wallet of person_11: {proxy_TRBC.walletOfOwner(person_11)}')
    print(f'Wallet of person_12: {proxy_TRBC.walletOfOwner(person_12)}')
    print(f'Wallet of person_13: {proxy_TRBC.walletOfOwner(person_13)}')
    print(f'Wallet of person_14: {proxy_TRBC.walletOfOwner(person_14)}')
    print(f'Wallet of person_15: {proxy_TRBC.walletOfOwner(person_15)}')
    print(f'Wallet of person_16: {proxy_TRBC.walletOfOwner(person_16)}')
    print(f'Wallet of person_17: {proxy_TRBC.walletOfOwner(person_17)}')
    print(f'Wallet of person_18: {proxy_TRBC.walletOfOwner(person_18)}')
    print(f'Wallet of person_19: {proxy_TRBC.walletOfOwner(person_19)}')
    print(f'Wallet of person_20: {proxy_TRBC.walletOfOwner(person_20)}')
    print(f'Wallet of person_21: {proxy_TRBC.walletOfOwner(person_21)}')
    print(f'Wallet of person_22: {proxy_TRBC.walletOfOwner(person_22)}')
    print(f'Wallet of person_23: {proxy_TRBC.walletOfOwner(person_23)}')
    print(f'Wallet of person_24: {proxy_TRBC.walletOfOwner(person_24)}')
    print(f'Wallet of person_25: {proxy_TRBC.walletOfOwner(person_25)}')
    print(f'Wallet of person_26: {proxy_TRBC.walletOfOwner(person_26)}')
    print(f'Wallet of person_27: {proxy_TRBC.walletOfOwner(person_27)}')
    print(f'Wallet of person_28: {proxy_TRBC.walletOfOwner(person_28)}')
    print(f'Wallet of person_29: {proxy_TRBC.walletOfOwner(person_29)}')
    print(f'Wallet of person_30: {proxy_TRBC.walletOfOwner(person_30)}')



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

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,15, {"from": multisig})
   
    tx_set_stockyard = proxy_TRBC.setStockYardInfo(2,16,30, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {proxy_TRBC.stockyardInfo(0)}')
    print(f'stockyard_1: {proxy_TRBC.stockyardInfo(1)}')
    print(f'stockyard_2: {proxy_TRBC.stockyardInfo(2)}')
    print(f'stockyard_3: {proxy_TRBC.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert proxy_TRBC.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0322',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    proxy_TRBC.setReadyToReward({"from": multisig})


    


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    proxy_TRBC.setPauseStatus(True, {"from": defender_wallet})

   



    assert proxy_TRBC.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################

    ### check if we can reward the same stockyard twice or skip a stockyard on accident

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})

    reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(3,{"from": defender_wallet})

    
    reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})
    print(reward_tx.info())





    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = proxy_TRBC.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())



   
    #######################################
    ####         LIQUIDATION        #######
    #######################################
    
    if proxy_TRBC.getLiquidatedArrayLength({"from": defender_wallet}) > 0 :
        liquidate = proxy_TRBC.liquidateOutstandingAccounts({"from": defender_wallet})
        print(liquidate.info())
        liquidation_transfer = liquidate.events['Transfer']['value']


        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})

        
    else: 
        print("NO LIQUIDATION NEEDED")
        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})


    print("#######################################################################################")
    print(f'\t\t\t\t\t AFTER REWARDING')
    print("#######################################################################################")
    print(f'coreTeam_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_1})  }')
    print(f'person_2 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_2})  }')
    print(f'person_3 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_3})  }')
    print(f'person_4 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_4})  }')
    print(f'person_5 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_5})  }')
    print(f'person_6 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_6})  }')
    print(f'person_7 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7})  }')
    print(f'person_8 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_8})  }')
    print(f'person_9 total maintenance fees due: {proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_9})  }')



    print("\n")


    print(f'coreTeam_1 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam1})  }')
    print(f'coreTeam_2 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam2})  }')
    print(f'person_1 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_1})  }')
    print(f'person_2 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_2})  }')
    print(f'person_3 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_3})  }')
    print(f'person_4 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_4})  }')
    print(f'person_5 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_5})  }')
    print(f'person_6 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_6})  }')
    print(f'person_7 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_7})  }')
    print(f'person_8 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_8})  }')
    print(f'person_9 total maintenance fees standing: {proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_9})  }')

    print("\n")

    print(f'coreTeam_1 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam1})  }')
    print(f'coreTeam_2 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam2})  }')
    print(f'person_1 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_1})  }')
    print(f'person_2 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_2})  }')
    print(f'person_3 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_3})  }')
    print(f'person_4 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_4})  }')
    print(f'person_5 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_5})  }')
    print(f'person_6 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_6})  }')
    print(f'person_7 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_7})  }')
    print(f'person_8 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_8})  }')
    print(f'person_9 WBTC balance: {proxy_TRBC.getWbtcBalanceForAddress({"from":person_9})  }')





    expected_bonus_for_owners_not_having_a_partner = ((total_to_deposit * 0.90) * .01)

    

    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam1}) == ((total_to_deposit * 0.08)) + expected_bonus_for_owners_not_having_a_partner
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam2}) == ((total_to_deposit * 0.02)) + expected_bonus_for_owners_not_having_a_partner
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_1}) == (((total_to_deposit * 0.90) * .98) / 30) 
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_2}) == (((total_to_deposit * 0.90) * .98) / 30) 
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_3}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_4}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_5}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_6}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_7}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_8}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_9}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_10}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_11}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_12}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_13}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_14}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_15}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_16}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_17}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_18}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_19}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_20}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_21}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_22}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_23}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_24}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_25}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_26}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_27}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_28}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_29}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_30}) == (((total_to_deposit * 0.90) * .98) / 30)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_32}) == 0



    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam2}) == 0 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_1}) == 1 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_2}) == 1 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_3}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_4}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_5}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_6}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_7}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_8}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_9}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_10}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_11}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_12}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_13}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_14}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_15}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_16}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_17}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_18}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_19}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_20}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_21}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_22}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_23}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_24}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_25}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_26}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_27}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_28}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_29}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_30}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0



    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam1}) == 0 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_1}) == 12000000 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_2}) == 12000000 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_3}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_4}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_5}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_6}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_8}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_9}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_10}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_11}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_12}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_13}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_14}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_15}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_16}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_17}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_18}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_19}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_20}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_21}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_22}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_23}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_24}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_25}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_26}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_27}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_28}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_29}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_30}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_32}) == 0



    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 2                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################


    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,15, {"from": multisig})
   
    tx_set_stockyard = proxy_TRBC.setStockYardInfo(2,16,30, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {proxy_TRBC.stockyardInfo(0)}')
    print(f'stockyard_1: {proxy_TRBC.stockyardInfo(1)}')
    print(f'stockyard_2: {proxy_TRBC.stockyardInfo(2)}')
    print(f'stockyard_3: {proxy_TRBC.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert proxy_TRBC.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0422',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    proxy_TRBC.setReadyToReward({"from": multisig})


    


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    proxy_TRBC.setPauseStatus(True, {"from": defender_wallet})

   



    assert proxy_TRBC.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################

    ### check if we can reward the same stockyard twice or skip a stockyard on accident

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})

    reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(3,{"from": defender_wallet})

    
    reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})
    print(reward_tx.info())





    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = proxy_TRBC.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())



   
    #######################################
    ####         LIQUIDATION        #######
    #######################################
    
    if proxy_TRBC.getLiquidatedArrayLength({"from": defender_wallet}) > 0 :
        liquidate = proxy_TRBC.liquidateOutstandingAccounts({"from": defender_wallet})
        print(liquidate.info())
        liquidation_transfer = liquidate.events['Transfer']['value']


        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})

        
    else: 
        print("NO LIQUIDATION NEEDED")
        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})

    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert proxy_TRBC.paused.call() == False



    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam1}) == ((total_to_deposit * 0.08) * 2) + (expected_bonus_for_owners_not_having_a_partner * 2)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam2}) == ((total_to_deposit * 0.02) * 2) + (expected_bonus_for_owners_not_having_a_partner * 2)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_1}) == (((total_to_deposit * 0.90) * .98) / 30) * 2 
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_2}) == (((total_to_deposit * 0.90) * .98) / 30) * 2 
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_3}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_4}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_5}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_6}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_7}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_8}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_9}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_10}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_11}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_12}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_13}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_14}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_15}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_16}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_17}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_18}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_19}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_20}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_21}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_22}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_23}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_24}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_25}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_26}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_27}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_28}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_29}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_30}) == (((total_to_deposit * 0.90) * .98) / 30) * 2
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_32}) == 0



    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam2}) == 0 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_1}) == 2 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_2}) == 2 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_3}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_4}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_5}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_6}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_7}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_8}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_9}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_10}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_11}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_12}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_13}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_14}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_15}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_16}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_17}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_18}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_19}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_20}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_21}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_22}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_23}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_24}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_25}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_26}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_27}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_28}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_29}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_30}) == 2
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0



    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam1}) == 0 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_1}) == 24000000 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_2}) == 24000000 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_3}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_4}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_5}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_6}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_8}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_9}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_10}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_11}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_12}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_13}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_14}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_15}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_16}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_17}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_18}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_19}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_20}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_21}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_22}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_23}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_24}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_25}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_26}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_27}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_28}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_29}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_30}) == 24000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_32}) == 0



  
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #                                                                              ROUND 3                                                                                #
    #######################################################################################################################################################################
    #######################################################################################################################################################################
    #######################################################################################################################################################################



    #################################################################
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,15, {"from": multisig})
   
    tx_set_stockyard = proxy_TRBC.setStockYardInfo(2,16,30, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {proxy_TRBC.stockyardInfo(0)}')
    print(f'stockyard_1: {proxy_TRBC.stockyardInfo(1)}')
    print(f'stockyard_2: {proxy_TRBC.stockyardInfo(2)}')
    print(f'stockyard_3: {proxy_TRBC.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert proxy_TRBC.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0522',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    proxy_TRBC.setReadyToReward({"from": multisig})


    


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    proxy_TRBC.setPauseStatus(True, {"from": defender_wallet})

   



    assert proxy_TRBC.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################

    ### check if we can reward the same stockyard twice or skip a stockyard on accident

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})

    reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(3,{"from": defender_wallet})

    
    reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})
    print(reward_tx.info())





    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = proxy_TRBC.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())



   
    #######################################
    ####         LIQUIDATION        #######
    #######################################
    
    if proxy_TRBC.getLiquidatedArrayLength({"from": defender_wallet}) > 0 :
        liquidate = proxy_TRBC.liquidateOutstandingAccounts({"from": defender_wallet})
        print(liquidate.info())
        liquidation_transfer = liquidate.events['Transfer']['value']


        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})

        
    else: 
        print("NO LIQUIDATION NEEDED")
        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})


    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert proxy_TRBC.paused.call() == False



    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam1}) == ((total_to_deposit * 0.08) * 3) + (expected_bonus_for_owners_not_having_a_partner * 3)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam2}) == ((total_to_deposit * 0.02) * 3) + (expected_bonus_for_owners_not_having_a_partner * 3)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_1}) == (((total_to_deposit * 0.90) * .98) / 30) * 3 
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_2}) == (((total_to_deposit * 0.90) * .98) / 30) * 3 
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_3}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_4}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_5}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_6}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_7}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_8}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_9}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_10}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_11}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_12}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_13}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_14}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_15}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_16}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_17}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_18}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_19}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_20}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_21}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_22}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_23}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_24}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_25}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_26}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_27}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_28}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_29}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_30}) == (((total_to_deposit * 0.90) * .98) / 30) * 3
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_32}) == 0



    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam2}) == 0 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_1}) == 3 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_2}) == 3 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_3}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_4}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_5}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_6}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_7}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_8}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_9}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_10}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_11}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_12}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_13}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_14}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_15}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_16}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_17}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_18}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_19}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_20}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_21}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_22}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_23}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_24}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_25}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_26}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_27}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_28}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_29}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_30}) == 3
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0



    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam1}) == 0 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_1}) == 36000000 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_2}) == 36000000 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_3}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_4}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_5}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_6}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_8}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_9}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_10}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_11}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_12}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_13}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_14}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_15}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_16}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_17}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_18}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_19}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_20}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_21}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_22}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_23}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_24}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_25}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_26}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_27}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_28}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_29}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_30}) == 36000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_32}) == 0



    ################################################
    ##### Person 7 pays their maintenance fees #####
    ################################################
    
    usdc_rewards_7 = proxy_TRBC.getUsdcBalanceForAddress({"from":person_7})
    maint_fees_7 = proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7})

    print(f'usdc person_7: {usdc_rewards_7}')
    print(f'maint_fees_person_7 {maint_fees_7}')

    if usdc_rewards_7 < maint_fees_7:
        amt_to_approve = maint_fees_7 - usdc_rewards_7
        mocked_usdc.approve(proxy_TRBC.address, amt_to_approve ,{"from":person_7})


    pay_maint_fees_person_7 = proxy_TRBC.payMaintanenceFees({"from": person_7})
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
    ######### owner needs to set the stockyard information  ###########
    #################################################################

    tx_set_stockyard = proxy_TRBC.setStockYardInfo(1,1,15, {"from": multisig})
   
    tx_set_stockyard = proxy_TRBC.setStockYardInfo(2,16,30, {"from": multisig})

    print("\n")
    print(f'stockyard_0: {proxy_TRBC.stockyardInfo(0)}')
    print(f'stockyard_1: {proxy_TRBC.stockyardInfo(1)}')
    print(f'stockyard_2: {proxy_TRBC.stockyardInfo(2)}')
    print(f'stockyard_3: {proxy_TRBC.stockyardInfo(3)}')

    #################################################################
    ######### owner needs to send funds and set the pay per nft  ####
    #################################################################

    assert proxy_TRBC.payPerNftForTheMonth.call() == 0


    total_to_deposit = 1 * 10 ** 8 

    mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0622',{"from": multisig})
    print(fundAndSetPayPerNFT.info())


    # mocked_wbtc.approve(proxy_TRBC,total_to_deposit, {"from":multisig})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fundAndSetPayPerNFT = proxy_TRBC.setPayPerNftForTheMonthAndCurrentRewardingDate(total_to_deposit,'0323',{"from": multisig})




    print(proxy_TRBC.payPerNftForTheMonth.call())

    expected_amt_per_nft = ((total_to_deposit * .90) / proxy_TRBC.totalSupply())
    assert proxy_TRBC.payPerNftForTheMonth.call() == expected_amt_per_nft



    ###########################################################
    ######### owner updates the maintenance fees variable ####
    ###########################################################

    proxy_TRBC.setMonthlyMaintenanceFeePerNFT(12*10**6, {"from": multisig})   # 12 dollars in USDC.e for round 2
    assert proxy_TRBC.calculatedMonthlyMaintenanceFee.call() == 12*10**6

    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})


    ### call the readyToReward function to begin the rewarding process ###
    proxy_TRBC.setReadyToReward({"from": multisig})


    


    ########################################################################################
    ######### Autotasks handle the payout as the defender wallet can do the rest ###########
    ########################################################################################

    ### pause the contract ###
    proxy_TRBC.setPauseStatus(True, {"from": defender_wallet})

   



    assert proxy_TRBC.stockyardsThatHaveBeenRewardedCount.call() == 0


    #######################
    ###      REWARD     ###
    #######################

    ### check if we can reward the same stockyard twice or skip a stockyard on accident

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})

    reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})
    print(reward_tx.info())

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(1,{"from": defender_wallet})

    with pytest.raises(exceptions.VirtualMachineError):
        reward_tx = proxy_TRBC.rewardBulls(3,{"from": defender_wallet})

    
    reward_tx = proxy_TRBC.rewardBulls(2,{"from": defender_wallet})
    print(reward_tx.info())





    ####################################
    ### UPDATE MAINTENANCE STANDING  ###
    ####################################

    update_maint_standing = proxy_TRBC.updateMaintenanceStanding({"from":defender_wallet})

    print(update_maint_standing.info())



   
    #######################################
    ####         LIQUIDATION        #######
    #######################################
    
    if proxy_TRBC.getLiquidatedArrayLength({"from": defender_wallet}) > 0 :
        liquidate = proxy_TRBC.liquidateOutstandingAccounts({"from": defender_wallet})
        print(liquidate.info())
        liquidation_transfer = liquidate.events['Transfer']['value']


        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})

        
    else: 
        print("NO LIQUIDATION NEEDED")
        proxy_TRBC.resetReadyToRewardChecks({"from": defender_wallet})
        proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})



    ##########################
    ### ASSERT INFORMATION ###
    ##########################

    assert proxy_TRBC.paused.call() == False


    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam1}) == ((total_to_deposit * 0.08) * 4) + (expected_bonus_for_owners_not_having_a_partner * 4)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":coreTeam2}) == ((total_to_deposit * 0.02) * 4) + (expected_bonus_for_owners_not_having_a_partner * 4)
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_1}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_2}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_3}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_4}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_5}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_6}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_7}) == (((total_to_deposit * 0.90) * .98) / 30) * 4
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_8}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_9}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_10}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_11}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_12}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_13}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_14}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_15}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_16}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_17}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_18}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_19}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_20}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_21}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_22}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_23}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_24}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_25}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_26}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_27}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_28}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_29}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_30}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getWbtcBalanceForAddress({"from":person_32}) == 0



    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam1}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":coreTeam2}) == 0 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_1}) == 0 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_2}) == 0 
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_3}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_4}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_5}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_7}) == 1
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_8}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_9}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_10}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_11}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_12}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_13}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_14}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_15}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_16}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_17}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_18}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_19}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_20}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_21}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_22}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_23}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_24}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_25}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_26}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_27}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_28}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_29}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_30}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeStandingForAddress({"from":person_31}) == 0


    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam1}) == 0 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":coreTeam2}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_1}) == 0 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_2}) == 0 
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_3}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_4}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_5}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_6}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_7}) == 12000000
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_8}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_9}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_10}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_11}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_12}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_13}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_14}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_15}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_16}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_17}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_18}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_19}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_20}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_21}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_22}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_23}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_24}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_25}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_26}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_27}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_28}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_29}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_30}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getMaintenanceFeeBalanceForAddress({"from":person_32}) == 0