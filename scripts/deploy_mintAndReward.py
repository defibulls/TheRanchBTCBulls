from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMintReward, network, config, MockV3Aggregator
import time



def deploy_contract():

    account = get_account()

    minting_contract = TheRanchBullsMintReward.deploy(

    '0x8E63885B64909d1a6E20d7b20800250bd6b0B5E9',
    '0x3298f2fB511c6a5b45a127e02279A9D84cF62e22',
    "ipfs://QmYnZxzLzCuuSE4gZK6gqGdxzDH9JRy2U3VS2aEEHuSqVj/",

    config["networks"][network.show_active()]["vrfCoordinator"],
    config["networks"][network.show_active()]["gasLane"],
    config["networks"][network.show_active()]["subscriptionId"],
    config["networks"][network.show_active()]["callbackGasLimit"],

    {"from": account},
    publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsMint!")
    return minting_contract


def main():
    deploy_contract()









