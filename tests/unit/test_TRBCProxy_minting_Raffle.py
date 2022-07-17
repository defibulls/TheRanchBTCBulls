
import pprint
import math
from urllib.request import proxy_bypass
import pytest


from brownie import (
    TheRanchBTCBullsCommunity,
    TheRanchBTCBullsCommunityV2,
    TheRanchBTCBullsChainLinkVRF,
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

from scripts.deploy_mintRaffle import deploy_raffle_contract



def test_TRBCProxy_gas_reward_30_1mintEach_with_transfers():



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



    expected_bonus_for_coreTeam_member = (350 * 10 ** 6)  * 30 * .01
   
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":coreTeam1}) == expected_bonus_for_coreTeam_member
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":coreTeam2}) == expected_bonus_for_coreTeam_member

    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_1}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_2}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_3}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_4}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_5}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_7}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_8}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_9}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_10}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_11}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_12}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_13}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_14}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_15}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_16}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_17}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_18}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_19}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_20}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_21}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_22}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_23}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_24}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_25}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_26}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_27}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_28}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_29}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_30}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_32}) == 0





    # get raffleplayerscount 
    # get raffle balance 
    assert proxy_TRBC.getNumberOfRafflePlayers() == 30

    assert proxy_TRBC.dailyRaffleBalance.call() == 30 * (350*10**6) * 0.03               ## raffle3 is 3% of all mint transactions 







    ###################################
    ### DEPLOY THE FEEDING CONTRACT ###
    ###################################

    TheRanchBullsRaffleContract = deploy_raffle_contract(multisig)



    ###########################################################################################################################################################################
    ###########################################################################################################################################################################
    ## Key takeaway here is that we are importing the functions of the TheRanchBTCBullsCommunity Contract but when we go to call the function, we point to the proxy address ##
    ###########################################################################################################################################################################
    ###########################################################################################################################################################################




    ### set address ###
    TheRanchBullsRaffleContract.setTheRanchBTCBullsCommunityAddress(proxy_TRBC,{"from": multisig})


    #### set the defender wallet up to allow this ###
    proxy_TRBC.setDefenderRole(defender_wallet, True, {"from": multisig})
    proxy_TRBC.setChainlinkVrfRole(TheRanchBullsRaffleContract, True, {"from": multisig})

    ### pause the contract ###
    proxy_TRBC.setPauseStatus(True, {"from": defender_wallet})

   

    TheRanchBullsRaffleContract.setDefenderRole(defender_wallet, True, {"from": multisig})


    with pytest.raises(exceptions.VirtualMachineError):
        fullfill_tx = TheRanchBullsRaffleContract.fake_fulfillRandomWords({"from": person_1})   ## failed because person_1 is not authorized


    fullfill_tx = TheRanchBullsRaffleContract.fake_fulfillRandomWords({"from": defender_wallet})
    print(fullfill_tx.info())


    ### unpause the contract ###
    proxy_TRBC.setPauseStatus(False, {"from": defender_wallet})


    assert proxy_TRBC.getNumberOfRafflePlayers() == 0
    assert proxy_TRBC.dailyRaffleBalance.call() == 0             #30 * (350*10**6) * 0.03               ## raffle3 is 3% of all mint transactions 

    assert proxy_TRBC.getUsdcBalanceForAddress({"from":coreTeam1}) == expected_bonus_for_coreTeam_member
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":coreTeam2}) == expected_bonus_for_coreTeam_member
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_1}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_2}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_3}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_4}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_5}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_7}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_8}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_9}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_10}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_11}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_12}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_13}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_14}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_15}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_16}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_17}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_18}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_19}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_20}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_21}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_22}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_23}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_24}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_25}) == 30 * (350*10**6) * 0.03   
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_26}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_27}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_28}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_29}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_30}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_31}) == 0
    assert proxy_TRBC.getUsdcBalanceForAddress({"from":person_32}) == 0






    assert TRBC.getNumberOfRafflePlayers() == 0
    assert TRBC.dailyRaffleBalance.call() == 0        

    assert TRBC.getUsdcBalanceForAddress({"from":coreTeam1}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":coreTeam2}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_1}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_2}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_3}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_4}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_5}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_7}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_8}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_9}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_10}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_11}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_12}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_13}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_14}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_15}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_16}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_17}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_18}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_19}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_20}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_21}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_22}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_23}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_24}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_25}) == 0 
    assert TRBC.getUsdcBalanceForAddress({"from":person_26}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_27}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_28}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_29}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_30}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_31}) == 0
    assert TRBC.getUsdcBalanceForAddress({"from":person_32}) == 0



    return


