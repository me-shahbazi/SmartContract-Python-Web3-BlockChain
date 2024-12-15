# Interacting with Smart Contracts on Blockchain

## Abstract
This repository provides a practical demonstration of how to deploy and interact with a simple smart contract on the Avalanche (AVAX) blockchain network. It includes two core components: a Solidity smart contract (`Register.sol`) for storing and retrieving information and a Python script (`BlockChain.py`) utilizing Web3 to interact with the deployed contract. This work exemplifies the synergy between blockchain development and client-side scripting for decentralized applications (dApps).

---

## Introduction
Blockchain technology enables the development of decentralized systems that operate transparently and securely. Smart contracts, programs deployed on blockchains, form the backbone of these systems, allowing users to automate and enforce agreements without intermediaries. This repository features:

1. **Register.sol**: A Solidity smart contract designed to store and retrieve string data.
2. **BlockChain.py**: A Python script leveraging the Web3 library to connect to the Avalanche Testnet and interact with the smart contract.

---

## Files in the Repository
### 1. **Register.sol**
This Solidity smart contract contains two primary functions:
- `setInfo(string _info)`: Allows users to store a string value on the blockchain.
- `getInfo()`: Retrieves the stored string value.

The contract demonstrates the use of:
- Public functions for interaction.
- The Ethereum ABI (Application Binary Interface) for encoding and decoding data.

#### Code Overview
```solidity
pragma solidity ^0.8.0;

contract Register {
    string private info;

    function setInfo(string memory _info) public {
        info = _info;
    }

    function getInfo() public view returns (string memory) {
        return info;
    }
}
```

### 2. **BlockChain.py**
This Python script is used to interact with the deployed `Register.sol` contract. It demonstrates how to:
- Connect to the Avalanche Testnet using Infura as the blockchain node provider.
- Use the Web3 Python library to call smart contract functions.

#### Features
- Connect to the Avalanche blockchain.
- Retrieve the latest block number.
- Invoke the `getInfo` function to fetch stored data.
- Handle contract ABIs for interaction.

#### Code Highlights
```python
from web3 import Web3

infura_url = "https://api.avax-test.network/ext/bc/C/rpc"
w3 = Web3(Web3.HTTPProvider(infura_url))

if w3.is_connected():
    print("Connected to AVAX Testnet Block Chain")
else:
    print("Connection failed")

contractAddress = "0x25709e153c097d8C58d34B2810e8EaA09525dEDE"
contractABI = [
    {
        "inputs": [],
        "name": "getInfo",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "_info", "type": "string"}],
        "name": "setInfo",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

contract = w3.eth.contract(contractAddress, abi=contractABI)
info = contract.functions.getInfo().call()
print(f"Contract Info: {info}")
```

---

## Prerequisites

1. **Software and Tools**
   - [Remix IDE](https://remix.ethereum.org/) for Solidity contract development.
   - [Python 3.x](https://www.python.org/) for running the interaction script.
   - [Node.js](https://nodejs.org/) and npm (optional, for web-based dApps).
   - Infura account for blockchain connectivity.

2. **Blockchain Network**
   - Avalanche Testnet.

3. **Libraries**
   - Web3.py (`pip install web3`).

---

## Deployment and Usage

### Step 1: Deploy the Smart Contract
1. Open `Register.sol` in Remix IDE.
2. Compile the contract using the Solidity compiler (version 0.8.x).
3. Deploy the contract to the Avalanche Testnet.
4. Copy the deployed contract address and ABI.

### Step 2: Configure the Python Script
1. Update `BlockChain.py`:
   - Replace `contractAddress` with the deployed contract address.
   - Use the ABI of the deployed contract.
2. Run the script:
   ```bash
   python BlockChain.py
   ```
3. Verify the output, including the latest block number and contract interactions.

---

## Results and Discussion
The repository demonstrates how to integrate a basic smart contract with a Python-based client. Key takeaways include:
- Effective use of the Web3 library to interact with blockchain.
- A minimalistic yet functional smart contract for learning purposes.

---

## Conclusion
This repository is a concise example for developers interested in exploring blockchain development. By combining Solidity and Python, it lays a foundation for more complex dApp ecosystems. Future enhancements could include:
- Integrating a frontend for user-friendly interactions.
- Expanding contract functionality.

---

## References
- [Web3.py Documentation](https://web3py.readthedocs.io/en/stable/)
- [Remix IDE](https://remix.ethereum.org/)
- [Infura Platform](https://infura.io/)

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

