# risk_manager.py

class RiskManager:
    def __init__(self, risk_per_trade=0.02, stop_loss_percentage=0.05):
        self.risk_per_trade = risk_per_trade
        self.stop_loss_percentage = stop_loss_percentage

    def calculate_position_size(self, entry_price, stop_loss_price, total_capital):
        position_size = (self.risk_per_trade * total_capital) / abs(entry_price - stop_loss_price)
        return position_size

    def calculate_stop_loss_price(self, entry_price):
        stop_loss_price = entry_price * (1 - self.stop_loss_percentage)
        return stop_loss_price


