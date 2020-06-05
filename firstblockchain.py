#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 00:12:08 2020

@author: rogue
"""
import hashlib
import json
class Block():
    def __init__(self, nonce,tstamp,transaction,prevhash=''):
        self.nonce=nonce
        self.tstamp=tstamp
        self.transaction=transaction
        self.prevhash=prevhash
        self.hash=self.calcHash()
    def calcHash(self):
        block_string=json.dumps({"nonce":self.nonce,"tstamp":self.tstamp,"transaction":self.transaction,"prevhash":self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def __str__(self):
        string="nonce: "+str(self.nonce) +"\n"
        string+="tstamp: "+str(self.tstamp) +"\n"
        string+="transaction: "+str(self.transaction)+"\n"
        string+="prevhash: "+str(self.prevhash)+"\n"
        string+="hash: "+str(self.hash)+"\n"
        return string
    
class Blockchain():
    def __init__(self):
        self.chain=[self.generateGenesisBlock(),]
    def generateGenesisBlock(self):
        return Block(0,'01/01/2017','Genisis Block')
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self,newBlock):
        newBlock.prevhash=self.getLastBlock().hash
        newBlock.hash=newBlock.calcHash()
        self.chain.append(newBlock)
    def isChainValid(self):
            for i in range(1,len(self.chain)):
                prevb=self.chain[i-1]
                currb=self.chain[i]
                if(currb.hash != currb.calcHash()):
                    print("invalid block")
                    return False
                if(currb.prevhash != prevb.hash):
                    print("invalid chain")
                    return False
            return True
BCtrade=Blockchain()
BCtrade.addBlock(Block(1,'20/05/2017',100))
BCtrade.addBlock(Block(2,'21/05/2017',20))
BCtrade.chain[1].transaction=333
for b in BCtrade.chain:
    print(b)
print(BCtrade.isChainValid())
