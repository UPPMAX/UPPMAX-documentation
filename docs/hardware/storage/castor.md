# Castor

Castor is a custom built storage system running GlusterFS dedicated to Bianca.
The system consists of 54 Huawei 5288 V3 servers, each server is equipped with
36 x 3TB SATA disks working as one logical volume (with redundancy) and
providing 109TB raw disk space per one server. This gives about 5,7 PB raw disk
space in total. Each storage server is connected to network with 2 x 40 Gbit/s
Ethernet links working as one aggregated link at 80 Gbit/s.
