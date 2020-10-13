I have created two different folder which works as two miners. Both miner will run the mining command parallelly. I have printed the timestamp in the toppointer.txt to check which miner mines the block first. To do the fork we need to run the following commands:
	- cd Day_02_Exercise
	- ./miner1/Addtoblockchain.sh ./miner1/input.txt & ./miner2/Addtoblockchain.sh ./miner2/input.txt