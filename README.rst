finsky
======

|pypi|

Google Play API

    Still in development. Downloading may not always work.

Install
-------

::

  pip install finsky

Usage
-----

finsky requires authentication parameters, specified in a YAML configuration
file. Your ``profile.yaml`` file might look like

.. code:: yaml

  android_id: 4c2d771066bd23bc
  auth_token: AUGBQrE3ETKnpMtiX6F3Fss-clxmlVJAww9j0L0F2G0bOXLIZN7o2MMNkce15x6g4w8Ca3q2ojRb0ImZardJOUNnJbP_0LKeT1G9ydg41c_pdKb4CkdBsoUd-svTckM-4Rs95HLr-zd7r0sGpa9VFjtavGSihEvUPwIBC5qiiObIsjlCoGgP8j0DOYimRoVUaJvzKFT4aHpxm2GmaNuMZwnUL7DMTPxiPEkCa5qIExZIQQA6--J2s8OzuIrW87goRhBkZ690rs9gMxmjZNjEBVg4Q6SQnMM6XNo5R_ipV1ciYJrMrnX18eETuUHH9vdo-cFRN2ZEJGcOfrFLqB3S6WL8btI0O_byXJXcI_RHyYADnI1_sQBUjV

Then for example, you can download snapchat with

::

  finsky download profile.yaml com.snapchat.android

Note ``com.snapchat.android`` is the app ID you'll see when you `browse to
snapchat on the play store
<https://play.google.com/store/apps/details?id=com.snapchat.android&hl=en>`__.

By default this will download the app to ``com.snapchat.android.apk``. This
can be changed with the ``--out`` option.

Why the name?
-------------

The word ``finsky`` appears a lot in the Google Play APK source code, so I
guessed it has some internal significance.

Acknowledgments
---------------

-  `googleplay-api <https://github.com/egirault/googleplay-api>`__
-  `django-googleplay-api <https://github.com/gotlium/django-googleplay-api>`__
-  `gpsoauth <https://github.com/simon-weber/gpsoauth>`__
-  Dima Kovalenko's `reverse engineering of
   EncryptedPasswd <http://codedigging.com/blog/2014-06-09-about-encryptedpasswd/>`__


.. |pypi| image:: https://img.shields.io/pypi/v/finsky.svg?style=flat-square
   :target: https://pypi.python.org/pypi/finsky
