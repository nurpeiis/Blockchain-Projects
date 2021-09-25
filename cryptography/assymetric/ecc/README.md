# Elliptic Curve Cryptography

## General Background 

One of the main reasons that I am exploring Elliptic curve cryptography is mainly because Ethereum uses Elliptic Curve Digital Signature Algorithm (ECDSA), which in turn uses eliptic curve cryptography in order to offer a Digital Signature [Algorithm](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm). In this case let's give a proper definition for two concepts: 

- [Digital Signature](https://en.wikipedia.org/wiki/Digital_Signature_Algorithm) - The Digital Signature Algorithm (DSA) is a Federal Information Processing Standard for digital signatures, based on the mathematical concept of modular exponentiation and the discrete logarithm problem. 
- [Elliptic Curve Cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) - Elliptic-curve cryptography (ECC) is an approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields. ECC allows smaller keys compared to non-EC cryptography (based on plain Galois fields) to provide equivalent security.

## Historical Background

## Hack history

The elliptic curve discrete logarithm is the hard problem underpinning elliptic curve cryptography. Despite almost three decades of research, mathematicians still haven't found an algorithm to solve this problem that improves upon the naive approach. In other words, unlike with factoring, based on currently understood mathematics there doesn't appear to be a shortcut that is narrowing the gap in a Trapdoor Function based around this problem. This means that for numbers of the same size, solving elliptic curve discrete logarithms is significantly harder than factoring. Since a more computationally intensive hard problem means a stronger cryptographic system, it follows that elliptic curve cryptosystems are harder to break than RSA and Diffie-Hellman.

One point that has been in the news recently is the Dual Elliptic Curve Deterministic Random Bit Generator (Dual_EC_DRBG). This is a random number generator standardized by the National Institute of Standards and Technology (NIST), and promoted by the NSA. Dual_EC_DRBG generates random-looking numbers using the mathematics of elliptic curves. The algorithm itself involves taking points on a curve and repeatedly performing an elliptic curve "dot" operation. After publication it was reported that it could have been designed with a backdoor, meaning that the sequence of numbers returned could be fully predicted by someone with the right secret number. Recently, the company RSA recalled several of their products because this random number generator was set as the default PRNG for their line of security products. Whether or not this random number generator was written with a backdoor or not does not change the strength of the elliptic curve technology itself, but it does raise questions about the standardization process for elliptic curves. As we've written about before, it's also part of the reason that attention should be spent to ensuring that your system is using adequately random numbers. In a future blog post, we will go into how a backdoor could be snuck into the specification of this algorithm.

### ECDSA Drawback

The ECDSA digital signature has a drawback compared to RSA in that it requires a good source of entropy. Without proper randomness, the private key could be revealed. A flaw in the random number generator on Android allowed hackers to find the ECDSA private key used to protect the bitcoin wallets of several people in early 2013. Sony's Playstation implementation of ECDSA had a similar vulnerability. A good source of random numbers is needed on the machine making the signatures. Dual_EC_DRBG is not recommended.


## Algorithm details

In order to understan ECC, first we have to undertand the Math behind Elliptic Curve. 

An elliptic curve is the set of points that satisfy a specific mathematical equation. The equation for an elliptic curve looks something like this:

`y^2 = x^3 + ax + b`

There are other representations of elliptic curves, but technically an `elliptic curve` is the set points satisfying an equation in `two variables` with `degree two` in one of the variables and `three` in the other. An elliptic curve is not just a pretty picture, it also has some properties that make it a good setting for cryptography.

An elliptic curve cryptosystem can be defined by picking a prime number as a maximum, a curve equation and a public point on the curve. A private key is a number priv, and a public key is the public point dotted with itself priv times. 

Computing the private key from the public key in this kind of cryptosystem is called the `elliptic curve discrete logarithm function`. This turns out to be the Trapdoor Function we were looking for.