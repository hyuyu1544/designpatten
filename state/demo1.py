"""Take water for example."""
from state import State, Context


class Water(Context):

    def __init__(self):
        super().__init__()
        self.add_state(SolidState('Solid'))
        self.add_state(LiquidState('Liquid'))
        self.add_state(GaseousState('Gaseous'))
        self.set_temperature(25)

    def get_temperature(self):
        return self._get_state_info()

    def set_temperature(self, temperature):
        return self._set_state_info(temperature)

    def rise_temperature(self, temperature):
        return self.set_temperature(self.get_temperature() + temperature)

    def reduce_temperature(self, temperature):
        return self.set_temperature(self.get_temperature() - temperature)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton


@singleton
class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        print("Now is {}˚C, is solid.".format(context._get_state_info()))


@singleton
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info > 0 and state_info < 100

    def behavior(self, context):
        print("Now is {}˚C, is liquid.".format(context._get_state_info()))


@singleton
class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info > 100

    def behavior(self, context):
        print("Now is {}˚C, is gaseous.".format(context._get_state_info()))


water = Water()
water.behavior()
water.set_temperature(101)
water.behavior()
water.rise_temperature(10)
water.behavior()
