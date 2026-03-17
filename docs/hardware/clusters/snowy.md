# Snowy hardware

## Snowy's system configuration

Snowy consists of 228 compute servers (nodes) where each compute server
consists of two 8-core Xeon E5-2660 processors running at 2.2 GHz.
We provide 198 nodes with 128 GB memory (`s1-s120`, `s151-s228`),
13 nodes with 256 GB (`s138-s150`) and 17 nodes with 512 GB (`s121-s137`).
All nodes are interconnected with a 2:1
oversubscribed FDR (40 GB/s) InfiniBand fabric.
In total Snowy provides 3548 CPU cores in compute nodes.



Nodes    | CPUs    |  Cores |  Memory     | Scratch    | GPUs | Name | Comment
--------------- | --------------- | --------------- | --------------- |--------------- |--------------- |--------------- |---------------
122 |  2x Xeon E5-2660 2.2 GHz  | 16 (2 x 8)    | 128GB | 3/4TB | N/A | s1-s12, s14-s40, s42-s120, s201-s204| .
49 |  2x Xeon E5-2660 2.2 GHz  | 16 (2 x 8)    | 128GB | 3/4TB | Tesla T4 | s151-s163, s164-s200| .
15 |  2x Xeon E5-2660 2.2 GHz  | 16 (2 x 8)    | 512GB | 3/4TB | N/A | s121-s129, s131, s133-s137 |.
12 |  2x Xeon E5-2660 2.2 GHz  | 16 (2 x 8)    | 256GB | 3/4TB | N/A | s139-s150 | .
1 |  2x Xeon E5-2660 2.2 GHz  | 80 (10 x 8)    | 4TB | 3/4TB | N/A | s229 | .
1 |  2x Xeon E5-2660 2.2 GHz  | 16 (2 x 8)    | 256GB | 3/4TB | Tesla T4 | s138 | .

## CPU

## GPU

## Network

## Storage
