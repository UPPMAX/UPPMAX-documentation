# Running ollama on Pelle

## Summary
- Ollama needs to be installed in the project folder.
- The location of the ollama models needs to be redirected in to a folder within the project `export OLLAMA_MODELS=/proj/naiss-XXXXX/...`.
- `ollama serve` must run on an allocated GPU or CPU node.
- Interaction with your `ollama serve` could be done
    -  on the allocated node itself
    -  on the login node
    -  on your own computer
- Running non-interactive tasks

## User installation of ollama

1. Login to Pelle and select a folder under your project allocation
```bash
ssh userid@pelle.uppmax.uu.se
...
cd /proj/naiss-XXXXX/userid/nobackup
```
2. Download `ollama`
```bash
wget https://ollama.com/download/ollama-linux-amd64.tar.zst
```

3. Make folder where you will unpack 
```bash
mkdir ollama && cd ollama
tar -xvf ../ollama-linux-amd64.tar.zst
```
Your `ollama` binary is in `/proj/naiss-XXXXX/userid/nobackup/bin/ollama`

## Running ollama on a compute node

1. Start interactive node with GPU
https://docs.uppmax.uu.se/cluster_guides/slurm_on_pelle/
```bash
interactive -A nais-XXXXX -p gpu -t 1:00:00 --gpus=l40s:1

# or on the old haswell nodes
interactive -A naiss-XXXXX -p haswell -c 16 -t 1:00:00 --gpus=t4:1
```
```
# exampe output from running the last command
salloc: Pending job allocation 4068884
salloc: job 4068884 queued and waiting for resources
salloc: job 4068884 has been allocated resources
salloc: Granted job allocation 4068884
salloc: Waiting for resource configuration
salloc: Nodes p2033 are ready for job
```
Take a note of the `JOBID 4068884` and the node address: `p2033`

2. Start `ollama serve` in the interactive session
```bash
export OLLAMA_MODELS=/proj/nais-XXXXXX/user/nobackup/ollama_models
mkdir -p $OLLAMA_MODELS

# start ollama serve
unset CUDA_VISIBLE_DEVICES
/proj/naiss-XXXXXX/userid/nobackup/ollama/bin/ollama serve
```
3. Look at the end that ollama dicovered the GPU
```
...
time=2026-03-20T07:58:02.030+01:00 level=INFO source=types.go:42 msg="inference compute" id=GPU-92ada8a8-9cda-effe-830e-0bdfcd3e0a96 filter_id="" library=CUDA compute=7.5 name=CUDA0 description="Tesla T4" libdirs=ollama,cuda_v13 driver=13.1 pci_id=0000:81:00.0 type=discrete total="15.0 GiB" available="14.6 GiB"
time=2026-03-20T07:58:02.030+01:00 level=INFO source=routes.go:1832 msg="vram-based default context" total_vram="15.0 GiB" default_num_ctx=4096
```
4. Find the JOBID of the reservation if you lost track
```bash
# Check the JOBID
squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           4068884   haswell interact   pmitev  R       0:06      1 p2034
```
5. Get additional shell in the same allocation
```bash
srun --x11 --pty --overlap --jobid 4068884 bash
```
This will start bash shell in the same job reservation.
6. Test that you can communicate with the ollama service
```bash
/proj/naiss-XXXXXX/userid/nobackup/ollama/bin/ollama list
NAME                      ID              SIZE      MODIFIED     
qwen2.5-coder:14b         9ec8897f747e    9.0 GB    23 hours ago
gemma3:latest             a2af6cc3eb7f    3.3 GB    36 hours ago
mistral:latest            6577803aa9a0    4.4 GB    37 hours ago
llama3.2-vision:latest    6f2f9757ae97    7.8 GB    37 hours ago
llama4:latest             bf31604e25c2    67 GB     39 hours ago
llama3.2:latest           a80c4f17acd5    2.0 GB    39 hours ago
llama4:scout              bf31604e25c2    67 GB     40 hours ago
```

## Expose `ollama serve` to Pelle login node or personal computer.
Warning: This approach exposes the ollama instance to everyone on Pelle - Use with caution.

1. Start interactive node with GPU as before
https://docs.uppmax.uu.se/cluster_guides/slurm_on_pelle/
```bash
interactive -A nais-XXXXX -p gpu -t 1:00:00 --gpus=l40s:1

# or on the old haswell nodes
interactive -A naiss-XXXXX -p haswell -c 16 -t 1:00:00 --gpus=t4:1
```

2. On the node start `ollama serve` with additional `export OLLAMA_HOST=0.0.0.0`
```bash
export OLLAMA_HOST=0.0.0.0
export OLLAMA_MODELS=/proj/nais-XXXXXX/user/nobackup/ollama_models
mkdir -p $OLLAMA_MODELS

# start ollama serve
unset CUDA_VISIBLE_DEVICES
/proj/naiss-XXXXXX/userid/nobackup/ollama/bin/ollama serve
```

3. On the login node you can, check on which node you got allocation
```bash
squeue --me
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           4068884   haswell interact   pmitev  R       0:06      1 p2034
```
4. Run ollama client on Pelle login node 
```bash
export OLLAMA_HOST=p2034 
# start ollama client
/proj/naiss-XXXXXX/userid/nobackup/ollama/bin/ollama

# check models 
/proj/naiss-XXXXXX/userid/nobackup/ollama/bin/ollama list
```
5. Run on personal computer with `ollama serve` running on Pelle GPU node
To expose `ollama serve` to you personal computer run in a shell
```bash
ssh -L 21434:p2034:11434 userid@pelle.uppmax.uu.se
```
Note that in the example above we select port 21434 on the local computer, to avoid potential conflict with local ollama installations running on your computer. Make sure you change `p2034` to the node with your `ollama serve`.
On your computer, make sure you connect to `localhost:21434` when running ollama.
```bash
export OLLAMA_HOST=localhost:21434
ollama list
```
```
NAME                      ID              SIZE      MODIFIED     
qwen2.5-coder:14b         9ec8897f747e    9.0 GB    23 hours ago
gemma3:latest             a2af6cc3eb7f    3.3 GB    36 hours ago
mistral:latest            6577803aa9a0    4.4 GB    37 hours ago
llama3.2-vision:latest    6f2f9757ae97    7.8 GB    37 hours ago
llama4:latest             bf31604e25c2    67 GB     39 hours ago
llama3.2:latest           a80c4f17acd5    2.0 GB    39 hours ago
llama4:scout              bf31604e25c2    67 GB     40 hours ago
```

## Running non-interactive jobs
Example sbatch `submit.sh` template

```bash
#!/bin/bash -l 
#SBATCH -A naiss-XXXX 
#SBATCH -p gpu --gpus=l40s:1
#SBATCH -t 10:00:00

# Get the first free port within a range
OPORT=$(comm -23 <(seq 21434 21444 | sort) <(ss -tan | awk '{print $4}' | cut -d':' -f2 | sort -u) | head -n 1)
export OLLAMA_HOST=localhost:$OPORT

# start the service
export OLLAMA_MODELS=/proj/nais-XXXXXX/user/nobackup/ollama_models
ollama serve &

# Wait a bit for the service to be ready
sleep 5

# Run! 
ollama list 
# or your python program
source venv/activate.sh
python myprogram.py
```
Submit the job.
```bash
sbatch submit.sh
```