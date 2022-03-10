
from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, TheRanchBullsAirDrop, MockedTokens_DAI, MockedTokens_USDC, network, config, MockV3Aggregator, accounts, exceptions
from scripts.deploy_mint import deploy_mint_contract
from scripts.deploy_AirDrop import deploy_AirDrop_contract
from web3 import Web3
import time, pytest
import pprint





def test_change_dev_address():
    owner = get_account()
    nodebulls = deploy_AirDrop_contract()
    _address1 = "0xa16d0E94d621bDF7aFe469f94FF0485B07503618"
    _address2 = "0xa16d0E94d621bDF7aFe469f94FF0485B07501919"
    
    tx_see_dev1 = nodebulls.see_Dev1_address()
    assert tx_see_dev1 != _address1

    tx_set_dev1 = nodebulls.setdev1(_address1,{"from": owner})
    tx_see_dev1 = nodebulls.see_Dev1_address()
    assert tx_see_dev1 == _address1

    tx_see_dev2 = nodebulls.see_Dev2_address()
    assert tx_see_dev2 != _address2

    tx_set_dev2 = nodebulls.setdev2(_address2,{"from": owner})
    tx_see_dev2 = nodebulls.see_Dev2_address()
    assert tx_see_dev2 == _address2

    assert tx_see_dev2 != tx_see_dev1

    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        tx_set_dev1 = nodebulls.setdev1(_address1,{"from": bad_actor})

    with pytest.raises(exceptions.VirtualMachineError):
        tx_set_dev2 = nodebulls.setdev2(_address2,{"from": bad_actor})
    
 

def test_change_dev_percent():  
    owner = get_account()
    nodebulls = deploy_AirDrop_contract()
    
    dev1_percent_change = 4
    dev2_percent_change = 4
    
    tx_see_dev1_percent = nodebulls.see_Dev1_percent()
    assert tx_see_dev1_percent != dev1_percent_change

    tx_set_dev1_percent = nodebulls.set_Dev1_percent(dev1_percent_change,{"from": owner})
    tx_see_dev1_percent = nodebulls.see_Dev1_percent()
    assert tx_see_dev1_percent == dev1_percent_change

    tx_see_dev2_percent = nodebulls.see_Dev2_percent()
    assert tx_see_dev2_percent != dev2_percent_change

    tx_set_dev2_percent = nodebulls.set_Dev2_percent(dev2_percent_change,{"from": owner})
    tx_see_dev2_percent = nodebulls.see_Dev2_percent()
    assert tx_see_dev2_percent == dev2_percent_change

    assert tx_set_dev2_percent != tx_set_dev1_percent

    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        tx_set_dev1_percent = nodebulls.set_Dev1_percent(dev1_percent_change,{"from": bad_actor})
     
    with pytest.raises(exceptions.VirtualMachineError):
        tx_set_dev2_percent = nodebulls.set_Dev2_percent(dev2_percent_change,{"from": bad_actor})
    
    
 


def test_dev_percent_overflow():
    owner = get_account()
    nodebulls = deploy_AirDrop_contract()
    
    dev1_percent_change = 4
    dev2_percent_change = 3
    
    nodebulls.set_Dev1_percent(dev1_percent_change,{"from": owner})
    assert nodebulls.see_Dev1_percent() == 4
    
    nodebulls.set_Dev2_percent(dev2_percent_change,{"from": owner})
    assert nodebulls.see_Dev2_percent() == 3

    assert nodebulls.see_Dev1_percent() + nodebulls.see_Dev2_percent() == 7

    ##################################################################

    dev1_percent_change = 7
    dev2_percent_change = 7
    
    nodebulls.set_Dev1_percent(dev1_percent_change,{"from": owner})
    assert nodebulls.see_Dev1_percent() == 7
    
    nodebulls.set_Dev2_percent(dev2_percent_change,{"from": owner})
    assert nodebulls.see_Dev2_percent() == 7

    assert nodebulls.see_Dev1_percent() + nodebulls.see_Dev2_percent() == 14

    ###################################################################

    dev1_percent_change = 17
    dev2_percent_change = 2
    
    nodebulls.set_Dev1_percent(dev1_percent_change,{"from": owner})
    assert nodebulls.see_Dev1_percent() == 17
    
    nodebulls.set_Dev2_percent(dev2_percent_change,{"from": owner})
    assert nodebulls.see_Dev2_percent() == 2

    assert nodebulls.see_Dev1_percent() + nodebulls.see_Dev2_percent() == 19

    ###################################################################

    dev1_percent_change = 15
    dev2_percent_change = 5
    
    nodebulls.set_Dev1_percent(dev1_percent_change,{"from": owner})
    assert nodebulls.see_Dev1_percent() == 15
    
    nodebulls.set_Dev2_percent(dev2_percent_change,{"from": owner})
    assert nodebulls.see_Dev2_percent() == 5

    assert nodebulls.see_Dev1_percent() + nodebulls.see_Dev2_percent() == 20

    ###################################################################

    dev1_percent_change = 22
    dev2_percent_change = 24
    
    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.set_Dev1_percent(dev1_percent_change,{"from": owner})
    
    with pytest.raises(exceptions.VirtualMachineError):
        nodebulls.set_Dev2_percent(dev2_percent_change,{"from": owner})
   
    ###################################################################



