from ._anvil_designer import MainTemplate
from ..connection import modal, evmChains, web3, Web3
import anvil


connected_descriptions = {
    True: "Connected",
    False: "No wallet connected. Connect wallet to show accounts and their ETH balances."
}

class Main(MainTemplate):
    def __init__(self, **properties):
        self.reset()
        self.init_components(**properties)

    @property
    def connected(self):
        try:
            return self.provider.isConnected()
        except AttributeError:
            return False

    @property
    def connection_text(self):
        return connected_descriptions[self.connected]

    def button_connect_click(self, **event_args):
        self.provider = modal.connect()
        
        self.account = web3.currentProvider.request({"method": "eth_requestAccounts"})[0]
        self.chain_id_hex = web3.currentProvider.request({"method": "eth_chainId"})
        self.chain_id = int(self.chain_id_hex, 16)
        self.chain_data = evmChains.getChain(self.chain_id)
        self.refresh_data_bindings()

    def button_disconnect_click(self, **event_args):
        modal.clearCachedProvider()
        self.provider = None
        self.refresh_data_bindings()

    def reset(self):
        self.provider = None
        self.account = "0x0000000000000000000000000000000000000000"
        self.chain_id_hex = ""
        self.chain_id = None
        self.chain_data = {"name": ""}