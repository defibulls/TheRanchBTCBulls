from scripts.helpful_scripts import get_account, get_contract, deploy_mocks, fund_with_link, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from brownie import Raffle, network, config, MockV3Aggregator
import time



def deploy_raffle_contract():
    owner = get_account()
    
    
    raffle_contract = Raffle.deploy(
        config["networks"][network.show_active()]["interval"],
        config["networks"][network.show_active()]["vrfCoordinator"],
        config["networks"][network.show_active()]["gasLane"],
        config["networks"][network.show_active()]["subscriptionId"],
        config["networks"][network.show_active()]["callbackGasLimit"],
        {"from": owner},
        publish_source=config["networks"][network.show_active()]["verify"]
    )
    print("Deployed Raffle!")
    return raffle_contract


def main():
    deploy_raffle_contract()


        # address vrfCoordinatorV2,
        # uint64 subscriptionId,
        # bytes32 gasLane, // keyHash
        # uint256 interval,
        # uint256 entranceFee,
        # uint32 callbackGasLimit



    # vrfCoordinator: '0x6168499c0cFfCaCD319c818142124B7A15E857ab'
    # eth_usd_price_feed: '0x6168499c0cFfCaCD319c818142124B7A15E857ab'
    # link_token: '0x01BE23585060835E02B77ef475b0Cc51aA1e0709'
    # subscriptionId: 6251
    # callbackGasLimit: '500000'
    # gasLane: '0xd89b2bf150e3b9e13446986e571fb9cab24b13cea0a43ea20a6049a85cc807cc'
    # fee: 250000000000000000
    # verify: True

