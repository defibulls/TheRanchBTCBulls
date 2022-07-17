
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


def test_TRBCProxy_PartnerNetworkTeam():



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


    TRBC_proxy = Contract.from_abi("TheRanchBTCBullsCommunity", proxy.address, TRBC.abi)


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

    mocked_usdc.transfer(person_11, 10_000 * 10**6, {"from": coinbase})

    mocked_usdc.transfer(person_12, 10_000 * 10**6, {"from": coinbase})





    TRBC_proxy.initialize({"from": multisig })
    TRBC.initialize({"from": multisig })



    print(f'deployer: {deployer}')
    print(f'multisig : {multisig}')
    print(f'owner of TRBC_proxy  : {TRBC_proxy.owner.call()}')
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


    TRBC_proxy.setUsdcTokenAddress(mocked_usdc,{"from": multisig})
    TRBC_proxy.setWbtcTokenAddress(mocked_wbtc,{"from": multisig})
    TRBC_proxy.setBaseURI("ipfs://aldkfjasdpofe", {"from": multisig})
    TRBC_proxy.setSafeAddresses(hostingSafe,btcMinersSafe,{"from": multisig})
    TRBC_proxy.setCoreTeamAddresses(coreTeam1,coreTeam2,{"from": multisig})



    print("Things needed to unpause the contract")
    print("--------------------------------------")

    print(f' coreTeam1: {TRBC_proxy.coreTeam_1.call()}')
    print(f' coreTeam2: {TRBC_proxy.coreTeam_2.call()}')
    print(f' usdc contract : {TRBC_proxy.usdcTokenContract.call()}')
    print(f' wbtc contract : {TRBC_proxy.wbtcTokenContract.call()}')
    print(f' hosting safe address  : {TRBC_proxy.hostingSafe.call()}')
    print(f' btcMinersSafe address  : {TRBC_proxy.btcMinersSafe.call()}')
    print(f'nftPerAddressLimit: {TRBC_proxy.nftPerAddressLimit.call()}')
    print(f'mintingCost: {TRBC_proxy.mintingCost.call()}')




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




 
    assert TRBC_proxy.nftPerAddressLimit.call() == 50
    assert TRBC_proxy.wbtcTokenDecimals.call() == 8
    assert TRBC_proxy.usdcTokenDecimals.call() == 6

    assert TRBC_proxy.mintingCost.call() == 350
    assert TRBC_proxy.publicSaleLive.call() == False
    assert TRBC_proxy.paused.call() == True

    assert TRBC_proxy.coreTeam_1.call() == coreTeam1
    assert TRBC_proxy.coreTeam_2.call() == coreTeam2




    assert TRBC_proxy.paused.call() == True
    assert TRBC.paused.call() == True


    assert TRBC_proxy.publicSaleLive.call() == False
    assert TRBC.publicSaleLive.call() == False



    TRBC_proxy.setPauseStatus(False, {"from": multisig})
 
    #owner starts the public sale
    TRBC_proxy.togglePublicSaleStatus({"from": multisig})




    assert TRBC_proxy.paused.call() == False
    assert TRBC.paused.call() == True


    assert TRBC_proxy.publicSaleLive.call() == True
    assert TRBC.publicSaleLive.call() == False



    def price_needed(count):
        return (count * TRBC_proxy.mintingCost() * 10 ** 6)



    ######################################################
    ###       CHECK BEFORE ANYONE PARTNERS ARE SET   #####
    ######################################################


    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == False

    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_1, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_2, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_2}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == False



    raffleEntryBool = True

    amt = 2
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_1})
    tx1 = TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_1, "value":  price_needed(amt)})


    amt = 2
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_2})
    tx2 = TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_2, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_1, {"from": person_3})

    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_3, {"from": person_1}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_3})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_3, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_2, {"from": person_4})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_4, {"from": person_2}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_4})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_4, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_1, {"from": person_5})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_5, {"from": person_1}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_5})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_5, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_2, {"from": person_6})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_6, {"from": person_2}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_6})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_6, "value":  price_needed(amt)})


    amt = 2
    TRBC_proxy.setPartnerAddress(person_1, {"from": person_7})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_7, {"from": person_1}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_7})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_7, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_2, {"from": person_8})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_8, {"from": person_2}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_8})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_8, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_1, {"from": person_9})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_9, {"from": person_1}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_9})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_9, "value":  price_needed(amt)})

    amt = 2
    TRBC_proxy.setPartnerAddress(person_2, {"from": person_10})
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == True
    mocked_usdc.approve(TRBC_proxy.address, price_needed(amt),{"from":person_10})
    TRBC_proxy.mint(amt,raffleEntryBool,{"from": person_10, "value":  price_needed(amt)})
    
 


  
    assert TRBC_proxy.balanceOf(TRBC_proxy) == 0
    assert mocked_usdc.balanceOf(TRBC_proxy) == ((20 * 350) * (10 ** 6))
    assert TRBC_proxy.btcMinersSafeBalance.call() ==   ((20 * 350) * (10 ** 6)) * .90
    assert TRBC_proxy.hostingSafeBalance.call() == ((20* 350) * (10 ** 6)) * 0.05
    assert TRBC_proxy.dailyRaffleBalance.call() ==  ((20 * 350) * (10 ** 6)) * 0.03
    assert TRBC_proxy.USDCRewardsBalance.call() == ((20 * 350) * (10 ** 6)) * 0.05
    
    assert TRBC_proxy.getNumberOfRafflePlayers() == 10
    assert TRBC_proxy.totalSupply() == 20
    assert TRBC_proxy.getRafflePlayer(0,{"from": multisig}) == person_1
    assert TRBC_proxy.getRafflePlayer(1,{"from": multisig}) == person_2



    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_1) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_2) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_3) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_4) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_5) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_6) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_7) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_8) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_9) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_10) == True
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_11) == False
    assert TRBC_proxy.getUserAlreadyInDailyRaffleStatus(person_12) == False





    ### Assert Totaly Supply Minted and How many NFTs each person should have ###
    assert TRBC_proxy.totalSupply() == 20
    assert len(TRBC_proxy.walletOfOwner(person_1)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_2)) == 2 
    assert len(TRBC_proxy.walletOfOwner(person_3)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_4)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_5)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_6)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_7)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_8)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_9)) == 2
    assert len(TRBC_proxy.walletOfOwner(person_10)) == 2



    ####### Person 10 has a change of heart and changes their partner to person_1 ########


    assert  TRBC_proxy.getPartnerNetworkTeamCount({"from":person_1}) == 4
    assert  TRBC_proxy.getPartnerNetworkTeamCount({"from":person_2}) == 4
    assert  TRBC_proxy.getPartnerNetworkTeamCount({"from":person_3}) == 0


    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == False
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == True
    x = TRBC_proxy.setPartnerAddress(person_1, {"from": person_10})
    

    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_1}) == True
    assert TRBC_proxy.getAreTheyOnMyPartnerNetworkTeam(person_10, {"from": person_2}) == False



    assert  TRBC_proxy.getPartnerNetworkTeamCount({"from":person_1}) == 5
    assert  TRBC_proxy.getPartnerNetworkTeamCount({"from":person_2}) == 3
    assert  TRBC_proxy.getPartnerNetworkTeamCount({"from":person_3}) == 0







    ######################################################################################
    ### Check if the partner that they person set has minted from the contract before  ###
    ######################################################################################


    assert TRBC_proxy.getHaveTheyMintedBefore(person_1) == True
    assert TRBC_proxy.getHaveTheyMintedBefore(person_2) == True
    assert TRBC_proxy.getHaveTheyMintedBefore(person_3) == True

    assert TRBC_proxy.getHaveTheyMintedBefore(person_11) == False
    assert TRBC_proxy.getHaveTheyMintedBefore(person_12) == False
 


