import math
import matplotlib.pyplot as plt

class Solution():
    def __init__(self, sol=None, score=None):
        self.sol = sol
        self.score = score

class GeneticAlgo():
    def __init__(self, nb_gen=1, len_pop=10):
        """You need to define 'score', 'gen_sol', 'cross_over', 'mutation' function.
        """
        self.nb_gen = nb_gen
        self.len_pop = len_pop
        self.best_of_each_gen: list[Solution] = []

    def plot_best_each_gen(self, show=True):
        liste_x = [i for i in range(self.nb_gen)]
        liste_y = [sol.score for sol in self.best_of_each_gen]
        plt.plot(liste_x, liste_y, 'o')
        plt.xlabel("generations")
        plt.ylabel("score of best solutions")
        if show:
            plt.show()

    def score(self, x:Solution):
        """Calculate score of solution as solution"""
        pass

    def gen_sol(self) ->Solution:
        """Generate a random solution"""
        pass

    def gen_pop(self) -> list[Solution]:
        """Return a population"""
        return [self.gen_sol() for _ in range(self.len_pop)]
    
    def cross_over(self, x:Solution, y:Solution) -> Solution:
        """Return the cross-overs between x and y"""
        pass

    def mutate(self, x:Solution) -> Solution:
        """Return the mutations of x"""
        pass

    def sort_pop(self, pop:list[Solution]):
        """Sort the pop according to function score"""
        pop.sort(key= lambda x:-x.score)

    def next_pop(self, pop:list[Solution], a, b, c):
        """Build next population based on pop.

            a is the proportion of kept solutions.

            b is the proportion of cross-over.

            c is the proportion of mutation"""
        new_pop = []
        for i in range(int(a * self.len_pop)):
            new_pop.append(pop[i])

        K = int( (1 + math.sqrt(1 + 8*b*self.len_pop)) / 2 )
        for i in range(K):
            for j in range(i+1, K):
                new_pop.append(self.cross_over(pop[i], pop[j]))

        for i in range(int(self.len_pop*c)):
            new_pop.append(self.mutate(pop[i]))

        while(len(new_pop) < self.len_pop):
            new_pop.append(self.gen_sol())

        return new_pop
    
    def fct_during_gen(self, actual_gen, actual_pop):
        print(actual_gen, end=" ")
    
    def algo(self, a=0.3, b=0.3, c= 0.2, gen=1) -> list[list[Solution]]:
        """Compute the genetic algorithm and return last population and the list of best solution at each step.

            a is the proportion of kept solutions.

            b is the proportion of cross-over.

            c is the proportion of mutation.

            gen is the number of generation of which you want to compute function self.fct_during_gen
        """

        self.best_of_each_gen = []
        pop = self.gen_pop()
        for actual_gen in range(self.nb_gen):
            self.sort_pop(pop)
            pop = self.next_pop(pop, a, b, c)
            self.best_of_each_gen.append(pop[0])
            if (actual_gen+1) % gen == 0:
                self.fct_during_gen(actual_gen, pop)
        return pop