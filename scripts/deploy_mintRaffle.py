from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBTCBullsChainLinkVRF, network, config, MockV3Aggregator
import time



def deploy_raffle_contract(_deployer):

    raffle_contract = TheRanchBTCBullsChainLinkVRF.deploy(
    

    config["networks"][network.show_active()]["vrfCoordinator"],
    config["networks"][network.show_active()]["gasLane"],
    config["networks"][network.show_active()]["subscriptionId"],
    config["networks"][network.show_active()]["callbackGasLimit"],

    {"from": _deployer},
    publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed TheRanchBullsFeeding Contract!")
    return raffle_contract


def main():
    deploy_raffle_contract()












