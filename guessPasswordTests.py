# -*- coding: utf-8 -*-
"""
Created on Wed May  1 00:57:18 2019

@author: Faradars-pc2
"""

import datetime
import genetic
import unittest


class GuessPasswordTests(unittest.TestCase):
    geneset =" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    
    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)
    '''    
    def test_I_am_a_python_programmer(self):
        target = "You are an expert python programmer."
        self.guess_password(target)   
      '''  
    def guess_password(self, target):
        
        startTime = datetime.datetime.now()
        
        def fnGetFitness(genes):
            return get_fitness(genes, target)
        
        def fnDisplay(candidate):
            display(candidate, startTime)
            
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness,
                                self.geneset, fnDisplay)
        self.assertEqual(''.join(best.Genes), target)
        
    def test_benchmark(self):
        genetic.Benchmark.run(self.test_I_am_a_python_programmer)
    
def display(candidate, startTime):
    timeD = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(
            ''.join(candidate.Genes),
            candidate.Fitness, str(timeD)))  
    
def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
               if expected == actual)    

if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    