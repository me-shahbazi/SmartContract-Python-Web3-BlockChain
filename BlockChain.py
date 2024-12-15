# Interact with simple Register.sol smart Contract

from web3 import Web3

# Infura URL for the AVAX Testnet
infura_url = "https://api.avax-test.network/ext/bc/C/rpc"

# https://www.infura.io/blog/post/deploy-an-erc721-smart-contract-and-mint-accounting-nfts-with-infura-and-avalanche-c-chain
# Infura is a Web3 development platform that provides scalable API access to blockchain networks like 
# Ethereum and IPFS (InterPlanetary File System). It simplifies the process of connecting decentralized applications (dApps) 
# to these networks by handling the heavy lifting of node management, data synchronization, and network connectivity.

# Infura offers easy-to-use APIs for interacting with blockchain networks, eliminating the need for developers to run their own node.

# Create a Web3 instance
w3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if w3.is_connected():
    print("Connected to AVAX Testnet Block Chain")
else:
    print("Connection failed")

# Example: Get the latest block number
latest_block = w3.eth.block_number
print(f"Latest Block: {latest_block}")

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

contractAddress = "0x25709e153c097d8C58d34B2810e8EaA09525dEDE" # Enter Your own contract address

# testnet.snowtrace.io -> contract address -> contract -> *Contract ABI* -> Copy + Paste
# Remix IDE -> Deploy -> Pin deployed Contract -> File explorer -> .deploys -> pinned-contracts -> ... .json -> CopyPaste ABI
contractABI= [
  {
    "inputs": [],
    "name": "getInfo",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_info",
        "type": "string"
      }
    ],
    "name": "setInfo",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
# The ABI is a JSON representation of your contract's public interface. 
# It includes details about functions, events, and data types, enabling interaction 
# with the contract from outside (e.g., using JavaScript with Web3.js or ethers.js).

# Without the ABI, you can't encode the data correctly to call the contract's functions 
# or decode the data returned by the contract. It's like trying to use an API without 
# the documentation—you wouldn't know what functions are available, what parameters they require, 
# or what responses to expect.

contract=w3.eth.contract(contractAddress, abi=contractABI) # type: ignore

try: 
    info = contract.functions.getInfo().call()  # type: ignore # getInfo Comes from contract object definition
    print(f"Contract Info: {info}") 
except Exception as e: 
    print(f"An error occurred: {e}")