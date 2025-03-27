# imports

# useful functions
def func_tool(x):
    return x

def func1(obj):
    output = func_tool(obj)
    return output





def MyModel_graph(inputs=(512,512,1),outputs=(512,512,1)):

    ## input

    ## Encoder

    ## Bridge

    ## Decoder

    ## Loss

    model = Model(inputs, outputs)

    return model


def MyModel(inputs=(512,512,1),outputs=(512,512,1)):
    return MyModel_graph(inputs=inputs, outputs=outputs)
