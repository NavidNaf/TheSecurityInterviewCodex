## Interviewer 1 Questions

### What is a buffer overflow?

A buffer overflow happens when a program writes more data into a buffer than it was designed to hold. In C, this is common with fixed-size arrays, and it can overwrite nearby memory, crash the program, or create a security vulnerability.

```c
char name[8];
strcpy(name, "this input is too long");
```

### How can you exploit a buffer overflow vulnerability?

An attacker can exploit a buffer overflow by giving input that is longer than the target buffer. If the overflow reaches important memory, it may overwrite variables, change program behavior, or in more serious cases control execution flow.

### How can you protect against a buffer overflow vulnerability?

You can protect against buffer overflow by checking input length before copying it into a buffer. It also helps to use safer functions like `snprintf`, enable compiler protections like stack canaries, and avoid unsafe memory handling patterns.

- Stack canary: A stack canary is a small guard value placed before control data on the stack to detect if a buffer overflow has overwritten memory.
- Unsafe memory handling: Unsafe memory handling means using memory operations without proper bounds checks, which can cause overflows, crashes, or security bugs.

### What are some unsafe libraries, and what are some safer libraries that help mitigate buffer overflow issues?

Unsafe C functions include `strcpy`, `strcat`, `gets`, and `sprintf` because they do not properly limit how much data gets written. Safer options include `snprintf`, `fgets`, `strncpy`, and `strncat`, but they still need to be used carefully with correct buffer sizes.

### What might happen if there is out-of-bounds access to an array?

Out-of-bounds access means the program reads from or writes to memory outside the array. This can cause crashes, leak sensitive data, corrupt nearby variables, or create a vulnerability that an attacker can abuse.

### What were the vulnerable points in `hpeSourceCode.c`?

The main issue was that `strcpy` copied user input into a fixed-size `username` buffer without checking the length. Since `username` was stored next to `is_admin`, a long input could overflow the buffer and overwrite the admin flag. (Details in the Code itself)

```bash
# 1. Compile the vulnerable code.
gcc hpeSourceCode.c -o hpeSourceCode

# 2. Send more than 16 bytes so username overflows into nearby memory.
./hpeSourceCode $(python3 -c 'print("A" * 16 + "\x01\x00\x00\x00")')

# 3. The first 16 bytes fill username, and the next bytes try to overwrite
#    is_admin with a non-zero value, which can trigger the admin branch.
```

## Interviewer 2 Questions

### What do you understand about cryptography?

Cryptography is the practice of protecting information using mathematical techniques. It is used for confidentiality, integrity, authentication, and non-repudiation in systems like HTTPS, password storage, and secure messaging.

### Define salting and hashing.

Hashing is the process of turning data into a fixed-size value using a one-way function. Salting means adding a unique random value to the input before hashing, usually to make password attacks harder.

### What is the difference between salting and hashing, and why do we use them?

Hashing transforms data into a fixed-size digest, while salting adds randomness before the hash is created. We use both in password storage so that even if two users have the same password, their stored hashes look different.

### When does a hash collision happen?

A hash collision happens when two different inputs produce the same hash output. Good cryptographic hash functions are designed to make collisions extremely hard to find in practice.

### How would you do side-channel analysis to test hash collision?

Side-channel analysis looks at indirect signals like timing, power usage, cache behavior, or memory access patterns while a program runs. For hash collision testing, I would check whether different inputs cause measurable behavior differences, but normally collision testing itself is done through cryptanalysis or large-scale input comparison.

### What is the purpose of the `/etc/shadow` file?

The `/etc/shadow` file stores Linux user password hashes and password aging information. It is readable only by privileged users, which makes it safer than storing password hashes in `/etc/passwd`.
