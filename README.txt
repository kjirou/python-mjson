=====
mjson
=====

This module is extended "python -mjson.tool".


How to use
----------

Same the original

.. code-block:: bash

   $ echo '{"a":1,"b",2}' | python -mmjson.tool
   {
       "a": 1, 
       "b": 2
   }


Change indents

.. code-block:: bash

   $ echo '{"a":1,"b",2}' | python -mmjson.tool -i 2
   {
     "a": 1, 
     "b": 2
   }

