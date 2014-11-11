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
