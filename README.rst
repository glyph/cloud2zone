Libcloud DNS Zone to BIND zone
==============================

`cloud2zone` is a python module and CLI tool which allow you to export DNS
zones from any `Libcloud`_-supported provider to the BIND zone file format.

Note: The generated BIND zone file doesn't contain ``SOA`` and ``NS``
records. This should work fine if you just want to import this file using a DNS
provider web interface, but if you want to use it with BIND you need to
manually add those records.

Usage
=====

.. code-block:: console

   $ pip install cloud2zone
   $ cloud2zone --provider my_provider \
                --account username \
                --domain my.zone.example.com

If you have not previously authenticated for the provider/username you have
specified, it will then prompt you for an API key, which it will store as
securely as it can using the `Keyring`_ module.

License
-------

Package is distributed under the `Apache 2.0 license`_.

.. _`Libcloud`: https://libcloud.apache.org/
.. _`Apache 2.0 license`: https://www.apache.org/licenses/LICENSE-2.0.html
.. _`Keyring`: https://pypi.org/project/keyring/
