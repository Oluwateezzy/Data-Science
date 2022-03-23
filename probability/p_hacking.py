from random import random, seed


def run_experiment():
    return [random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):

    num_head = len([flip for flip in experiment if flip])
    return num_head < 469 or num_head > 531

#seed(0)
experiments =  [run_experiment() for _ in range(1000)]
num_rejections = len([experiment for experiment in experiments
                    if reject_fairness(experiment)])

print(num_rejections)
print(run_experiment())