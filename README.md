sleuth
======

A minimal Python mocking library

# Usage

Watch calls with sleuth.watch

    with sleuth.watch("some.path.to.thing") as mock:
        result = thing(1, a=2)
        self.assertTrue(mock.called)
        self.assertEqual(1, mock.call_count)
        self.assertEqual([((1,), {a:2})], mock.calls)
        self.assertEqual(result, mock.call_returns[0])

Replace functions with sleuth.switch...

    with sleuth.switch("some.path.to.thing", lambda x: 'something') as mock:
        thing(1, a=2)
        self.assertTrue(mock.called)
        self.assertTrue(['something'], mock.call_returns)


Cause functions to throw exceptions with sleuth.detonate:

    with sleuth.detonate("some.path.to.thing", exception_class=ValueError):
        try:
            thing(1, a=2)
        except ValueError:
            pass

Replace functions with a specific return value with sleuth.fake

    with sleuth.fake("some.path.to.thing", return_value=1) as mock:
        thing(1, a=2)

        self.assertEqual([1], mock.call_returns)
