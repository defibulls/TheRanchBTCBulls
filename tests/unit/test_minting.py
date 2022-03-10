from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint






def test_if_someone_can_start_minting_as_soon_as_contract_is_deployed():
    owner = get_account()
    TheRanchBullsMint = deploy_mint_contract()
  
    contract_balance = TheRanchBullsMint.getBalance({"from": owner})
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    assert contract_balance == 0
    
    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]
    

    ##########################################
    ## Give each person mocked USDC and DAI ##
    ##########################################

    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": owner})

    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

    TheRanchBullsMint.setMintingTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenDecimals(6,{"from": owner})
        
    print(f'TheRanchBullsMint_ETH_balance: {TheRanchBullsMint.getBalance()/10**18}')
  
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 500_000
 
    #########################################################
    ####       Transfer USDC and DAI to each person      ####
    #########################################################
    

    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": owner})
    mocked_usdc.transfer(person_2, 10_000 * 10**6, {"from": owner})
    assert (mocked_usdc.balanceOf(person_1) / 10**6) == 10_000

    
    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_1})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(3,{"from": person_1})             #should fail as contract is paused











    

def test_if_only_whitelist_or_presale_people_can_mint_when_presale_starts():
    owner = get_account()
    TheRanchBullsMint = deploy_mint_contract()
  
    contract_balance = TheRanchBullsMint.getBalance({"from": owner})
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    assert contract_balance == 0
    
    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]
    

    ##########################################
    ## Give each person mocked USDC and DAI ##
    ##########################################

    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": owner})

    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

    TheRanchBullsMint.setMintingTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenDecimals(6,{"from": owner})
        
    print(f'TheRanchBullsMint_ETH_balance: {TheRanchBullsMint.getBalance()/10**18}')
  
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 500_000
 
    #########################################################
    ####       Transfer USDC and DAI to each person      ####
    #########################################################
    

    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": owner})
    mocked_usdc.transfer(person_2, 10_000 * 10**6, {"from": owner})
    mocked_usdc.transfer(person_3, 10_000 * 10**6, {"from": owner})
    assert (mocked_usdc.balanceOf(person_1) / 10**6) == 10_000

    
    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_1})
    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_2})
    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_3})



    # Owner unpauses contract
    TheRanchBullsMint.togglePauseStatus({"from": owner})

    TheRanchBullsMint.addToWhiteList([person_1])
    assert TheRanchBullsMint.isWhitelisted(person_1) == True
    assert TheRanchBullsMint.isPresalelisted(person_1) == False

    TheRanchBullsMint.addToPresaleList([person_2])
    assert TheRanchBullsMint.isWhitelisted(person_2) == False
    assert TheRanchBullsMint.isPresalelisted(person_2) == True

    assert TheRanchBullsMint.isWhitelisted(person_3) == False
    assert TheRanchBullsMint.isPresalelisted(person_3) == False


    # Owner starts presale on the contract
    TheRanchBullsMint.togglePresaleStatus({"from": owner})

    TheRanchBullsMint.mint(3,{"from": person_1})
    TheRanchBullsMint.mint(3,{"from": person_2})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(3,{"from": person_3})








def test_whitelist_person_cannot_mint_then_sell_and_mint_again():
    owner = get_account()
    TheRanchBullsMint = deploy_mint_contract()
  
    contract_balance = TheRanchBullsMint.getBalance({"from": owner})
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    assert contract_balance == 0
    
    person_1 = accounts[1]
    person_2 = accounts[2]
   

    ##########################################
    ## Give each person mocked USDC and DAI ##
    ##########################################

    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": owner})

    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

    TheRanchBullsMint.setMintingTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenDecimals(6,{"from": owner})
        
    print(f'TheRanchBullsMint_ETH_balance: {TheRanchBullsMint.getBalance()/10**18}')
  
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 500_000
 

    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": owner})
    assert (mocked_usdc.balanceOf(person_1) / 10**6) == 10_000

    # Owner unpauses contract
    TheRanchBullsMint.togglePauseStatus({"from": owner})
    # Owner starts presale on the contract
    TheRanchBullsMint.togglePresaleStatus({"from": owner})
    
    
    TheRanchBullsMint.addToWhiteList([person_1])

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_1})
    TheRanchBullsMint.mint(3,{"from": person_1})
    

    
    assert TheRanchBullsMint.addressPurchases(person_1) == 3
    assert TheRanchBullsMint.addressPurchases(person_2) == 0
    assert TheRanchBullsMint.ownerOf(1) == person_1
    assert TheRanchBullsMint.ownerOf(1) != person_2

    TheRanchBullsMint.transferFrom(person_1, person_2, 1, {"from": person_1})    
    assert TheRanchBullsMint.ownerOf(1) != person_1
    assert TheRanchBullsMint.ownerOf(1) == person_2

    assert TheRanchBullsMint.addressPurchases(person_1) == 3
    assert TheRanchBullsMint.addressPurchases(person_2) == 0

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*1)*10**6),{"from":person_1})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(3,{"from": person_1})          # should fail as this would be the 6th NFT minted from this person
 





def test_whitelist_person_mints_presale_max_then_gets_to_nftmax_during_publicsale():
    owner = get_account()
    TheRanchBullsMint = deploy_mint_contract()
  
    contract_balance = TheRanchBullsMint.getBalance({"from": owner})
    print(f'TheRanchBullsMint_contract_adddress: {TheRanchBullsMint.address}')
    assert contract_balance == 0
    
    person_1 = accounts[1]
    person_2 = accounts[2]
   

    ##########################################
    ## Give each person mocked USDC and DAI ##
    ##########################################

    mocked_usdc = MockedTokens_USDC.deploy(500_000 * 10**6, {"from": owner})

    #######################################################
    #### set the token to use for minting and rewarding ###
    #######################################################

    TheRanchBullsMint.setMintingTokenAddress(mocked_usdc,{"from": owner})
    TheRanchBullsMint.setMintingTokenDecimals(6,{"from": owner})
        
    print(f'TheRanchBullsMint_ETH_balance: {TheRanchBullsMint.getBalance()/10**18}')
  
    assert (mocked_usdc.balanceOf(owner) / 10**6) == 500_000
 

    mocked_usdc.transfer(person_1, 10_000 * 10**6, {"from": owner})
    assert (mocked_usdc.balanceOf(person_1) / 10**6) == 10_000

    # Owner unpauses contract
    TheRanchBullsMint.togglePauseStatus({"from": owner})
    # Owner starts presale on the contract
    TheRanchBullsMint.togglePresaleStatus({"from": owner})
    
    
    TheRanchBullsMint.addToWhiteList([person_1])

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_1})
    TheRanchBullsMint.mint(3,{"from": person_1})
    

    
    assert TheRanchBullsMint.addressPurchases(person_1) == 3
    assert TheRanchBullsMint.addressPurchases(person_2) == 0
    assert TheRanchBullsMint.ownerOf(1) == person_1
    assert TheRanchBullsMint.ownerOf(1) != person_2

    TheRanchBullsMint.transferFrom(person_1, person_2, 1, {"from": person_1})    
    assert TheRanchBullsMint.ownerOf(1) != person_1
    assert TheRanchBullsMint.ownerOf(1) == person_2

    assert TheRanchBullsMint.addressPurchases(person_1) == 3
    assert TheRanchBullsMint.addressPurchases(person_2) == 0

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*1)*10**6),{"from":person_1})

    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(3,{"from": person_1})          # should fail as this would be the 6th NFT minted from this person


    # Owner stops presale on the contract
    TheRanchBullsMint.togglePresaleStatus({"from": owner})
    # Owner starts public on the contract
    TheRanchBullsMint.togglePublicSaleStatus({"from": owner})


    mocked_usdc.approve(TheRanchBullsMint.address, ((250*4)*10**6),{"from":person_1})
    TheRanchBullsMint.mint(4,{"from": person_1})
    assert TheRanchBullsMint.addressPurchases(person_1) == 7

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*5)*10**6),{"from":person_1})
    TheRanchBullsMint.mint(5,{"from": person_1})
    assert TheRanchBullsMint.addressPurchases(person_1) == 12

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*6)*10**6),{"from":person_1})
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(6,{"from": person_1})                  #should revert as this exceeds 5 mints per tx
    assert TheRanchBullsMint.addressPurchases(person_1) == 12


    mocked_usdc.approve(TheRanchBullsMint.address, ((250*5)*10**6),{"from":person_1})
    TheRanchBullsMint.mint(5,{"from": person_1})
    assert TheRanchBullsMint.addressPurchases(person_1) == 17

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*4)*10**6),{"from":person_1})
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(4,{"from": person_1})                        # should fail as this exceeds the max mints per wallet address
    assert TheRanchBullsMint.addressPurchases(person_1) == 17


    mocked_usdc.approve(TheRanchBullsMint.address, ((250*3)*10**6),{"from":person_1})
    TheRanchBullsMint.mint(3,{"from": person_1})
    assert TheRanchBullsMint.addressPurchases(person_1) == 20

    mocked_usdc.approve(TheRanchBullsMint.address, ((250*1)*10**6),{"from":person_1})
    with pytest.raises(exceptions.VirtualMachineError):
        TheRanchBullsMint.mint(1,{"from": person_1})                        # should fail as this exceeds the max mints per wallet address
    assert TheRanchBullsMint.addressPurchases(person_1) == 20


 







    

    


