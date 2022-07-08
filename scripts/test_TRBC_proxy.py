from operator import index
from py import process
import pytest
from brownie import (
    TheRanchBTCBullsCommunity,
    TheRanchBTCBullsCommunityV2,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    Contract,
    network,
    config,
    accounts,
    exceptions,
)
from scripts.helpful_scripts import get_account, encode_function_data, upgrade


def test_proxy_upgrades():



    owner = accounts[0]
    person_1 = accounts[1]
    person_2 = accounts[2]
    person_3 = accounts[3]

    account = get_account()
    proxy_TRBC = TheRanchBTCBullsCommunity.deploy(
        {"from": owner},
    )
    proxy_admin = ProxyAdmin.deploy(
        {"from": owner},
    )
    box_encoded_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        proxy_TRBC.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": owner, "gas_limit": 1000000},
    )
    proxy_TRBCV2 = TheRanchBTCBullsCommunityV2.deploy(
        {"from": owner},
    )


    proxy_TRBC = Contract.from_abi("TheRanchBTCBullsCommunity", proxy.address, proxy_TRBC.abi)


    print("vvvvvvvvvvvvvvvvvvvvvvv BEFORE UPGRADE vvvvvvvvvvvvvvvvvvvvvvvvv")

    proxy_TRBC.safeMint({"from": person_1})
    proxy_TRBC.safeMint({"from": person_1})
    proxy_TRBC.safeMint({"from": person_1})

    print(proxy_TRBC.walletOfOwner(person_1))
    print(proxy_TRBC.balanceOf(person_1))

    print(f'prize AMT : {proxy_TRBC.prizeAMT(person_1)}')


    print("^^^^^^^^^^^^^^^^^^   BEFORE UPGRADE  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")



    with pytest.raises(AttributeError):
        proxy_TRBC.safeMint10({"from": person_1})


    assert proxy_TRBC.balanceOf(person_1) == 3


    upgrade(owner, proxy, proxy_TRBCV2, proxy_admin_contract=proxy_admin)

    
    proxy_TRBC = Contract.from_abi("TheRanchBTCBullsCommunityV2", proxy.address, proxy_TRBCV2.abi)


    
    # assert proxy_TRBC.balanceOf(person_1) == 3



    print("\n\n\n")

    print("vvvvvvvvvvvvvvvvvvvvvvv AFTER UPGRADE vvvvvvvvvvvvvvvvvvvvvvvvv")
    

    print(proxy_TRBC.walletOfOwner(person_1))
    print(proxy_TRBC.balanceOf(person_1))

    print(f'prize AMT : {proxy_TRBC.prizeAMT(person_1)}')


    proxy_TRBC.safeMint10({"from": person_1})



    print(proxy_TRBC.walletOfOwner(person_1))
    print(proxy_TRBC.balanceOf(person_1))

    print(f'prize AMT : {proxy_TRBC.prizeAMT(person_1)}')


    print("^^^^^^^^^^^^^^^^^^   AFTER UPGRADE  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

 


