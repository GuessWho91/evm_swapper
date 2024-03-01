from evm_wallet import Chains
from evm_wallet import Coin
from evm_wallet import Wallet
from evm_wallet import W3Transactor
from evm_wallet import W3Error
from evm_swapper.contracts import SwapperContract


class Swapper(W3Transactor):

    chain: Chains
    wallet: Wallet

    def __init__(self, contract: SwapperContract):
        self.contract = contract
        self.wallet = contract.wallet
        self.chain = contract.wallet.chain

        if not contract.is_chain_available(self.chain):
            raise W3Error(
                f'This chain is not available in this protocol'
            )

    async def swap(self, token_from: Coin, token_to: Coin, amount):

        self.wallet.logger.info(f"[Swapper] [{self.wallet.address}] Start swap {amount} of {token_from.__class__.__name__} to "
                                f"{token_to.__class__.__name__} in {self.chain} by {self.contract.__class__.__name__}")

        token_to_sell = self.wallet.web3.to_checksum_address(token_from.get_address())
        token_to_buy = self.wallet.web3.to_checksum_address(token_to.get_address())

        amount_wei = self.wallet.get_amount_wei(token_to_sell, amount)

        self.check_gas()
        self.approve_token_if_need(token_from, amount_wei, self.contract.router_address)

        txn = self.contract.get_transaction(token_to_sell, token_to_buy, amount_wei)
        tx_hex = await self.wallet.sigh_transaction(txn)

        self.wallet.logger.success(f"[Swapper] [{self.wallet.address}] Transaction send succeed {self.chain.get_scan_url()}{tx_hex}")

        return tx_hex
