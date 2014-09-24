sleuth
======

A minimal Python mocking library

# Usage

Watch calls with sleuth.watch

   with sleuth.watch("some.path.to.thing") as mock:
       thing(1, a=2)
       self.assertTrue(mock.called)
       self.assertEqual(1, mock.call_count)
       self.assertEqual([((1,), {a:2})], mock.calls)
 
Replace functions with sleuth.switch...

   with sleuth.switch("some.path.to.thing", lambda x: None) as mock:
       thing(1, a=2)
       self.assertTrue(mock.called)

