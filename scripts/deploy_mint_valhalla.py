from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintValhalla, network, config, MockV3Aggregator
import time



def deploy_mint_valhalla_contract():
    owner = get_account()
    royalties = get_account(index=1)

    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    
    valhalla_contract = TheRanchBullsMintValhalla.deploy(
        royalties,
	    '0xAB594600376Ec9fD91F8e885dADF0CE036862dE0',
        "ipfs://QmdUXmi3hQo38im7giUQ1G5RWo16KxR4vN4ao/",
        {"from": owner},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsMintValhalla!")
    return valhalla_contract


def main():
    deploy_mint_valhalla_contract()
