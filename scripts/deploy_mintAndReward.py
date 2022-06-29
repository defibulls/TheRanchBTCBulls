from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintAndReward, network, config, MockV3Aggregator
import time



def deploy_contract():
    owner = get_account()

    minting_contract = TheRanchBullsMintAndReward.deploy(
    
    # "ipfs://aliveBulls/",
    # "ipfs://graveyardBulls/",

    "ipfs://QmYnZxzLzCuuSE4gZK6gqGdxzDH9JRy2U3VS2aEEHuSqVj/",

    config["networks"][network.show_active()]["vrfCoordinator"],
    config["networks"][network.show_active()]["gasLane"],
    config["networks"][network.show_active()]["subscriptionId"],
    config["networks"][network.show_active()]["callbackGasLimit"],

    {"from": owner},
    publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsMint!")
    return minting_contract


def main():
    deploy_contract()












