from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsReward, network, config, MockV3Aggregator
import time



def deploy_reward_contract():
    owner = get_account()

    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    # else:
    #     deploy_mocks()
    #     price_feed_address = MockV3Aggregator[-1].address
    
    reward_contract = TheRanchBullsReward.deploy(
        {"from": owner},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsReward!")
    return reward_contract


def main():
    deploy_reward_contract()




#         price_feed_address,