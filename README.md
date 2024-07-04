#The attack can be safely done on Unsecure keys: tested with a known weak key. See Modulus below
N=55089599753625499150129246679078411260946554356961748980861372828434789664694269460953507615455541204658984798121874916511031276020889949113155608279765385693784204971246654484161179832345357692487854383961212865469152326807704510472371156179457167612793412416133943976901478047318514990960333355366785001217
#Check the image file for p, q values


# Simple-Fermat-Factorization-attack-on-RSA
#To find the public Modulus you generated you can follow the below commands
#replace with the needed certificate name

#Modulus should be passed to the fermat_factorization 

─$ openssl rsa -pubin -in pubkey.txt -text -noout
Public-Key: (2048 bit)
Modulus:
    00:87:6a:f4:c1:84:70:eb:f7:fe:c7:11:83:6b:a8:
    1e:d2:0f:23:d1:43:b2:0b:d1:e9:70:ee:3f:d7:e9:
    29:7c:70:32:81:d6:26:f3:cb:35:b4:2c:7d:7a:44:
    2d:bb:0a:d7:33:d2:f0:06:88:8d:d4:91:8e:6c:1d:
    58:7d:d4:c9:34:59:b8:de:cb:6b:ff:6e:59:6e:f2:
    99:86:aa:d2:61:8d:92:ab:68:1e:12:df:1d:ed:c5:
    55:e6:c5:36:4d:92:bb:1c:fb:f6:a1:7b:b2:03:0d:
    3b:72:5a:33:6e:75:d1:0c:3b:a8:c2:f8:7d:00:41:
    90:0c:f4:07:d2:09:a1:f4:02:34:35:e6:44:ff:e9:
    02:b4:dd:c6:54:7a:10:82:40:b8:e0:4b:d7:48:87:
    b7:c0:d4:2e:6b:40:3a:a3:5a:e2:1b:51:3b:d9:05:
    67:4f:a9:e8:6e:49:d2:d6:ce:43:ba:c6:19:f4:3c:
    30:70:f1:06:7d:8d:98:91:83:60:56:9c:6c:e1:11:
    a8:bf:8a:a8:16:f3:ce:82:30:8d:ea:b7:2d:cb:f6:
    93:cd:83:a8:a9:40:ff:37:5e:c0:be:b1:5c:74:3c:
    df:31:28:8e:1e:a0:df:45:35:89:de:48:d5:95:ea:
    fb:10:35:68:62:4e:38:f0:5d:cf:cd:d5:b8:9f:5e:
    4d:f3
Exponent: 65537 (0x10001)

                                                                                                                                                                                                                                                                                            
┌──(kaliboy㉿kali)-[~]
└─$ openssl x509 -in cert.pem -pubkey -noout             
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAh2r0wYRw6/f+xxGDa6ge
0g8j0UOyC9HpcO4/1+kpfHAygdYm88s1tCx9ekQtuwrXM9LwBoiN1JGObB1YfdTJ
NFm43str/25ZbvKZhqrSYY2Sq2geEt8d7cVV5sU2TZK7HPv2oXuyAw07clozbnXR
DDuowvh9AEGQDPQH0gmh9AI0NeZE/+kCtN3GVHoQgkC44EvXSIe3wNQua0A6o1ri
G1E72QVnT6nobknS1s5DusYZ9DwwcPEGfY2YkYNgVpxs4RGov4qoFvPOgjCN6rct
y/aTzYOoqUD/N17AvrFcdDzfMSiOHqDfRTWJ3kjVler7EDVoYk448F3PzdW4n15N
8wIDAQAB
-----END PUBLIC KEY-----

#out to the text file

openssl x509 -in cert.pem -pubkey -noout > pubkey.txt
