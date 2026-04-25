A few days ago I decided that I wanted to learn more about the Blockchain. So I started reading various documentations, browsed through GitHub, watched video’s online and finally took the online training at the Microsoft Virtual Academy “[Microsoft Blockchain as a Service](https://mva.microsoft.com/en-us/training-courses/microsoft-blockchain-as-a-service-17104?l=aZrQbG3SD_3206218965)”. I guess this is only the beginning as there is so much more to explore in this field. But today I want to share with you the first steps I took trying to understand how this all works. 

The first thing I needed was a Blockchain where I can play around. When you download the Ethereum Wallet you can access the Main network, the test network or run a local blockchain node, but while I was looking into that, I came across a much easier and (for me as a Blockchain newbie) more comprehensive solution called “Ganache” Ganache is a one click ethereum blockchain which you can use to run tests, execute commands, and inspect state while controlling how the chain operates. 

Ganache is available for Windows, Mac and Linux. I am going to use the Windows version. here. So let’s install it. 

- Goto [http://truffleframework.com/ganache/](http://truffleframework.com/ganache/)
- Download and install the “AppX” package

When starting the Ganache Application , it automatically creates 10 accounts. Each account gets an initial 100 ETH assigned. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image.png)

There is no need to run a miner for generating new blocks, since it has an build in miner. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_3.png)

When we select the Blocks option, we see that the first block has been created. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_4.png)

Since we haven’t executed any transactions on the blockchain yet, the block has no transactions. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_5.png)

Okay, so we now have a local blockchain running that is waiting for some transactions. We could now setup some wallets for the test accounts and transfer ETHs, but since I am on a journey to learn how things actually work, I came across the web3 JavaScript API for Ethereum.

If you haven’t installed Node.js yet, you can download it from here: [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

Next open a command prompt and create a folder like C:\DEV\Web3NodeJS

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_6.png)

Then install the Ethereum JavaScript API with the following command:

npm install [web3@0.20.3](mailto:web3@0.20.3)

(I specified the version, as this is the version where things worked for me). 

Once installed, you should have the following content within the folder. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_7.png)

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_8.png)

Now let’s start Node. Enter ‘Node’ at the command prompt. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_9.png)

then enter the following 2 lines of code:

Web3 = require('web3');

web3 = new Web3(new Web3.providers.HttpProvider([http://localhost:7545](http://localhost:7545)));

Note that the above specified port relates to the local RPC server. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_10.png)

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_11.png)

Now that we have a connection, we can start communicating with our local Blockchain. Let’s start with some simple commands:

at the prompt enter: web3.eth

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_12.png)

to get a list of all the accounts enter. 

web3.eth.accounts

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_13.png)

These should be the same accounts that you see in the Ganache application. Now let’s take a look at the balances of the first 3 accounts. 

web3.eth.getBalance('0x627306090abab3a6e1400e9345bc60c78a8bef57')

web3.eth.getBalance('0xf17f52151ebef6c7334fad080c5704d77216b732')

web3.eth.getBalance('0xc5fdf4076b8f3a5357c5e395ab970b5b54098fef')

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_14.png)

And now we transfer some ETH from one account to another. We send 5 ETH from the 3rd account to the 2nd account. 

web3.eth.sendTransaction({from: '0xC5fdf4076b8F3A5357c5E395ab970B5B54098Fef', to: '0xf17f52151ebef6c7334fad080c5704d77216b732', value: web3.toWei(5, 'ether'), gasLimit: 21000, gasPrice: 20000000000})

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_15.png)

Switch back to the Ganache application and check the account balance. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_16.png)

The next block has been created which includes the transaction. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_17.png)

Now let’s take a look at the transaction itself. 

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_18.png)

1. the transaction ID

2. The sender address 

3. The receiver address

4. the value we transferred = 5

Now let’s switch back to the Node console and enter the following command to retrieve the details for Block 1. 

web3.eth.getBlock(1)

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_19.png)

Now let’s look at the transaction details. Note that I took the transaction ID from the output above. 

web3.eth.getTransaction('0x48296c2076ed3ecdafef03e85ae012025431eee89688de251506546232edf0ce')

![image](https://ftp.verboon.info/wp-content/uploads/be19988bfe7b_1042B/image_20.png)

That’s it for today, I hope you enjoyed the article. I am currently looking at creating contracts within Ethereum, I’ll share my learnings with that anytime soon. 

**Resources**

What is Ethereum?
[http://ethdocs.org/en/latest/introduction/what-is-ethereum.html](http://ethdocs.org/en/latest/introduction/what-is-ethereum.html)

Web3.js
[https://github.com/ethereum/web3.js](https://github.com/ethereum/web3.js)

Ganache
[http://truffleframework.com/ganache/](http://truffleframework.com/ganache/)