
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint




def test_owner_of_contracts():
    owner = get_account()
    actor = get_account(index=2)
    theRanchMint = deploy_mint_contract()
    assert theRanchMint.owner() == owner
    assert theRanchMint.owner() != actor

    theRanchAirDrop = deploy_AirDrop_contract()

    assert theRanchAirDrop.owner() == owner
    assert theRanchAirDrop.owner() != actor




def test_who_can_withdraw_funds():

    owner = get_account()
    actor = get_account(index=2)

    nodebullsMint = deploy_mint_contract()
    tx_withdraw_funds = nodebullsMint.withdraw({"from": owner})
    with pytest.raises(exceptions.VirtualMachineError):
        tx_withdraw_funds = nodebullsMint.withdraw({"from": actor})

    nodebullsAirDrop = deploy_AirDrop_contract()
    tx_withdraw_funds = nodebullsAirDrop.withdraw({"from": owner})
    with pytest.raises(exceptions.VirtualMachineError):
        tx_withdraw_funds = nodebullsAirDrop.withdraw({"from": actor})



def test_who_can_start_public_sale():  
    owner = get_account()
    actor = get_account(index=2)
    nodebulls = deploy_mint_contract()
    tx_toggleSaleStatus = nodebulls.togglePublicSaleStatus({"from": owner})
    with pytest.raises(exceptions.VirtualMachineError):
        tx_toggleSaleStatus = nodebulls.togglePublicSaleStatus({"from": actor})


def test_who_can_start_presale():
    owner = get_account()
    actor = get_account(index=2)
    nodebulls = deploy_mint_contract()
    tx_togglePreSaleStatus = nodebulls.togglePresaleStatus({"from": owner})
    with pytest.raises(exceptions.VirtualMachineError):
        tx_togglePreSaleStatus = nodebulls.togglePresaleStatus({"from": actor})




def test_who_can_change_BaseURI_data():
    owner = get_account()
    actor = get_account(index=2)
    nodebulls = deploy_mint_contract()
    
    URL = "https://ipfs/io/408204582.com"

    tx_set_Base_URI = nodebulls.setBaseURI(URL,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        tx_set_contract_URI = nodebulls.setBaseURI(URL,{"from": actor})
    

def test_set_royalty_address():
    owner = get_account()
    actor = get_account(index=2)
    future_project_wallet = get_account(index=2)
    nodebulls = deploy_mint_contract()


    nodebulls.setRoyaltyAddress(future_project_wallet.address,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.setRoyaltyAddress(actor,{"from": actor})



def test_set_minting_token_address():
    owner = get_account()
    actor = get_account(index=2)
    mocked_usdc = MockedTokens_USDC.deploy(100_000 * 10 ** 6, {"from": owner})

    nodebulls = deploy_mint_contract()

    nodebulls.setMintingTokenAddress(mocked_usdc.address,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.setMintingTokenAddress(mocked_usdc.address,{"from": actor})
    
    

def test_set_minting_token_decimals_change():
    owner = get_account()
    actor = get_account(index=2)

    nodebulls = deploy_mint_contract()

    nodebulls.setMintingTokenDecimals(10,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.setMintingTokenDecimals(10,{"from": actor})



def test_set_price_per_mint():
    owner = get_account()
    actor = get_account(index=2)

    nodebulls = deploy_mint_contract()

    nodebulls.adjustPricePerMint(150,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.adjustPricePerMint(150,{"from": actor})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.adjustPricePerMint(90,{"from": owner})



def test_set_mints_per_tx():
    owner = get_account()
    actor = get_account(index=2)

    nodebulls = deploy_mint_contract()

    nodebulls.adjustMintsPerTransaction(10,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.adjustMintsPerTransaction(10,{"from": actor})
    
def test_set_mints_per_wallet():
    owner = get_account()
    actor = get_account(index=2)

    nodebulls = deploy_mint_contract()

    nodebulls.adjustMintsPerWallet(100,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.adjustMintsPerWallet(100,{"from": actor})
    
    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.adjustMintsPerWallet(10,{"from": owner})
    


def test_open_and_close_award_state():
    owner = get_account()
    actor = get_account(index=2)

    theRanchAirDrop = deploy_AirDrop_contract()

    theRanchAirDrop.openAwardState({"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        theRanchAirDrop.openAwardState({"from": owner})

    theRanchAirDrop.closeAwardState({"from": owner})    

    with pytest.raises(exceptions.VirtualMachineError):
        theRanchAirDrop.openAwardState({"from": actor})

    theRanchAirDrop.openAwardState({"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        theRanchAirDrop.closeAwardState({"from": actor})
    

def test_set_rewards_token_address():
    owner = get_account()
    actor = get_account(index=2)
    mocked_usdc = MockedTokens_USDC.deploy(100_000 * 10 ** 6, {"from": owner})
    mocked_dai = MockedTokens_DAI.deploy(100_000 * 10 ** 18, {"from": actor})

    nodebulls = deploy_AirDrop_contract()

    nodebulls.setRewardTokenAddress(mocked_usdc.address,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.setRewardTokenAddress(mocked_dai.address,{"from": actor})
    



def test_set_rewards_token_decimals_address():
    owner = get_account()
    actor = get_account(index=2)

    nodebulls = deploy_AirDrop_contract()

    nodebulls.setRewardTokenDecimals(12,{"from": owner})

    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.setRewardTokenDecimals(11,{"from": actor})

