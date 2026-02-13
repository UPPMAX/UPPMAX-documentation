# UPPMAX as an organisation

UPPMAX is a provider of HPC infrastructure
that is physically located in Uppsala.

???- question "Where can I find an overview of UPPMAX?"

    See [our overview of UPPMAX](uppmax.md).

Here we place UPPMAX within the bigger, national, picture,
starting from the biggest source of money for research in Sweden.

![Vetenskapsrådet logo](./img/vr_logo_128_x_154.png)

[Vetenskapsrådet](https://www.vr.se) ('Science counsel', VR) is biggest funder
of research in Sweden and funds the national HPC infrastructure.

![NAISS logo](./img/naiss_logo_416_x_68.png)

The [National Academic Infrastructure for Supercomputing in Sweden](https://www.naiss.se/) (NAISS) provides such HPC infrastructure: computing power, storage and data services. Applications for these resources starts at
[this NAISS page](https://www.naiss.se//#application-rounds-for-compute-and-storage-resources). These resources are physically located in multiple places in Sweden,
among other Uppsala.

![UPPMAX logo](./img/uppmax_logo.png)

[Uppsala Multidisciplinary Center for Advanced Computational Science](https://www.uppmax.uu.se/) (**UPPMAX = UppMACS**)
provides the HPC infrastructure that is physically located in Uppsala.
Part of this is to provide training and [support](https://www.uppmax.uu.se/support).

```mermaid
flowchart TD
    HPC_Sweden(HPC in Sweden)
    HPC_others(HPC in other cities)
    HPC_Uppsala(HPC in Uppsala)
    NAISS(NAISS)
    UPPMAX(UPPMAX)
    UU(Uppsala University)
    Users(Users)
    VR(Vetenskapsrådet)

    VR --> |money| HPC_Sweden
    HPC_Sweden -->|done by| NAISS
    NAISS --> |money| HPC_others
    NAISS --> |money| HPC_Uppsala
    HPC_Uppsala -->|done by| UPPMAX
    UU -->|money| HPC_Uppsala
    Users -->|apply for HPC|NAISS
```
