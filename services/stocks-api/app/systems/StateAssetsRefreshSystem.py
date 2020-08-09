from app.asset_tables.AssetTableResolver import AssetTableResolver
from app.exchange_rates.ExchangeRateUpdater import ExchangeRateUpdater
from app.systems.System import System


class StateAssetsRefreshSystem(System):
    def __init__(
            self,
            exchange_rate_updater: ExchangeRateUpdater,
            table_resolver: AssetTableResolver
    ):
        self.exchange_rate_updater = exchange_rate_updater
        self.table_resolver = table_resolver

    def handle(self, entities):
        for asset in entities["exchange-rate-state"].get_components().values():
            table = self.table_resolver.resolve(asset.get_asset_code())
            new_info = table.get_asset_exchange_info_by_code(asset.get_asset_code())

            if new_info:
                self.exchange_rate_updater.update(
                    asset,
                    *new_info
                )
