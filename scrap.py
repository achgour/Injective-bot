import asyncio
import ast
from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.composer import Composer




async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.mainnet()
    client = AsyncClient(network)

    block_height = "55327294"
    block = await client.get_block(block_height=block_height)


    txs_hash = [tx.hash.upper()[2:] for tx in block.data.txs if tx.tx_msg_types == b'["/injective.wasmx.v1.MsgExecuteContractCompat"]']
    print(txs_hash)
    composer = Composer(network=network.string())
    for tx_hash in txs_hash:
        
        transaction_response = await client.get_tx_by_hash(tx_hash=tx_hash)
        print(transaction_response)

        transaction_messages = composer.UnpackTransactionMessages(transaction=transaction_response.data)
        print(transaction_messages)
        first_message = transaction_messages[0]
        print(first_message)

    ### si vous voulez tester sur le choix d'un block ###
    #block_height = "55327294"
    #block = await client.get_block(block_height=block_height) 

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())










