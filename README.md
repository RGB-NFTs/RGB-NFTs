# RGB NFTs
### RGB NFTs Source Code and proof of work.

[rgbnft.py](https://github.com/RGB-NFTs/RGB-NFTs/blob/main/rgbnft.py "rgbnft.py") is the file that generated the 8192 pictures.

By running rgbnft.py, you will **ALWAYS** get the exact 8192 pictures. 

**This is to prove that I didn't make them manually.**

To get a full blue image, I had to bruteforce the seed which the random library uses.
The program I coded and used is [prob.py](https://github.com/RGB-NFTs/RGB-NFTs/blob/main/prob.py "prob.py").
![](https://raw.githubusercontent.com/RGB-NFTs/RGB-NFTs/main/seed.png)

You might wonder why it took almost 1 hour to do so.

To get a full either red, green or blue image, you will need to get one of the three colors, 16 times in row.

The maths would be:

`(1/3)^16`

**This equals to 1 in 43.046.721**.

This is extremely rare, and that's why there's only 1 ultrarare NFT.

Other than that, the 52 Rare NFTs are the ones that only contain 2 out of 3 colors. 

You can find them [here](https://raw.githubusercontent.com/RGB-NFTs/RGB-NFTs/main/rarenfts.txt)
