# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:39:11 2019

@author: Faradars-pc2
"""

import random
import statistics
import time
import sys

class Chromosome:
    Genes = None
    Fitness = None
    
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness

def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
        
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

def _mutate(parent, geneSet, get_fitness):
    index = random.randrange(0, len(parent.Genes))
    childGenes = parent.Genes[:]
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate \
        if newGene == childGenes[index] \
        else newGene
    
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness)

def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent) 
    if bestParent.Fitness >= optimalFitness:
        return bestParent
    
    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        
        if bestParent.Fitness >= child.Fitness:
            continue
        display(child)
        if child.Fitness >= optimalFitness:
            return child
        bestParent = child
        

class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{0} {1:3.2f} {2:3.2f}".format( 1+i, 
                      mean, statistics.stdev(timings, mean)
                      if i >1 else 0))
        
        

























