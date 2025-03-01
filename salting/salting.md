# What is Salting? 🧂

Salting is the process of adding a **random value** to the password before hashing it. This makes sure that even if two users have the same password, their hashes will be completely different. Without a salt, identical passwords will result in identical hashes, which makes it easier for attackers to break them. 😱

## Example:

- User 1: Password = "Ilikecookies!"
- User 2: Password = "Ilikecookies!"

Without salt, both users will have the same hash. But if we add a salt, like "s3cr3t!@#$", each user will get a different hash, even though their passwords are the same.

## Why is salting important?

Adding a salt prevents attacks like **rainbow tables**, which use precomputed hash values to guess passwords. With salting, attackers would need to calculate hashes for every single password and salt combination, making it much harder to crack.


