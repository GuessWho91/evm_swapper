# EVM_Account

Module to swap with EVM web3 wallets

##  Make swap

    from evm_swapper import Swapper
    from evm_swapper import PancakeContract
    from evm_wallet import W3Error
    from evm_wallet import Chains

    try:
        chain = Chains.BSC # Chain to work with
        swapper = Swapper(PancakeContract(wallet))
        swapper.swap(USDT(chain), USDC(chain),  0.01)
    except W3Error as e:
        wallet.logger.error(e.msg)