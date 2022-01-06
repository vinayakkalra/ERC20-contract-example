from brownie import Athereum, network, config
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENV
from web3 import Web3


def deploy_erc20():
    account = get_account()
    token = Athereum.deploy(Web3.toWei(1000000000, "ether"), {"from": account})

    print(f"Contract Deployed to {token}")
    print(token.name())
    return token


def main():
    deploy_erc20()
