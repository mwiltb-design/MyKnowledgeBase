# Auto-Research

(From DataCamp Tutorial)

Andrej Karpathy's AutoResearch is an open-source tool that runs ML experiments in a loop, keeping only the changes that beat the current best result. You describe research directions in a markdown file, point an AI coding agent at the repo, and walk away. By morning, you have a git history of validated improvements and a log of everything the agent tried.
Released on March 7, 2026, the project picked up 21,000+ GitHub stars and 8.6 million views on Karpathy's announcement within days. This article covers how the three-file architecture works, what the ratchet loop does during those overnight runs, what results AutoResearch has produced so far, and where the approach hits its limits.
What is AutoResearch?
AutoResearch is an open-source Python tool that lets an AI agent run ML experiments on a single GPU without human intervention. It loops through propose-train-evaluate cycles, keeping only changes that improve validation loss. The project ships under an MIT license.
(rest of the tutorial follows)
... (I will include the rest of the text from the previous getText output)
...
Conclusion
Writing a good program.md requires having done the research yourself. You need to know which directions are worth trying, what "better" means for your problem, and when incremental gains have run their course. The agent handles execution, but the judgment behind the research agenda remains human. If the next generation of engineers skips that formative work because agents handle it now, the field will have plenty of compute and no one with the experience to point it in the right direction.
