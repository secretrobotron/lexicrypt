=========
lexicrypt
=========


What it is
==========

Encrypt and decrypt text through images.


Installation
============

sudo pip install -r requirements.txt


Screenshot
==========

.. image:: https://img.skitch.com/20111120-bx4m4tpu9dpemdadyr4a8ppake.jpg


Todo
====

* Save self.char_array to a database, such that: author[char_array[public_key_1, public_key_2, public_key_n]]
* If a visitor's public key matches one in the char_array's list, provide a
  browser notification that this image can be decrypted
* Allow them to decrypt by providing a link to the image
