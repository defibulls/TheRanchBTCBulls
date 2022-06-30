from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsFeeding, network, config, MockV3Aggregator
import time



def deploy_feeding_contract():
    owner = get_account()

    feeding_contract = TheRanchBullsFeeding.deploy(
    

    "ipfs://QmYnZxzLzCuuSE4gZK6gqGdxzDH9JRy2U3VS2aEEHuSqVj/",

    {"from": owner},
    publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsFeeding Contract!")
    return feeding_contract


def main():
    deploy_feeding_contract()












