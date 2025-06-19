# Compress guide



Modality | Format Examples | Compression Methods | Linux Tools / Libraries
-- | -- | -- | --
Text | .txt, .csv, .json, .xml | Gzip, Bzip2, Zstandard, Parquet | gzip, bzip2, zstd, pigz, xz, parquet-tools, jq
Image | .jpg, .png, .tiff, .webp | JPEG, PNG, WebP, AVIF, LZW | imagemagick, jpegoptim, optipng, cwebp, vips
Audio | .wav, .mp3, .flac, .ogg | MP3, FLAC, OGG, AAC | ffmpeg, lame, flac, sox, opusenc, audacity
Video | .mp4, .avi, .mkv, .mov | H.264, H.265 (HEVC), VP9, AV1, frame sampling | ffmpeg, HandBrakeCLI, avconv, mkvmerge
Tabular | .csv, .tsv, .parquet, .orc | Parquet, ORC, Snappy, Zstd, Delta Encoding | parquet-tools, csvkit, orc-tools, duckdb, spark-shell
Time-Series | .csv, .hdf5, .parquet | Delta + Zlib, Gorilla, Run-Length, HDF5 | h5py, influx-tools, zstd, lz4, h5repack
Graph | .graphml, .gml, .json, .adj | Adjacency list compression, Sparse matrices (CSR, CSC) | networkx, igraph, snap.py, zlib, np.savez_compressed
Multimodal | Mixed formats (JSONL + JPG + WAV) | TFRecord, WebDataset, ZIP with chunked reads | tar, zip, tfrecord, webdataset, shardwriter, lz4
Geospatial | .shp, .geojson, .tif, .gpkg | GeoTIFF + LZW/DEFLATE, ECW, JPEG2000, TopoJSON | GDAL, ogr2ogr, gdal_translate, mapshaper, qgis, tippecanoe
Genomic | .fasta, .fastq, .bam, .vcf | Gzip, BGZF (Blocked Gzip), CRAM (lossy BAM), BCF | samtools, bcftools, htslib, bgzip, tabix, seqtk
