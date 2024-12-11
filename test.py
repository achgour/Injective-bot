json_data = {
  body {
    messages {
      type_url: "/cosmwasm.wasm.v1.MsgExecuteContract"
      value: "\n*inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\022*inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\032]{\"swap\":{\"offer_asset\":{\"info\":{\"native_token\":{\"denom\":\"inj\"}},\"amount\":\"100000000000000\"}}}*\026\n\003inj\022\017100000000000000"
    }
    timeout_height: 55415577
  }
  auth_info {
    signer_infos {
      public_key {
        type_url: "/injective.crypto.v1beta1.ethsecp256k1.PubKey"
        value: "\n!\003H\260\265\211-\025V\0343]\326\222\334\017\304\331\260\356\231\332\272kE\273\265\305\361O}\201\371\207"
      }
      mode_info {
        single {
          mode: SIGN_MODE_DIRECT
        }
      }
      sequence: 73
    }
    fee {
      amount {
        denom: "inj"
        amount: "147013500000000"
      }
      gas_limit: 294027
    }
  }
  signatures: "&\016\230wya\335\037,\032\205>mP\335\003B\357\303\250{_-\326\361\251a8\364\270\343\342t\332/\200\327wb\311\236L\226)\247\003\023\226\016Y\256\"\354T\377D\025\2122\000T\270u\335"
}
tx_response {
  height: 55415549
  txhash: "8637CAFFFA72BB20F83066C19CD547C4BBDEB7579169DD540696CB6E8227C19E"
  data: "122E0A2C2F636F736D7761736D2E7761736D2E76312E4D736745786563757465436F6E7472616374526573706F6E7365"
  raw_log: "[{\"msg_index\":0,\"events\":[{\"type\":\"message\",\"attributes\":[{\"key\":\"action\",\"value\":\"/cosmwasm.wasm.v1.MsgExecuteContract\"},{\"key\":\"sender\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"module\",\"value\":\"wasm\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"amount\",\"value\":\"100000000000000inj\"}]},{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"amount\",\"value\":\"100000000000000inj\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"sender\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"amount\",\"value\":\"100000000000000inj\"}]},{\"type\":\"execute\",\"attributes\":[{\"key\":\"_contract_address\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"}]},{\"type\":\"wasm\",\"attributes\":[{\"key\":\"_contract_address\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"action\",\"value\":\"swap\"},{\"key\":\"sender\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"receiver\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"offer_asset\",\"value\":\"inj\"},{\"key\":\"ask_asset\",\"value\":\"factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"},{\"key\":\"offer_amount\",\"value\":\"100000000000000\"},{\"key\":\"return_amount\",\"value\":\"2577544418926\"},{\"key\":\"spread_amount\",\"value\":\"652756179\"},{\"key\":\"commission_amount\",\"value\":\"7755900959\"},{\"key\":\"maker_fee_amount\",\"value\":\"2585041789\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"amount\",\"value\":\"2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"}]},{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"amount\",\"value\":\"2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\"},{\"key\":\"sender\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"amount\",\"value\":\"2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"}]},{\"type\":\"coin_spent\",\"attributes\":[{\"key\":\"spender\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"amount\",\"value\":\"2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"}]},{\"type\":\"coin_received\",\"attributes\":[{\"key\":\"receiver\",\"value\":\"inj1sf4wtl6h5sjlvvl6khz6eecly72fl9kgsnfesv\"},{\"key\":\"amount\",\"value\":\"2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"}]},{\"type\":\"transfer\",\"attributes\":[{\"key\":\"recipient\",\"value\":\"inj1sf4wtl6h5sjlvvl6khz6eecly72fl9kgsnfesv\"},{\"key\":\"sender\",\"value\":\"inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\"},{\"key\":\"amount\",\"value\":\"2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni\"}]}]}]"
  logs {
    events {
      type: "message"
      attributes {
        key: "action"
        value: "/cosmwasm.wasm.v1.MsgExecuteContract"
      }
      attributes {
        key: "sender"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "module"
        value: "wasm"
      }
    }
    events {
      type: "coin_spent"
      attributes {
        key: "spender"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "amount"
        value: "100000000000000inj"
      }
    }
    events {
      type: "coin_received"
      attributes {
        key: "receiver"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "amount"
        value: "100000000000000inj"
      }
    }
    events {
      type: "transfer"
      attributes {
        key: "recipient"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "sender"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "amount"
        value: "100000000000000inj"
      }
    }
    events {
      type: "execute"
      attributes {
        key: "_contract_address"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
    }
    events {
      type: "wasm"
      attributes {
        key: "_contract_address"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "action"
        value: "swap"
      }
      attributes {
        key: "sender"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "receiver"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "offer_asset"
        value: "inj"
      }
      attributes {
        key: "ask_asset"
        value: "factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
      attributes {
        key: "offer_amount"
        value: "100000000000000"
      }
      attributes {
        key: "return_amount"
        value: "2577544418926"
      }
      attributes {
        key: "spread_amount"
        value: "652756179"
      }
      attributes {
        key: "commission_amount"
        value: "7755900959"
      }
      attributes {
        key: "maker_fee_amount"
        value: "2585041789"
      }
    }
    events {
      type: "coin_spent"
      attributes {
        key: "spender"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "amount"
        value: "2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
    }
    events {
      type: "coin_received"
      attributes {
        key: "receiver"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "amount"
        value: "2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
    }
    events {
      type: "transfer"
      attributes {
        key: "recipient"
        value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      }
      attributes {
        key: "sender"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "amount"
        value: "2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
    }
    events {
      type: "coin_spent"
      attributes {
        key: "spender"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "amount"
        value: "2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
    }
    events {
      type: "coin_received"
      attributes {
        key: "receiver"
        value: "inj1sf4wtl6h5sjlvvl6khz6eecly72fl9kgsnfesv"
      }
      attributes {
        key: "amount"
        value: "2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
    }
    events {
      type: "transfer"
      attributes {
        key: "recipient"
        value: "inj1sf4wtl6h5sjlvvl6khz6eecly72fl9kgsnfesv"
      }
      attributes {
        key: "sender"
        value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      }
      attributes {
        key: "amount"
        value: "2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      }
    }
  }
  gas_wanted: 294027
  gas_used: 283255
  tx {
    type_url: "/cosmos.tx.v1beta1.Tx"
    value: "\n\200\002\n\370\001\n$/cosmwasm.wasm.v1.MsgExecuteContract\022\317\001\n*inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5\022*inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae\032]{\"swap\":{\"offer_asset\":{\"info\":{\"native_token\":{\"denom\":\"inj\"}},\"amount\":\"100000000000000\"}}}*\026\n\003inj\022\017100000000000000\030\231\246\266\032\022~\n^\nT\n-/injective.crypto.v1beta1.ethsecp256k1.PubKey\022#\n!\003H\260\265\211-\025V\0343]\326\222\334\017\304\331\260\356\231\332\272kE\273\265\305\361O}\201\371\207\022\004\n\002\010\001\030I\022\034\n\026\n\003inj\022\017147013500000000\020\213\371\021\032@&\016\230wya\335\037,\032\205>mP\335\003B\357\303\250{_-\326\361\251a8\364\270\343\342t\332/\200\327wb\311\236L\226)\247\003\023\226\016Y\256\"\354T\377D\025\2122\000T\270u\335" 
  }
  timestamp: "2023-12-25T13:18:51Z"
  events {
    type: "coin_spent"
    attributes {
      key: "spender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "amount"
      value: "147013500000000inj"
      index: true
    }
  }
  events {
    type: "coin_received"
    attributes {
      key: "receiver"
      value: "inj17xpfvakm2amg962yls6f84z3kell8c5l6s5ye9"
      index: true
    }
    attributes {
      key: "amount"
      value: "147013500000000inj"
      index: true
    }
  }
  events {
    type: "transfer"
    attributes {
      key: "recipient"
      value: "inj17xpfvakm2amg962yls6f84z3kell8c5l6s5ye9"
      index: true
    }
    attributes {
      key: "sender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "amount"
      value: "147013500000000inj"
      index: true
    }
  }
  events {
    type: "message"
    attributes {
      key: "sender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
  }
  events {
    type: "tx"
    attributes {
      key: "fee"
      value: "147013500000000inj"
      index: true
    }
    attributes {
      key: "fee_payer"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
  }
  events {
    type: "tx"
    attributes {
      key: "acc_seq"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5/73"
      index: true
    }
  }
  events {
    type: "tx"
    attributes {
      key: "signature"
      value: "Jg6Yd3lh3R8sGoU+bVDdA0Lvw6h7Xy3W8alhOPS44+J02i+A13diyZ5MlimnAxOWDlmuIuxU/0QVijIAVLh13Q=="
      index: true
    }
  }
  events {
    type: "message"
    attributes {
      key: "action"
      value: "/cosmwasm.wasm.v1.MsgExecuteContract"
      index: true
    }
    attributes {
      key: "sender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "module"
      value: "wasm"
      index: true
    }
  }
  events {
    type: "coin_spent"
    attributes {
      key: "spender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "amount"
      value: "100000000000000inj"
      index: true
    }
  }
  events {
    type: "coin_received"
    attributes {
      key: "receiver"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "amount"
      value: "100000000000000inj"
      index: true
    }
  }
  events {
    type: "transfer"
    attributes {
      key: "recipient"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "sender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "amount"
      value: "100000000000000inj"
      index: true
    }
  }
  events {
    type: "execute"
    attributes {
      key: "_contract_address"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
  }
  events {
    type: "wasm"
    attributes {
      key: "_contract_address"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "action"
      value: "swap"
      index: true
    }
    attributes {
      key: "sender"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "receiver"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "offer_asset"
      value: "inj"
      index: true
    }
    attributes {
      key: "ask_asset"
      value: "factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
    attributes {
      key: "offer_amount"
      value: "100000000000000"
      index: true
    }
    attributes {
      key: "return_amount"
      value: "2577544418926"
      index: true
    }
    attributes {
      key: "spread_amount"
      value: "652756179"
      index: true
    }
    attributes {
      key: "commission_amount"
      value: "7755900959"
      index: true
    }
    attributes {
      key: "maker_fee_amount"
      value: "2585041789"
      index: true
    }
  }
  events {
    type: "coin_spent"
    attributes {
      key: "spender"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "amount"
      value: "2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
  }
  events {
    type: "coin_received"
    attributes {
      key: "receiver"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "amount"
      value: "2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
  }
  events {
    type: "transfer"
    attributes {
      key: "recipient"
      value: "inj1jx7r5vjr7ykdg4weseluq7ta90emw02jyz5mt5"
      index: true
    }
    attributes {
      key: "sender"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "amount"
      value: "2577544418926factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
  }
  events {
    type: "coin_spent"
    attributes {
      key: "spender"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "amount"
      value: "2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
  }
  events {
    type: "coin_received"
    attributes {
      key: "receiver"
      value: "inj1sf4wtl6h5sjlvvl6khz6eecly72fl9kgsnfesv"
      index: true
    }
    attributes {
      key: "amount"
      value: "2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
  }
  events {
    type: "transfer"
    attributes {
      key: "recipient"
      value: "inj1sf4wtl6h5sjlvvl6khz6eecly72fl9kgsnfesv"
      index: true
    }
    attributes {
      key: "sender"
      value: "inj1m9f38mzmrcmz63nrhgw4v7qj0puceep76qfzae"
      index: true
    }
    attributes {
      key: "amount"
      value: "2585041789factory/inj1kzaaapa8ux4z4lh8stm6vv9c5ykhtwl84zxrtl/ni"
      index: true
    }
  }
}


data = json.loads(json_data)

# Accède à la valeur que tu recherches
return_amount = data["tx_response"]["logs"][0]["events"][0]["attributes"][0]["value"]

print("Return Amount:", return_amount)