from anvil.js.window import Web3Modal, WalletConnectProvider, evmChains, web3, Web3

wallet_connect_provider = WalletConnectProvider.default
providers = {
    "walletconnect": {
        "package": wallet_connect_provider,
        "options": {"infuraId": "bd76ba3ce1f844f98ab024ff5e3f0ff0"},
    }
}

options = {
    "network": "mainnet",
    "cacheProvder": True,
    "providerOptions": providers,
}

modal = Web3Modal.default(options)

