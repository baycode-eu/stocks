from app.cli.components.Loader import Loader


class CliView:
    def __init__(self, state):
        self.state = state
        self.loader = Loader()

    def __clear(self):
        print("\033[H\033[J")

    def render(self):
        self.__clear()
        self.loader.step()

        for exchange_rate in self.state["exchange-rate-state"].get_components().values():
            print("[ %s ] Name: %s, Bid: %r, Ask: %r, Owned: %r, Owned Bid: %r" % (
                self.loader.print(),
                exchange_rate.get_asset_code(),
                exchange_rate.get_value_of_base_asset_in_compared_asset_bid(),
                exchange_rate.get_value_of_base_asset_in_compared_asset_ask(),
                exchange_rate.get_amount_of_compared_asset(),
                exchange_rate.get_sum_of_owned(),
            ))

        print("Should update: " + str(self.state["settings"].get_component_by_id("should_update")))
