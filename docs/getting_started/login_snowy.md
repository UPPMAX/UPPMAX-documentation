# Login to Snowy

!!! info "Objectives"
    - We'll go through how to reach Snowy

!!! warning
    - If you lack a user account, visit the [Getting started page](https://www.uppmax.uu.se/support/getting-started/course-projects/)

## Local UPPMAX project

## Snowy is availabe as compute nodes

## Login to SNowy

You log in only from Rackham

Two ways:

- Interactive session
- Batch job using Snowy resources


```mermaid
        graph TB

        Node1 -- interactive --> SubGraph2Flow
        Node1 -- sbatch --> SubGraph2Flow
        subgraph "Snowy"
        SubGraph2Flow(calculation nodes) 
        end

        Node1 -- usr-sensXXX + 2FA----> SubGraph1Flow
        subgraph "Bianca"
        SubGraph1Flow(Bianca login) -- usr+passwd --> private(private cluster)
        private -- interactive --> calcB(calculation nodes)
        private -- sbatch --> calcB
        end

        subgraph "Rackham"
        Node1[Login] -- interactive --> Node2[R-calc]
        Node1 -- sbatch --> Node2
        end
```
