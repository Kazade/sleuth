# Sleuth - a Simple mocking library

# USAGE:

#  Watch calls with sleuth.watch
#
#  with sleuth.watch("some.path.to.thing") as mock:
#      thing(1, a=2)
#      self.assertTrue(mock.called)
#      self.assertEqual(1, mock.call_count)
#      self.assertEqual([((1,), {a:2})], mock.calls)
#
#  Replace functions with sleuth.switch...
#
#  with sleuth.switch("some.path.to.thing", lambda x: pass) as mock:
#

def _dot_lookup(thing, comp, import_path):
    try:
        return getattr(thing, comp)
    except AttributeError:
        __import__(import_path)
        return getattr(thing, comp)


def _evaluate_path(target):
    components = target.split('.')
    import_path = components.pop(0)
    thing = __import__(import_path)

    for comp in components:
        import_path += ".%s" % comp
        thing = _dot_lookup(thing, comp, import_path)
    return thing

def _patch(path, replacement):
    thing = _evaluate_path(
        ".".join(path.split(".")[:-1])
    )
    setattr(thing, path.split(".")[-1], replacement)

class Watch(object):
    """
        A context manager that is used to watch a function for calls. It essentially decorates
        the function for the lifetime of the context and records all the calls made to it so that
        you can test that everything is as you expect it to be
    """
    def __init__(self, func_path):
        self._original_func = _evaluate_path(func_path)
        self._func_path = func_path

        if not hasattr(self._original_func, "__call__"):
            raise TypeError("Tried to watch something that isn't a callable")

        def wrapper(_func):
            def wrapped(*args, **kwargs):
                wrapped.call_count += 1
                wrapped.calls.append(
                    (args, kwargs)
                )
                wrapped.called = True
                return _func(*args, **kwargs)

            wrapped.call_count = 0
            wrapped.calls = []
            wrapped.called = False

            return wrapped

        self._mock = wrapper(self._original_func)

    def __enter__(self):
        _patch(self._func_path, self._mock)

        return self._mock

    def __exit__(self, *args, **kwargs):
        _patch(self._func_path, self._original_func)

watch = Watch


class Switch(object):
    """
        Replaces a function specified by a path, with the passed callable. The passed in callable is
        wrapped using the above Watch context manager so that you can also assert that your replacement is
        called as you expect.
    """
    def __init__(self, func_path, replacement):
        self._original_func = _evaluate_path(func_path)
        self._func_path = func_path
        self._replacement = replacement
        self._watch = None

    def __enter__(self):
        _patch(self._func_path, self._replacement)
        self._watch = watch(self._func_path)
        return self._watch.__enter__()

    def __exit__(self, *args, **kwargs):
        self._watch.__exit__(*args, **kwargs)
        _patch(self._func_path, self._original_func)

switch = Switch
