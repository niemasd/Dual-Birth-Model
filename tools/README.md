DESCRIPTIONS
===
* **[DualBirthSimulator.py](DualBirthSimulator.py):** Our implementation of the Dual-Birth generative process
* **[ComputeProb.py](ComputeProb.py):** Computes the probability mass of a given ordered or unordered ranked tree shape under the dual-birth model
* **[estimate-cherries.sh](estimate-cherries.sh):** The Cherry Estimate Correction method we used in our paper
* **[supported-subtrees-min.py](supported-subtrees-min.py):** Alternative Cherry Estimate Correction method (unused)
* **[supported-subtrees-simple-max.py](supported-subtrees-simple-max.py):** Alternative Cherry Estimate Correction method (unused)
* **[supported-subtrees-simple.py](supported-subtrees-simple.py):** Alternative Cherry Estimate Correction method (unused)
* **[supported-subtrees.py](supported-subtrees.py):** Alternative Cherry Estimate Correction method (unused)


Example
===
To sample 20 trees with 6 leaves from the dual-birth process with rates <code>λ<sub>a</sub>=1</code> and <code>λ<sub>b</sub>=2</code>, and to then immediately compute their
probabilities evaluated as unordered trees use:


```
python DualBirthSimulator.py 1 2 6 20 | python ComputeProb.py 1 2 /dev/stdin 1
```