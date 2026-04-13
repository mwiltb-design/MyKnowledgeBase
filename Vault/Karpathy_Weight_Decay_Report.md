# Karpathy Session Report: Weight Decay and Init Scaling

(From Google Doc: 1WCyfHZq5ka_l0rZgBrM0RcEnUoFEej3PPZTxHWBnNrU)

New findings:
1. Weight decay on embeddings and VEs is a big deal. The baseline has no WD on embeddings or value embeddings. Adding tiny amounts (0.001 for embeddings, 0.001→0.002→0.003 for VEs) stacked for ~0.0028 total improvement. But more is worse — 0.005 VE WD regressed. This was the best discovery of the session.
2. Transformer init scale 0.68x is a sweet spot. Reducing the default init scale gave consistent gains through 0.8x→0.7x→0.68x, but 0.66x and 0.65x both regressed. Narrow optimum.
3. FINAL_LR_FRAC 0.05 helps. Small nonzero floor for learning rate at end of training.
4. lm_head weight decay 0.01 — small targeted WD on the output head helped.
... (rest of the report follows)
... (I will include the rest of the text from the previous getText output)
...
Final config: depth 9, dim 512, batch 262K, SSSSL window, short window 1/8, RoPE base 200K, embedding LR 0.9, unembedding LR 0.005, init scale 0.68x, x0_lambda 0.05, FINAL_LR_FRAC 0.05, warmdown 0.75, VE WD 0.003, embedding WD 0.001, lm_head WD 0.01, muon momentum warmup 200 steps
