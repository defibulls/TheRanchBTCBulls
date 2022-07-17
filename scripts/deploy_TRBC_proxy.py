from http.client import UPGRADE_REQUIRED
from brownie import (
    Box,
    BoxV2,
    TheRanchBTCBullsCommunity,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
    Contract,
)
from scripts.helpful_scripts import get_account, encode_function_data, upgrade


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    TheRanchBTCBulls = TheRanchBTCBullsCommunity.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # # Optional, deploy the ProxyAdmin and use that as the admin contract
    # proxy_admin = ProxyAdmin.deploy(
    #     {"from": account},
    #     publish_source=config["networks"][network.show_active()]["verify"],
    # )

    # If we want an intializer function we can add
    # `initializer=box.store, 1`
    # to simulate the initializer being the `store` function
    # with a `newValue` of 1
    bulls_encoded_initializer_function = encode_function_data()
    # box_encoded_initializer_function = encode_function_data(initializer=box.store, 1)
    proxy = TransparentUpgradeableProxy.deploy(
        TheRanchBTCBulls.address,
        bulls_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Proxy deployed to {proxy} ! You can now upgrade it just incase!")
    # proxy_bulls = Contract.from_abi("Box", proxy.address, TheRanchBTCBulls.abi)
    # proxy_bulls.store(1,{"from": account})
   
    #print(f"Here is the initial value in the Box: {proxy_box.retrieve()}")

    return







