sleuth
======

A minimal Python mocking library

# Why Sleuth?

Most Python projects use mock, which became unittest.mock in Python 3. So why write Sleuth?

Firstly, Sleuth has a different take on mocking than Mock does which can essentially be summarised as "mock functions not objects". Mocking functions is an explicit, readable and predictable thing to do and leads to clean test cases and
loosely-coupled code.

Secondly, Sleuth aims to have a simple and expressive API. With Mock sometimes it's difficult to tell what's going on
and which arguments you need to pass to mock things as you need. Sleuth breaks mocking functions into a set of clearly
defined use cases:

 - watch: You want to see how a function is called, but not change its behaviour.
 - switch: You want to replace a function with another one for testing.
 - detonate: You want to throw an exception when the function is called.
 - fake: You want to replace the function with another one which returns a particular value when called.

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

    with sleuth.detonate("some.path.to.thing", exception=ValueError):
        try:
            thing(1, a=2)
        except ValueError:
            pass

Or...

    with sleuth.detonate("some.path.to.thing", exception=ValueError("Some custom thingy")):
        try:
            thing(1, a=2)
        except ValueError:
            pass

Replace functions with a specific return value with sleuth.fake

    with sleuth.fake("some.path.to.thing", return_value=1) as mock:
        thing(1, a=2)

        self.assertEqual([1], mock.call_returns)
