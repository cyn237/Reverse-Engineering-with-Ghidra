# Quest 5
https://freehackquest.com/en/quest/5

The challenge provided us with two files, an executable called dark and a flag.enc file.

First, we try to run the executable:

![image](https://user-images.githubusercontent.com/72126514/201160752-5fca54e1-0a48-47f1-8759-a89231b82995.png)

The executable gave us a hint on the format of our input, which is an inputfile and an output file.

After opening up Ghidra, we can observe the different functions. FUN 00400715 appears to be our main function, so we will rename it to main.

![image](https://user-images.githubusercontent.com/72126514/201158725-87d8f1eb-b308-46ee-ad5a-63a251fc43be.png)
![image](https://user-images.githubusercontent.com/72126514/201159254-38d6073c-199d-4584-83a7-31752154ffa2.png)

At first glance, this main function seems to be opening/reading files and writing in to another file:

![image](https://user-images.githubusercontent.com/72126514/201159798-0850e0f8-e5ce-46e2-9de2-f022d523218c.png)

After going through the decompiled code and renaming a few variables, we cget a sense of what the executable does:

![image](https://user-images.githubusercontent.com/72126514/201167203-0347fc3d-c5c9-43e4-983a-b19c181051fd.png)

After opening two files, the program encrypts the input file and stores the output into a string. At line 52 we can find how the encryption is done.

Giving a closer look to decompiled code and the assembly code:

![image](https://user-images.githubusercontent.com/72126514/201182849-234146d0-e1f6-4196-82eb-3c6073ab90b2.png)

We can see the encryption is done by swapping bytes in the input file:

***Python representation***

original_index = size_of_chunk * (i + 1) - j - 1

scrambled_index = size_of_chunk * i + j

Input_File[scrambled_index] = i* i ^ j* j ^ swap_byte(Input_File[original_index])

We can write a simple python script to reverse the process:

![image](https://user-images.githubusercontent.com/72126514/201191589-15f36707-22d9-4bf5-ac9b-96c531f652f7.png)

After running the script, we get our decrypted file, which is a pdf containing our flag:

![image](https://user-images.githubusercontent.com/72126514/201191790-36de6e61-7303-422a-b8a5-b43a05a1cb2c.png)


