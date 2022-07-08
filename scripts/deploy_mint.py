from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import TheRanchBullsMint, network, config, MockV3Aggregator
import time



def deploy_mint_contract():
    owner = get_account()
    
    minting_contract = TheRanchBullsMint.deploy(
    
    owner,
    owner,
    "ipfs://QmdUXmi3hQo38im7giUQ1G5RWo16KxR4vN4ao/",
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
    deploy_mint_contract()
