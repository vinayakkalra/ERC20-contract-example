# ERC-20 Contract using OpenZeppelin standards

Create a simple mintable, burnable ERC20 contract and deploy yours now using this implementation. This repo uses brownie and python to deploy contracts and interact with them.

To create your own ERC-20 on rinkeby chain, follow the below steps:

1. Open deploy_erc20.py inside scripts folder and change the values as per your required values (Name, symbol and token supply)
2. You can find the ERC20 contract in contracts folder. The name of the file is Athereum.sol
3. To deploy on rinkeby, use the below script.

```
brownie run scripts/deploy_erc20.py --network rinkeby
```