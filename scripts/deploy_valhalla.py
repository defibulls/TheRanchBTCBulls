from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import valhalla, network, config, MockV3Aggregator
import time



def deploy_valhalla_contract():
    owner = get_account()
    royalties = get_account(index=1)

    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    
    valhalla_contract = valhalla.deploy(
        {"from": owner},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsMint!")
    return valhalla_contract


def main():
    deploy_valhalla_contract()
