from pymonad.operators.maybe import Just, Nothing, Maybe

x = Just(1).maybe(Nothing, lambda x : str(x))
print(x)

x = Nothing.maybe(Nothing, lambda x: str(x))
print(x)


x = Just("John").maybe(Nothing, lambda x: int(x))
print(x)