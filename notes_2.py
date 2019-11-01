- Boolean bitwise operations
- Shifing
- Masking

 OR
a = False
b = True

a || b == True

a = 1
b = 0

a | b == 1


AND

a = False
b = True
a && b == False

a = 1
b = 0
a & b == 0

NOT

!True == False
!False == True

~1 == 0
~0 == 1

(Or-ing two bytes together)
    0b11010110
|   0b01011010
    ----------
    0b11011110


XOR  "There can only be one"
a = True
b = True

a XOR b = False

c = False
d = False

a XOR b = False

e = True
d = False

e XOR d = True

1 ^ 0 == 1
1 ^ 1 == 0

    0b01110110
^   0b10110101
--------------
    0b11000011


    0b01100011
      AABCDDDD


    0b10
+   0b11
---------
   0b101


NOR
!(a || b)
~(a | b)

OR
AND
NOT
NOR
XOR
NAND


Shifting

0b 1100 >> 1 shift one to the right
   0110 >> 1 shift everything one place to the right
   0011

   0b01110110 >> 2
     00011101

     00000000

    1100 << 1

    1 1100


0b10000010
number_of_operands = (0b10000010 >> 6)

10100010 >>5
0b101


Masking

  0b 0110
& 0b 0010
---------
     0010

Second Try
  0b 0100
& 0b 0010
----------
     0000



  0b 10110110
& 0b 00001111
-------------
     00000110



  0b 10110110
& 0b 00011100
-------------
     00010100


0b10100010 >> 5

   0b101
&  0b001
--------
   0b001


AABCDDDD

Shift to get AA
Shift and Mask to get C

   0b10100010
&  0b00001111
--------------
   0b00000010
