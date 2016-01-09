class NewPythonClass:
    def __init__(self, param1 = 'Hello', param2 = 'World'):
        self.param1 = param1
        self.param2 = param2

    def output_params(self):
        print "%s %s" % (self.param1, self.param2)

NewPythonClass('Hi', 'There').output_params()
NewPythonClass().output_params()
