# Quest 46: Belgium Bank
source: https://freehackquest.com/en/quest/46

Initial overview:

![image](https://user-images.githubusercontent.com/72126514/200956648-244c0f1f-2173-4d2d-acfe-dd02d747bf9b.png)

Output of the executable:

![image](https://user-images.githubusercontent.com/72126514/200957920-7edcba9f-9151-41c8-9201-6a97bdef2a05.png)

From th output, we know that we need to find a key with format XXXX-XXXX. 
After navigating to the Main function, we see the decompiled code:

![image](https://user-images.githubusercontent.com/72126514/200957481-f83c5959-9a07-4d9f-95e0-eb4938055ec8.png)

After some initialization, notice the comparison that checks the validity of the key on line 31.

Since we need the boolean uVar4 to be TRUE, we can back track to line 27 and see the key check.
We can see that uVar4 will be true if pcVar2 is equal to pcVar3, so this is very likely our key check.

At line 22, pcVar2 is initialized as a string "DEAD-BEEF", and we can tell pcVar3 stores our input string.

![image](https://user-images.githubusercontent.com/72126514/200960222-e208aae3-d2d6-4ae1-9763-febb7c1e6f2e.png)

After verifying, we can see that the key is indeed DEAD-BEEF
