# What is Hashing? 🔍

Hashing is the process of converting a password into a fixed-size string, typically represented as a hexadecimal number. Here’s the deal: once a password is hashed, it **cannot be reversed**. That means even if someone steals the hash, they can't figure out the original password. 💥

## Example of a Hashing Algorithm:
For example, using **SHA-256** will take "myPassword" and convert it to something like:
b9f3c2c5cdd1ee515568fa9e4298cd27934e72990a6b7787d8b7392e6da3b18b


🔥 A key feature of hashing: **it’s a one-way function!** You can’t go from the hash back to the original password.

## Why do we need to hash passwords?

If someone gains access to your database, they can see the hashed version of the password. This is a security measure to ensure the original password is not exposed.

