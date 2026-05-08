# Architecture Comparison Matrices

Generated: 2026-05-02 01:17:55  

Architectures compared: 19


## A2a Matrix

For each cluster in the **row** architecture, the best-matching cluster in the **column** architecture is found via Jaccard similarity. The score is the cluster-size-weighted average of those best matches. Range: 0–1 (1.0 = identical decompositions).

| Architecture \ Architecture | WCA_UEM_thresh20_stop-PRESELECTED_file-True | WCA_UEM_thresh23_stop-PRESELECTED_file-True | WCA_UEM_thresh30_stop-PRESELECTED_file-True | WCA_UEM_thresh50_stop-PRESELECTED_file-True | WCA_UEM_thresh75_stop-PRESELECTED_file-True | WCA_UEM_thresh100_stop-PRESELECTED_file-True | WCA_UEMNM_thresh20_stop-PRESELECTED_file-True | WCA_UEMNM_thresh23_stop-PRESELECTED_file-True | WCA_UEMNM_thresh30_stop-PRESELECTED_file-True | WCA_UEMNM_thresh50_stop-PRESELECTED_file-True | WCA_UEMNM_thresh75_stop-PRESELECTED_file-True | WCA_UEMNM_thresh100_stop-PRESELECTED_file-True | LIMBO_IL_thresh20_stop-PRESELECTED_file-True | LIMBO_IL_thresh23_stop-PRESELECTED_file-True | LIMBO_IL_thresh30_stop-PRESELECTED_file-True | LIMBO_IL_thresh50_stop-PRESELECTED_file-True | LIMBO_IL_thresh75_stop-PRESELECTED_file-True | LIMBO_IL_thresh100_stop-PRESELECTED_file-True | ACDC_hadoop_mapreduce_focused |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WCA_UEM_thresh20_stop-PRESELECTED_file-True | 1.0000 | 0.9947 | 0.9824 | 0.9473 | 0.1283 | 0.0844 | 1.0000 | 0.9947 | 0.9824 | 0.9473 | 0.1301 | 0.0896 | 0.3506 | 0.3506 | 0.2031 | 0.2040 | 0.0864 | 0.0883 | 0.2035 |
| WCA_UEM_thresh23_stop-PRESELECTED_file-True | 0.9895 | 1.0000 | 0.9877 | 0.9525 | 0.1336 | 0.0896 | 0.9895 | 1.0000 | 0.9877 | 0.9525 | 0.1353 | 0.0949 | 0.3436 | 0.3436 | 0.1969 | 0.1979 | 0.0828 | 0.0849 | 0.2036 |
| WCA_UEM_thresh30_stop-PRESELECTED_file-True | 0.9652 | 0.9756 | 1.0000 | 0.9649 | 0.1459 | 0.1019 | 0.9652 | 0.9756 | 1.0000 | 0.9649 | 0.1476 | 0.1072 | 0.3276 | 0.3276 | 0.1828 | 0.1838 | 0.0702 | 0.0723 | 0.2019 |
| WCA_UEM_thresh50_stop-PRESELECTED_file-True | 0.8975 | 0.9075 | 0.9311 | 1.0000 | 0.1810 | 0.1371 | 0.8975 | 0.9075 | 0.9311 | 1.0000 | 0.1828 | 0.1424 | 0.2836 | 0.2836 | 0.1441 | 0.1451 | 0.0631 | 0.0423 | 0.1949 |
| WCA_UEM_thresh75_stop-PRESELECTED_file-True | 0.0822 | 0.0877 | 0.1006 | 0.1374 | 1.0000 | 0.6854 | 0.0822 | 0.0877 | 0.1006 | 0.1374 | 0.5655 | 0.5101 | 0.2377 | 0.2725 | 0.3236 | 0.3585 | 0.3345 | 0.2882 | 0.3231 |
| WCA_UEM_thresh100_stop-PRESELECTED_file-True | 0.0594 | 0.0648 | 0.0774 | 0.1134 | 0.6169 | 1.0000 | 0.0594 | 0.0648 | 0.0774 | 0.1134 | 0.4487 | 0.5742 | 0.2138 | 0.2371 | 0.2891 | 0.3715 | 0.3838 | 0.4039 | 0.2589 |
| WCA_UEMNM_thresh20_stop-PRESELECTED_file-True | 1.0000 | 0.9947 | 0.9824 | 0.9473 | 0.1283 | 0.0844 | 1.0000 | 0.9947 | 0.9824 | 0.9473 | 0.1301 | 0.0896 | 0.3506 | 0.3506 | 0.2031 | 0.2040 | 0.0864 | 0.0883 | 0.2035 |
| WCA_UEMNM_thresh23_stop-PRESELECTED_file-True | 0.9895 | 1.0000 | 0.9877 | 0.9525 | 0.1336 | 0.0896 | 0.9895 | 1.0000 | 0.9877 | 0.9525 | 0.1353 | 0.0949 | 0.3436 | 0.3436 | 0.1969 | 0.1979 | 0.0828 | 0.0849 | 0.2036 |
| WCA_UEMNM_thresh30_stop-PRESELECTED_file-True | 0.9652 | 0.9756 | 1.0000 | 0.9649 | 0.1459 | 0.1019 | 0.9652 | 0.9756 | 1.0000 | 0.9649 | 0.1476 | 0.1072 | 0.3276 | 0.3276 | 0.1828 | 0.1838 | 0.0702 | 0.0723 | 0.2019 |
| WCA_UEMNM_thresh50_stop-PRESELECTED_file-True | 0.8975 | 0.9075 | 0.9311 | 1.0000 | 0.1810 | 0.1371 | 0.8975 | 0.9075 | 0.9311 | 1.0000 | 0.1828 | 0.1424 | 0.2836 | 0.2836 | 0.1441 | 0.1451 | 0.0631 | 0.0423 | 0.1949 |
| WCA_UEMNM_thresh75_stop-PRESELECTED_file-True | 0.0860 | 0.0915 | 0.1044 | 0.1414 | 0.5680 | 0.4888 | 0.0860 | 0.0915 | 0.1044 | 0.1414 | 1.0000 | 0.6960 | 0.2156 | 0.2469 | 0.2999 | 0.3322 | 0.3116 | 0.2852 | 0.3498 |
| WCA_UEMNM_thresh100_stop-PRESELECTED_file-True | 0.0608 | 0.0662 | 0.0788 | 0.1149 | 0.4622 | 0.5643 | 0.0608 | 0.0662 | 0.0788 | 0.1149 | 0.6253 | 1.0000 | 0.2037 | 0.2285 | 0.2846 | 0.3524 | 0.4026 | 0.3995 | 0.2561 |
| LIMBO_IL_thresh20_stop-PRESELECTED_file-True | 0.2206 | 0.2189 | 0.2149 | 0.2038 | 0.2358 | 0.2155 | 0.2206 | 0.2189 | 0.2149 | 0.2038 | 0.2241 | 0.2140 | 1.0000 | 0.8401 | 0.6801 | 0.5835 | 0.4095 | 0.3357 | 0.2663 |
| LIMBO_IL_thresh23_stop-PRESELECTED_file-True | 0.1872 | 0.1853 | 0.1809 | 0.1684 | 0.2696 | 0.2434 | 0.1872 | 0.1853 | 0.1809 | 0.1684 | 0.2575 | 0.2376 | 0.8220 | 1.0000 | 0.7838 | 0.6714 | 0.4745 | 0.3866 | 0.2849 |
| LIMBO_IL_thresh30_stop-PRESELECTED_file-True | 0.0979 | 0.0969 | 0.0945 | 0.0879 | 0.3234 | 0.2915 | 0.0979 | 0.0969 | 0.0945 | 0.0879 | 0.2870 | 0.2805 | 0.5613 | 0.6934 | 1.0000 | 0.7996 | 0.5870 | 0.4675 | 0.2717 |
| LIMBO_IL_thresh50_stop-PRESELECTED_file-True | 0.0790 | 0.0778 | 0.0751 | 0.0675 | 0.3044 | 0.3416 | 0.0790 | 0.0778 | 0.0751 | 0.0675 | 0.2805 | 0.3174 | 0.4621 | 0.5310 | 0.7374 | 1.0000 | 0.7575 | 0.6169 | 0.2637 |
| LIMBO_IL_thresh75_stop-PRESELECTED_file-True | 0.0378 | 0.0374 | 0.0363 | 0.0333 | 0.2656 | 0.3546 | 0.0378 | 0.0374 | 0.0363 | 0.0333 | 0.2532 | 0.3603 | 0.2944 | 0.3518 | 0.4651 | 0.6943 | 1.0000 | 0.7838 | 0.2209 |
| LIMBO_IL_thresh100_stop-PRESELECTED_file-True | 0.0294 | 0.0291 | 0.0279 | 0.0245 | 0.2138 | 0.3427 | 0.0294 | 0.0291 | 0.0279 | 0.0245 | 0.2186 | 0.3473 | 0.2208 | 0.2586 | 0.3486 | 0.5128 | 0.7535 | 1.0000 | 0.1595 |
| ACDC_hadoop_mapreduce_focused | 0.1027 | 0.1027 | 0.1037 | 0.1060 | 0.3612 | 0.3385 | 0.1027 | 0.1027 | 0.1037 | 0.1060 | 0.4107 | 0.3308 | 0.2547 | 0.2845 | 0.3089 | 0.3323 | 0.3161 | 0.2485 | 1.0000 |


## Cvg Matrix

Fraction of entities in the **row** architecture that appear anywhere in the **column** architecture. Range: 0–1 (1.0 = every entity in row is present in column).

| Architecture \ Architecture | WCA_UEM_thresh20_stop-PRESELECTED_file-True | WCA_UEM_thresh23_stop-PRESELECTED_file-True | WCA_UEM_thresh30_stop-PRESELECTED_file-True | WCA_UEM_thresh50_stop-PRESELECTED_file-True | WCA_UEM_thresh75_stop-PRESELECTED_file-True | WCA_UEM_thresh100_stop-PRESELECTED_file-True | WCA_UEMNM_thresh20_stop-PRESELECTED_file-True | WCA_UEMNM_thresh23_stop-PRESELECTED_file-True | WCA_UEMNM_thresh30_stop-PRESELECTED_file-True | WCA_UEMNM_thresh50_stop-PRESELECTED_file-True | WCA_UEMNM_thresh75_stop-PRESELECTED_file-True | WCA_UEMNM_thresh100_stop-PRESELECTED_file-True | LIMBO_IL_thresh20_stop-PRESELECTED_file-True | LIMBO_IL_thresh23_stop-PRESELECTED_file-True | LIMBO_IL_thresh30_stop-PRESELECTED_file-True | LIMBO_IL_thresh50_stop-PRESELECTED_file-True | LIMBO_IL_thresh75_stop-PRESELECTED_file-True | LIMBO_IL_thresh100_stop-PRESELECTED_file-True | ACDC_hadoop_mapreduce_focused |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WCA_UEM_thresh20_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEM_thresh23_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEM_thresh30_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEM_thresh50_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEM_thresh75_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEM_thresh100_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEMNM_thresh20_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEMNM_thresh23_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEMNM_thresh30_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEMNM_thresh50_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEMNM_thresh75_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| WCA_UEMNM_thresh100_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| LIMBO_IL_thresh20_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| LIMBO_IL_thresh23_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| LIMBO_IL_thresh30_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| LIMBO_IL_thresh50_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| LIMBO_IL_thresh75_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| LIMBO_IL_thresh100_stop-PRESELECTED_file-True | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| ACDC_hadoop_mapreduce_focused | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |


---

**A2a**: Architecture-to-Architecture similarity (Jaccard-weighted best match)  

**Cvg**: Coverage — fraction of source entities present in target  

Diagonal is always 1.0 (self-comparison).
