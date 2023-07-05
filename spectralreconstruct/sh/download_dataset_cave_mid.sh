mkdir ../data/MID ../data/MID/complete_ms_data
cd ../data/MID/complete_ms_data

## Multiband Image DB produced by CAVE. 
## https://www.cs.columbia.edu/CAVE/databases/multispectral/
wget https://www.cs.columbia.edu/CAVE/databases/multispectral/zip/complete_ms_data.zip

unzip complete_ms_data.zip
del complete_ms_data.zip

cd ../../../sh