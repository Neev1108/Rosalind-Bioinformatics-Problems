#!/usr/bin/env python
# coding: utf-8

# In[12]:


from Bio import SeqIO




"""
For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok
in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k
suffix of s that matches a length k prefix of t as long as s≠t; we demand s≠t
to prevent directed loops in the overlap graph (although directed cycles may be present).

Return: The adjacency list corresponding to O3
You may return edges in any order.

"""


class Graph:
    list_of_nodes = []
    adjacency_list = []
    
    def addNode(self, node):
        self.list_of_nodes.append(node)
        
class Node:
    seq = ''
    kmers = []
    
    
    def __init__(self, name, seq,k):
        self.name = name
        self.seq = seq
        self.kmers = self.findk_Mers(self.seq,k)
        
    def findk_Mers(self,seq,k):
        kmer_arr = []
        seq = self.seq
        for i in range(len(self.seq)-k+1):
            kmer = seq[i:i+k]
            kmer_arr.append(kmer)
        self.kmers = kmer_arr
        
        return kmer_arr
        
            


  


# #### Overlap graphs will retreive the kmers list from each node, and then compare the suffix [:1] of one kmers list to another nodes kmers prefix [:len(kmers_second)-2]

# In[16]:



def overlap_graphs(graph, k) -> list:
    adjacency_list = []
    for node in graph.list_of_nodes:
        kmer_array = node.kmers
        for kmer, second_node in zip(kmer_array[1:], graph.list_of_nodes):
            kmers_second = second_node.kmers
            if kmer in kmers_second[:len(kmers_second)-2] and node.name != second_node and node.seq != second_node.seq and [second_node.name, node.name] not in adjacency_list:
                edge = [node.name, second_node.name]
                adjacency_list.append(edge)
        
    return adjacency_list
    


# In[17]:



