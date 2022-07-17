from urllib.request import proxy_bypass
import pytest


from brownie import (
    TheRanchBTCBullsCommunity,
    TheRanchBTCBullsCommunityV2,
    TRBCProxy,
    TheRanchBullsFeeding,
    Contract,
    network,
    config,
    accounts,
    exceptions,
    MockedTokens_USDC,
    MockedTokens_WBTC
)
from scripts.helpful_scripts import get_account, encode_function_data, upgrade, LOCAL_BLOCKCHAIN_ENVIRONMENTS

from scripts.deploy_bullsFeeding import deploy_feeding_contract


def test_TRBCProxy_feedingContract_works_correctly():



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

 
    print(f'\nBEFORE: person_1 ETH Balance: {person_1.balance()/10**18}')
    print(f'BEFORE: person_1 usdc Balance: {mocked_usdc.balanceOf(person_1) / 10**6}')


    raffleEntryBool = True


    amt = 1
    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_1})
    tx1 = proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})

    proxy_TRBC.setPartnerAddress(person_1,{"from": person_2})
    assert proxy_TRBC.myPartner(person_2) == person_1


    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_2})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(3),{"from":person_3})
    proxy_TRBC.mint(3,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_4})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(proxy_TRBC.address, price_needed(amt),{"from":person_5})
    proxy_TRBC.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})





    assert proxy_TRBC.balanceOf(proxy_TRBC) == 0
    assert mocked_usdc.balanceOf(proxy_TRBC) == ((7 * 350) * (10 ** 6))
    assert proxy_TRBC.btcMinersSafeBalance.call() ==   ((7 * 350) * (10 ** 6)) * .90
    assert proxy_TRBC.hostingSafeBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    assert proxy_TRBC.dailyRaffleBalance.call() ==  ((7 * 350) * (10 ** 6)) * 0.03
    assert proxy_TRBC.USDCRewardsBalance.call() == ((7 * 350) * (10 ** 6)) * 0.05
    
    assert proxy_TRBC.getNumberOfRafflePlayers() == 5
    assert proxy_TRBC.totalSupply() == 7
    assert proxy_TRBC.getRafflePlayer(0,{"from": multisig}) == person_1



    print(f'B coreTeam1 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam1})}')
    print(f'B coreTeam2 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam2})}')
    print(f'B person_1 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_1})}')
    print(f'B person_2 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_2})}')
    print(f'B person_3 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_3})}')
    print(f'B person_4 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_4})}')
    print(f'B person_5 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_5})}')
    print(f'B person_6 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_6})}')
    print(f'B person_7 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_7})}')



    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_1}) == ((1 * 350) * (10 ** 6)) * 0.02
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_2}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_3}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_4}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_5}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_6}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_7}) == 0




    ## let core team withdraw so their starting balance for the test is back at 0


    proxy_TRBC.withdrawUsdcBalance({"from": coreTeam1})
    proxy_TRBC.withdrawUsdcBalance({"from": coreTeam2})





    ###################################
    ### DEPLOY THE FEEDING CONTRACT ###
    ###################################

    TheRanchBullsFeedingContract = deploy_feeding_contract(multisig)


    TheRanchBullsFeedingContract.setUsdcTokenAddress(mocked_usdc,{"from": multisig})



    #### let person 4,5,6,7 mint from the feeding contract ###



    def price_needed(count):
        return (count * TheRanchBullsFeedingContract.mintingCost() * 10 ** 6)

 

    amt = 1
    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_4})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_4, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_5})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_5, "value":  price_needed(amt)})

    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_6})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_6, "value":  price_needed(amt)})


    mocked_usdc.approve(TheRanchBullsFeedingContract.address, price_needed(amt),{"from":person_7})
    TheRanchBullsFeedingContract.mint(amt,{"from": person_7, "value":  price_needed(amt)})



    print('\n\n')
    print(f'person_4 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_4)}')
    print(f'person_5 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_5)}')
    print(f'person_6 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_6)}')
    print(f'person_7 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_7)}')
    print(f'person_8 HayBales: {TheRanchBullsFeedingContract.walletOfOwner(person_8)}')





    ###########################################################################################################################################################################
    ###########################################################################################################################################################################
    ## Key takeaway here is that we are importing the functions of the TheRanchBTCBullsCommunity Contract but when we go to call the function, we point to the proxy address ##
    ###########################################################################################################################################################################
    ###########################################################################################################################################################################



    proxy_TRBC.setEcosystemRole(TheRanchBullsFeedingContract, True, {"from": multisig})
    TheRanchBullsFeedingContract.setTheRanchBullsMintRewardAddress(proxy_TRBC, {"from": multisig})  


    assert proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam1}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam2}) == 0

    pre_hostingSafe_balance = proxy_TRBC.hostingSafeBalance.call()


    TheRanchBullsFeedingContract.feedTheBulls(1,4, 4000)



    # expected cuts for coreteam1 50,50,50,50 = 200
    # expected cuts for coreteam2 50,50,50,50 = 200
    # hosting safe should get 20% of the last two people at 200,200 so that would be 400 


    print(f'A coreTeam1 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam1})}')
    print(f'A coreTeam2 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam2})}') 
    print(f'A person_1 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_1})}')
    print(f'A person_2 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_2})}')
    print(f'A person_3 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_3})}')
    print(f'A person_4 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_4})}')
    print(f'A person_5 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_5})}')
    print(f'A person_6 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_6})}')
    print(f'A person_7 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_7})}')
    print(f'A person_8 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_8})}')
    print(f'A person_9 USDC rewards on contract: {proxy_TRBC.getUsdcBalanceForAddress({"from": person_9})}')



    assert proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam1}) == 200
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": coreTeam2}) == 200
    assert proxy_TRBC.hostingSafeBalance.call() == pre_hostingSafe_balance + 400




    ### persons 4,5 have nfts on both contracts and should get 90% since they don't have a partner set each, 6,7 don't own a BTC bull and should only get 70% of the 1000


    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_1}) == ((1 * 350) * (10 ** 6)) * 0.02
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_2}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_3}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_4}) == 900
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_5}) == 900
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_6}) == 700
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_7}) == 700
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_8}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_9}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from": person_10}) == 0



    assert TRBC.getUsdcBalanceForAddress({"from": coreTeam1}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": coreTeam2}) == 0
    assert TRBC.hostingSafeBalance.call() == 0


    assert TRBC.getUsdcBalanceForAddress({"from": person_1}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_2}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_3}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_4}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_5}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_6}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_7}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_8}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_9}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from": person_10}) == 0








