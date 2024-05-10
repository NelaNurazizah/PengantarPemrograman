Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("""
... PRAKTIKUM PENGANTAR PEMROGRAMAN
... Nama        : Nela Nurazizah
... NIM         : 301230029
... Angkatan    : 2023
... """)

PRAKTIKUM PENGANTAR PEMROGRAMAN
Nama    : Nela Nurazizah
NIM             : 301230029
Angkatan        : 2023

>>> print("""
... PRAKTIKUM PENGANTAR PEMROGRAMAN
... Nama        :Nela Nurazizah
... NIM :301230029
... Angkatan    :2023
... """)

PRAKTIKUM PENGANTAR PEMROGRAMAN
Nama    :Nela Nurazizah
NIM     :301230029
Angkatan        :2023

>>> print("""
... PRAKTIKUM PENGANTAR PEMROGRAMAN
... Nama        :Nela Nurazizah
... NIM :301230029
... Angkatan:2023
... """)

PRAKTIKUM PENGANTAR PEMROGRAMAN
Nama    :Nela Nurazizah
NIM     :301230029
Angkatan:2023

>>> a = 10
>>> if a>6:
... print("lulus")
  File "<stdin>", line 2
    print("lulus")
    ^
IndentationError: expected an indented block after 'if' statement on line 1
>>> a = 10
>>> if a>6:
...     print("Lulus")
... else:
...     print("Tidak Lulus")
...
Lulus
>>> a = 4
>>> if a>6:
...     print("Lulus")
... else:
...     print("Tidak Lulus")
...
Tidak Lulus
>>>
