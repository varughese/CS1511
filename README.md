# CS 1511 Homeworks
`CS 1511: Theory of Computation` with Kirk Pruhs at University of Pittsburgh in Spring 2019. Collection of homeworks done with [@kjustin2](https://github.com/kjustin2). Super hard class. Used the textbook *Computational Complexity: A Modern Approach* by Arora and Barak.

## Topics

#### Historical Results
  - Information and Computation
    - Church-Turing Thesis
    - Undecidable Problems
      - Halting, Diagonlization
  - Quantifying Information
    - Entropy
      - Source Coding Theorem
    - Kolmogorov Complexity
  - Logic, Proofs, Computation
    - Difference between Truth and Provability
    - Provably statements are enumerable
    - A sound and complete axiomization implies provable statements are decidable/computable
    - Godel's Incompleteness Theorems (1930's)

#### P, PH, PSAPCE
  - Time and Space
    - LogSpace, P, PSPACE, ExpTime
    - Undecidable Problems
    - LogSpace in P and PSpace is in ExpTime
    - Time and space hiearchy theorems
    - Machine based complete problems for P, PSpace, EXPTIME
    - Circuit Value Problem is log space complete for P
    - TQBF is polynomial time complete for PSpace
  - PH and Alternation
    - Definition of PH
    - PH in PSPACE 
    - Machine based complete problem for NP
    - Cook-Levin Theorem, SAT is complete for NP
    - NP-completeness of THEOREMS
    
#### Circuits
  - Defintion of P/Poly
  - P subset P/Poly
  - Unary Halting in P/Poly
  - Most functions are not in P/Poly 
  - Karp Lipton

#### Randomization
  - Problems which have easy randomized algorithms but its not so clear how to solve them detetermnistically 
  - Definition of BPP, RP, co-RP, ZPP
  - Why these classes seem to not have complete problems
  - ZPP in BPP
  - BPP in P/Poly
  - BPP in polynomial time hierarchy

#### Interactive Proofs
  - Examples: Uno card color, graph non isomorphism
  - Definitions of AM and IP
  - AM protocol for approximate set size
  - GNI in AM[2] via AM protocol for approximate set size 
  - IP=PSPACE
  - If GI is NP-complete then the polynomial time hierachy collapses

#### Energy
  - Billiard ball circuits
  - Reversable computation and  Landauer's principle
  - Minimum energy computation

#### Quantum Computation
  - Two 1/2 silvered mirror experiment and bomb testing experiment
  - EPR experiment and the parity game
  - No cloning theorem (Skipping this semester as we are running out of time)
  - Quantum teleportation (skipping in lecture and leaving as a (hard) homework problem as we are short of time)
  - Simon's Algorithm
  - Provably secure quantum cyrptography using Quantum Indeterminancy (skipping on the first pass as we are running out of time, we may do it at the end the crypo section if there is time)
  - A brief overview of Shor's algorithm

#### Approximation Algorithms
  - Statement of PCP theorem
  - Hardness of approximation of MAXSAT
  - How to use PCP to prove hardness of approximation by reduction
  - Proof that NP subset PCP(poly, 1)

#### Cryptography
  - One time pad private key
  - Public key cryptography
  - Definition of one-way function
  - Definition of Pseudo-random generators. Equivalent to unpredictable generator.
  - One way functions imply pseudo-random generators which imply private key cryptography with smallish keys 
  - Pseudo-random generators imply derandomization of BPP and BPP subset subexponential time
  - Bit commitment protocol
  - Definition of perfect zero knowledge. Definition of semantic security.
  - Perfect zero knowledge proof of graph isomorphism



### How
I use VSCode with a LaTeX extension called [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop). Any LaTeX editor would work. We used GitHub for collaboration.
