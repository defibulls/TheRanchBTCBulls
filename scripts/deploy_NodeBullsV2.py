from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import Nodebulls_V2, network, config, MockV3Aggregator
import time



def deploy_AirDrop_contract():
    account = get_account()

    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    
    nodebulls = Nodebulls_V2.deploy(
        get_account(index=99),
        get_account(index=98),
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed TheRanchBullsAirDrop!")
    return nodebulls


def main():
    deploy_AirDrop_contract()




#         price_feed_address,