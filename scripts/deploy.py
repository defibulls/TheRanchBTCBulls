from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import NodeBulls, network, config, MockV3Aggregator
import time


from brownie import accounts



def deploy_contract():
    account = get_account()

    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    
    nodebulls = NodeBulls.deploy(
        get_account(index=1),
       
        # get_contract("vrf_coordinator").address,
        # get_contract("link_token").address,
        # config["networks"][network.show_active()]["fee"],
        # config["networks"][network.show_active()]["keyhash"],
        # "ipfs://QmdUXmi3hQo38im7giUQ1G5RWo16KxR4vNLfCNyfiLt4ao/",
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed NodeBulls!")
    return nodebulls


def main():
    deploy_contract()


