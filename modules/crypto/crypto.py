class CryptoDesk:

    def portfolio(self):
        return {
            "status": "not_connected",
            "message": "Connect a supported data provider."
        }

    def market_request(self, asset: str):
        return {
            "asset": asset,
            "status": "awaiting_market_provider",
        }

    def transaction_status(self):
        return {
            "status": "not_connected"
        }


crypto_desk = CryptoDesk()
