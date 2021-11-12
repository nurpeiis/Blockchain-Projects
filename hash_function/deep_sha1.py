from hashlib import sha1
from binascii import hexlify
from itertools import product
from sys import argv

POSSIBLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAX_LENGTH = 6


def type_convert(s):
    if type(s) is bytes:
        return s
    return s.encode('ascii')


def sha1_hash(s):
    s = type_convert(s)
    return sha1(s).hexdigest()[:MAX_LENGTH]


def deep_sha1_hash(s, depth=2):
    s = type_convert(s)
    orig_str = s
    s = sha1(s).hexdigest().encode('ascii')
    for _ in range(1, depth-1):
        s = sha1(orig_str + s).hexdigest().encode('ascii')
    return sha1(orig_str + s).hexdigest()[:MAX_LENGTH]


def show(orig_str, collision_str, deep_sha1=True, depth=2, num_trials=0):
    ''' Print the original string, the collision string, and then recompute
        the hashes of each of them and print those, to prove that we found
        a collision.
    '''
    # Do the encoding to ascii for bytes output
    orig_ascii = orig_str.encode('ascii')
    collision_ascii = collision_str.encode('ascii')
    if deep_sha1:
        orig_hashed = deep_sha1_hash(orig_ascii, depth)
    else:
        orig_hashed = sha1_hash(orig_ascii)
    if deep_sha1:
        collision_hashed = deep_sha1_hash(collision_ascii, depth)
    else:
        collision_hashed = sha1_hash(collision_ascii)
    # Print stuff.
    print(f'Collision found! In {num_trials} trials')
    if deep_sha1:
        print(f'This is deep sha1 hash function with depth {depth}')
    else:
        print('This is sha1 hash function')

    print(orig_str
          + ' (bytes: ' + str(hexlify(orig_ascii)) + ')'
            + ' hashes to ' + str(orig_hashed)
            + ', but ' + collision_str
            + ' (bytes: ' + str(hexlify(collision_ascii)) + ')'
            + ' also hashes to ' + str(collision_hashed))


def is_collision(trial, orig_hash, deep_sha1=True, depth=2):
    ''' Returns true if the hash of trial is the same as orig_hash.
    '''
    if deep_sha1:
        h = deep_sha1_hash(trial, depth)
    else:
        h = sha1_hash(trial)
    return h == orig_hash


def collide(startnumber, deep_sha1=True, depth=2):
    ''' Search for collisions in the hash. Start with the possible match
        at index startnumber and look for collisions by searching upward
        from there.
        Note that this means if you choose a large value (e.g. 400000) this
        will not look for collisions on possibilities 0 <= x <= 400001, so
        choose a low number unless you want this to run for quite a while.
    '''
    if deep_sha1:
        print(
            f'Finiding collision in deep sha1 hash function with depth {depth}')
    else:
        print('Finiding collision in deep sha1 hash function')
    # Iterator that yields possible characters.
    possible = product(POSSIBLE, repeat=100)

    # Iterate over the product until we reach the specified startnumber
    for i in range(startnumber):
        possible.__next__()

    # This is our collision target
    orig = ''.join([e for e in possible.__next__()]).lstrip('0')

    if deep_sha1:
        orig_hash = deep_sha1_hash(orig, depth)
    else:
        orig_hash = sha1_hash(orig)

    # Iterate over the possible options
    n = 0
    for trial in possible:
        n += 1
        # Convert the tuple from itertools.product into a string
        trial = ''.join([e for e in trial])
        # Strip the leading zeros (who cares about zeros!)
        trial = trial.lstrip('0')
        if n % 10000000 == 0:
            print(f'{n/10000000} trials')
        # Exit if we found a collision
        if is_collision(trial, orig_hash, deep_sha1, depth):
            show(orig, trial, deep_sha1, depth, n)
            break


if __name__ == '__main__':
    #collide(10, False)
    collide(10, True, 2)
    #collide(10, True, 3)
