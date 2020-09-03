from process import action

class Interpreter(object):
    def __init__(self, database):
        self._database = database
        self._action = action.Action(self._database._hero)