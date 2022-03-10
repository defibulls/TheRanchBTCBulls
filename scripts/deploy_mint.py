from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, network, config, MockV3Aggregator
import time



def deploy_mint_contract():
    account = get_account()

    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    
    nodebulls = TheRanchBullsMint.deploy(
        account,
        "ipfs://QmdUXmi3hQo38im7giUQ1G5RWo16KxR4vNLfCNyfiLt4ao/",
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsMint!")
    return nodebulls


def main():
    deploy_mint_contract()

