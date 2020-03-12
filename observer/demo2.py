"""Take stock price for example."""
from TESTCASE import TEST_CASES
from observer import Observable, Observer
import time


class Stock(Observable):
    """Stock price."""

    def __init__(self):
        super().__init__()
        self.message = 11

    def set_message(self, message):
        self.message = message
        self.notify_observer(self.message)

    def get_message(self):
        return self.message


class InvestorA(Observer):
    """When the price lower than 10, I want to buy."""

    def update(self, observable, message):
        if observable.get_message() < 10:
            print("InvestorA buy the stock at {}.".format(observable.message))


class InvestorB(Observer):
    """When the price higher than 12, I want to sell."""

    def update(self, observable, message):
        if observable.get_message() > 12:
            print("InvestorB sell the stock at {}.".format(observable.message))


def main():
    TWIII = Stock()
    Seller = InvestorB()
    Buyer = InvestorA()
    TWIII.add_observer(Seller)
    TWIII.add_observer(Buyer)
    for i in range(len(TEST_CASES['price'])):
        TWIII.set_message(TEST_CASES['price'][i])
        time.sleep(TEST_CASES['time'][i])


if __name__ == "__main__":
    main()
