# RSA

## General Background 


## Historical Background

## Hack history

That said, factoring is not the hardest problem on a bit for bit basis. Specialized algorithms like the Quadratic Sieve and the General Number Field Sieve were created to tackle the problem of prime factorization and have been moderately successful. These algorithms are faster and less computationally intensive than the naive approach of just guessing pairs of known primes.

These factoring algorithms get more efficient as the size of the numbers being factored get larger. The gap between the difficulty of factoring large numbers and multiplying large numbers is shrinking as the number (i.e. the key's bit length) gets larger. As the resources available to decrypt numbers increase, the size of the keys need to grow even faster. This is not a sustainable situation for mobile and low-powered devices that have limited computational power. The gap between factoring and multiplying is not sustainable in the long term.

All this means is that RSA is not the ideal system for the future of cryptography. In an ideal Trapdoor Function, the easy way and the hard way get harder at the same rate with respect to the size of the numbers in question. We need a public key system based on a better Trapdoor.

## Algorithm details

Use two prime numbers, `pub, priv` with the max equal to the product of the two numbers, `max = pub*priv`

To encrypt a number you multiply it by itself `pub` times, making sure to wrap around when you hit the `max`. To decrypt a message, you multiply it by itself `priv` times and you get back to the original number. It sounds surprising, but it actually works. This property was a big breakthrough when it was discovered.

## Sources

- [Amazing blog](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)