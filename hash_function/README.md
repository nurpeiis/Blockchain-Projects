# Hash Functions

The goal of this sub-directory is to make existant hash function collission resistant

## Showing collisions

In order to test if collisions happen with the  algorithm. I am going to use this [repository's](https://github.com/nathantypanski/sha1-collisions) implementation for collision detection.

## Deep SHA-1 description

I implemented `deep-sha1` hash function, which is a twist on `sha1` algorithm, which can be found in `deep_sha1.py` file. The algorithm is as follows:

1. Input string `input` to get hash
2. Pass `input` into `sha1` function and save to `output`
3. Go through each letter of `input` and do following operations, where `c` is the character of `input`:
   `output = sha1(output+c)`
4. Return `sha1(output+input)`

In this case we concantenate previous hash values with every letter of the input string and then concatenate final hash with initial input to get final hash value.

The python implementation is as follows:

```python
def deep_sha1_hash(s):
    orig_str = s
    s = type_convert(s)
    s = sha1(s).hexdigest().encode('ascii')
    for c in orig_str:
        s = sha1(s+type_convert(c)).hexdigest().encode('ascii')
    return sha1(type_convert(orig_str) + s).hexdigest()[:MAX_LENGTH]
```


## Comparison of Deep SHA-1 vs SHA-1

We can find collision in SHA-1 in 700,000 trials, while with my own improvement of SHA-1 with Deep SHA-1, I have run for more than 20 million trials for more than 5 minutes the script to find collison and I still cannot find collisions.

The output for usual SHA-1 is as follows:

```
Finiding collision in sha1 hash function
Collision found! In 6600639 trials
This is sha1 hash function
a (bytes: b'61') hashes to e65ffc, but rH85 (bytes: b'72483835') also hashes to 812512
```

The output for my Deep SHA-1 algorithm is as follows:

```
Finiding collision in deep sha1 hash function
10 million trials
```

So now collision found in more than 10 million trials.