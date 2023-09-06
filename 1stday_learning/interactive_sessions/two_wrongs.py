
#%%
class Right(object):
    pass

class Wrong(object):
    def __add__(self, obj):
        if isinstance(obj, Wrong):
            return Right()

#%% 
obj1 = Wrong()
obj2 = Wrong()

# Two Wrongs _can_ make a Right!
obj3 = obj1 + obj2
print(
    "Two {wrong}s can make a {right}!".format(
    wrong=type(obj1),
    right=type(obj3)
    )
)

# %%
