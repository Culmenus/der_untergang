import os
from io import open
import re
from datasets import Dataset
from datasets import DatasetDict
from datasets import load_dataset

def getData():
    ccmatrix_path = os.path.relpath('data/de-is.bitextf.tsv')
    tatoeba_path = os.path.relpath('data/de-is_tatoeba.tsv')

    lines = open(ccmatrix_path, encoding='utf-8').\
            read().strip().split('\n')

    lines2 = open(tatoeba_path, encoding='utf-8').\
            read().strip().split('\n')

    tatoebaDict = { 'id': [], 'translation': [] }

    for i in range(len(lines2)):
        lines2[i] = lines2[i].split('\t')
        tatoebaDict['id'].append(i)
        tatoebaDict['translation'].append({ 'de': lines2[i][3], 'is': lines2[i][1]})
        
    ccmatrixDict = { 'id': [], 'translation': [] }

    for i in range(len(lines)):
        lines[i] = lines[i].split('\t')
        ccmatrixDict['id'].append(i)
        ccmatrixDict['translation'].append({ 'de': lines[i][1], 'is': lines[i][2] })

    tatoebaDataset = Dataset.from_dict(tatoebaDict)

    ccmatrixDataset = Dataset.from_dict(ccmatrixDict)

    tatoebaData = DatasetDict({'train': tatoebaDataset})

    ccmatrixData = DatasetDict({'train': ccmatrixDataset})

    return tatoebaData, ccmatrixData

tatoeba, test = getData()

print(test)
print(tatoeba)

dataset_tab = load_dataset('parquet', data_files='../data/tilde_model.parquet')

print(dataset_tab['train'])

print(dataset_tab)

def yeetsofthyphen(dataset):
    dataset['translation'] = {'de': re.sub(r"\xad", "", dataset['translation']['de']), 'is': dataset['translation']['is']}
    return dataset

dataset_tab['train'] = dataset_tab['train'].map(yeetsofthyphen)

print(dataset_tab['train'][100])