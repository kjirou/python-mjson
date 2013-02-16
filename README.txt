=====
mjson
=====

This module is extended "python -mjson.tool".


How to use
----------

Same the original

.. code-block:: bash

   $ echo '{"a":1,"b",2}' | mjson
   {
       "a": 1, 
       "b": 2
   }


Change indents

.. code-block:: bash

   $ echo '{"a":1,"b",2}' | mjson -i 2
   {
     "a": 1, 
     "b": 2
   }

