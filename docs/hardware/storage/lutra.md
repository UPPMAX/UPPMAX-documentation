# Lutra

UPPMAX has many [storage systems](../../cluster_guides/uppmax_storage_system.md).
This page describes the Lutra storage system.

Lutra is a custom built storage system running GlusterFS. The system consist of
6 Huawei 5288 V5 servers with a total of 6x38 10TB SATA-drives for a capacity
of 2.2 PB. The usable disk space is 1.8PB. Lutra is meant for "offload" or
archive storage and available for all users at a cost of (at this moment) 500
SEK/TB/year, for a commitment of four years and a minimum 50TB. The design and
filesystem choice makes Lutra very scalable, cost efficient while retaining
moderate read/write performance. Lutra is connected to [Pelle](../../cluster_guides/pelle.md),
[Rackham](../../cluster_guides/rackham.md) and
[Snowy](../../cluster_guides/snowy.md) for
general availability.

If you are interested in this type of storage please
[contact support](../../support.md).
