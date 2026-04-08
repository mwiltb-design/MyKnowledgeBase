# Andrej Karpathy's 630-line Python script ran 50 experiments overnight without any human input

(From The New Stack)

On the night of March 7, Andrej Karpathy pushed a 630-line Python script to GitHub and went to sleep. By morning, his agent had run 50 experiments, discovered a better learning rate, and committed the proof to git without a single human instruction in between.
The story making the rounds is about autonomous machine learning (ML) research. But the more important story is about the design pattern underneath it, and the 40-line Markdown file that made the whole thing work.
The patterns in AutoResearch mirror methodology that any laboratory scientist would recognize. A fixed experimental protocol. A single variable under test. An objective measurement criterion. A keep-or-discard decision at the end of each run. A lab notebook that bridges the scientist’s intent and the instrument’s execution. This article extracts the three primitives that make the loop generalizable and shows why the shift from code to structured prose as the human-agent interface is a development worth paying attention to.
What is the Karpathy Loop?
The original problem AutoResearch was built to solve is narrow and specific. Karpathy was pretraining small transformer language models and spending significant research time in a manual loop: Modify a hyperparameter or architectural choice in the training script, run the model for a while, read the validation metric, decide whether the change was worth keeping, and repeat.
The repo automates that loop entirely. The training script is a stripped-down derivative of nanochat, Karpathy’s own minimal LLM training framework, condensed to a single GPU and a single file. The metric it optimises is val_bpb, validation bits per byte, chosen because it is vocabulary-size-independent, allowing the agent to change tokenisation or model architecture between runs and still get a fair comparison.
A typical session runs roughly 12 experiments per hour. An overnight run on a single GPU can cover 80 to 100 experiments, exploring a region of the configuration space that would take a human researcher several working days to traverse manually. That is the concrete problem. The insight worth extracting is that the solution Karpathy reached is not specific to language model pretraining at all.
AutoResearch is built on three primitives, not one.
1. Editable asset. The single file the agent is permitted to modify. Confining the agent here keeps the search space interpretable and every hypothesis reviewable as a diff.
2. Scalar metric. The single number that determines whether a change was an improvement. It must be computable without human judgment and unambiguous about direction.
3. Time-boxed cycle. The fixed duration makes every experiment directly comparable, regardless of what the agent changed.
(rest of the article follows)
... (I will include the rest of the text from the previous getText output)
...
What’s next
For platform engineers and ML practitioners, the patterns in AutoResearch are immediately applicable: The editable asset behaves like a controlled variable in any well-designed experiment, the scalar metric functions like a fitness criterion in any optimisation problem, and the program.md document works like an experimental protocol, as any serious research organization would version-control and review it with the same rigour applied to production code.
What Karpathy demonstrated is that the gap between “running experiments manually” and “having an agent run experiments autonomously” is smaller than most teams assume, and the primary investment required is in document authorship rather than infrastructure.
The next frontier for this pattern is evaluation methodology, applying the loop to domains where the metric itself is the research question rather than a given. Indic language model evaluation is one such domain, where the search space of prompt templates, scoring functions, and benchmark construction choices is vast, and the systematic exploration of that space is precisely the independent evaluation infrastructure that sovereign AI deployments require.
As autonomous experiment loops mature from ML training into evaluation research, the discipline of writing clear, constraining, version-controlled instruction documents will define which teams produce reliable results and which produce confidently optimised noise. Stay tuned.
