# Quest 26
https://freehackquest.com/en/quest/26

Since we got an html file for this problem, we will just inspect it with a browser instead of Ghidra.

![image](https://user-images.githubusercontent.com/72126514/201715848-936082a3-42a9-4ccd-ac0f-f099f4072d4c.png)

We are prompted to enter a code, which we should be able to find embedded in the html code.

![image](https://user-images.githubusercontent.com/72126514/201716206-f52a2ea7-1813-4272-99f0-9f3e1aa2fd35.png)

Here in inspect mode, we see the html code calls the function "calculate()" to check the password. We also find the definition of calculate() written as html script.

function calculate(){
  if(document[_0x30b0[2]](_0x30b0[1])[_0x30b0[0]]==_0x30b0[3]){
    document[_0x30b0[2]](_0x30b0[5])[_0x30b0[4]]=_0x30b0[6];} 
  else {
    document[_0x30b0[2]](_0x30b0[5])[_0x30b0[4]]=_0x30b0[7]

In the if else statement, 0x30b0[3] appears to be the key, which is "f9ad44e29cf6c7adf795d7da995ead0d" in text.

![image](https://user-images.githubusercontent.com/72126514/201718381-c13c9700-626d-4753-baf8-d3da5ae4f06c.png)

We obtain the flag: c4cff44b60130184d39fd52c46403cdd

