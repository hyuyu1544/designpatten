"""Take preprocessing crawler for example."""
from strategy import Context, Strategy
from TESTCASE import TEST_CASES


class FBItemStrategy(Strategy):
    def execute(self):
        print("---FB---")
        print('Name: {}'.format(self.kwargs['name']))
        print('Channel: {}'.format(self.kwargs['channel']))
        print('Content: {}'.format(self.kwargs['content']))


class IGItemStrategy(Strategy):
    def execute(self):
        print("---IG---")
        print('Name: {}'.format(self.kwargs['name']))
        print('Channel: {}'.format(self.kwargs['channel']))
        print('Content: {}'.format(self.kwargs['content']))


def main(doc):
    for i in doc:
        if i['channel'] == 'FB':
            preprocess = Context(FBItemStrategy(**i))
            preprocess.strategy_execute()
        elif i['channel'] == 'IG':
            preprocess = Context(IGItemStrategy(**i))
            preprocess.strategy_execute()


if __name__ == "__main__":
    main(TEST_CASES)
