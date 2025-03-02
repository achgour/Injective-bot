import asyncio

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.transaction import Transaction
from pyinjective.wallet import PrivateKey
from private_key import pv_key
from time import sleep


async def main() -> None:
    
    qty_INJ = float(input('quantité de INJ: '))
    qty_inj = int(qty_INJ*(10**6))
    
    contract = input("contract: ")
    #contract test : inj1j9qnpyzwkc7nxchx2x42s55kvjs6mx5dv6uce7
    #vérifier sur l'explorer qu'il est toujours fermé
    
    # select network: local, testnet, mainnet
    network = Network.mainnet()

    # initialize grpc client
    # set custom cookie location (optional) - defaults to current dir
    client = AsyncClient(network)
    composer = await client.composer()
    await client.sync_timeout_height()

    # load account
    priv_key = PrivateKey.from_hex(pv_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()


    # prepare tx msg
    # NOTE: COIN MUST BE SORTED IN ALPHABETICAL ORDER BY DENOMS
    funds = [
        composer.Coin(
            amount=qty_inj,
            denom="factory/inj1gxf874xgdcza4rtkashrc8w2s3ulaxa3c7lmeh/inj-tt",
        )
    ]
    msg = composer.MsgExecuteContract(
        sender=address.to_acc_bech32(),
        contract=contract,
        msg='{"swap":{"offer_asset":{"info":{"native_token":{"denom":"factory/inj1gxf874xgdcza4rtkashrc8w2s3ulaxa3c7lmeh/inj-tt"}},"amount":"'+str(qty_inj)+'"}}}',
        funds=funds,
    )

    i = -1
    while True:
        await client.get_account(address.to_acc_bech32())
        i += 1
        if i%1000 == 0:
            print(i)
        # build sim tx
        tx = (
            Transaction()
            .with_messages(msg)
            .with_sequence(client.get_sequence())
            .with_account_num(client.get_number())
            .with_chain_id(network.chain_id)
        )
        sim_sign_doc = tx.get_sign_doc(pub_key)
        sim_sig = priv_key.sign(sim_sign_doc.SerializeToString())
        sim_tx_raw_bytes = tx.get_tx_data(sim_sig, pub_key)

        # simulate tx
        (sim_res, success) = await client.simulate_tx(sim_tx_raw_bytes)
        print(sim_res)

        if success:
            # build tx
            gas_price = 500000000
            gas_limit = sim_res.gas_info.gas_used + 300000  # add 20k for gas, fee computation
            gas_fee = "{:.18f}".format((gas_price * gas_limit) / pow(10, 18)).rstrip("0")
            fee = [
                composer.Coin(
                    amount=gas_price * gas_limit,
                    denom=network.fee_denom,
                )
            ]


            # broadcast tx: send_tx_async_mode, send_tx_sync_mode, send_tx_block_mode
            tx = tx.with_gas(gas_limit).with_fee(fee).with_memo("").with_timeout_height(client.timeout_height)
            sign_doc = tx.get_sign_doc(pub_key)
            sig = priv_key.sign(sign_doc.SerializeToString())
            tx_raw_bytes = tx.get_tx_data(sig, pub_key)

            res = await client.send_tx_sync_mode(tx_raw_bytes)
            tx_hash = res.txhash
            print(tx_hash)
            print("gas fee: {} INJ".format(gas_fee))
            print(f"nombre tx sim : {i}")
            
        return


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
