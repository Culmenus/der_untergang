import re
from cleaner import getData

tatoebaData, ccmatrixData = getData()

def normalizeString(s):
    s = s.lower().strip()
    s = re.sub(r"([.!?])", r" \1", s)
    s = re.sub(r"[^a-zA-ZÁáÐðÉéÍíÓóÚúÝýÞþÆæÖöÜüÄäß.!?]+", r" ", s)
    return s

def normalizeDataset(dataset):
    pairs = []

    for i in range(len(dataset['train'])):
        german = dataset['train'][i]['translation']['de']
        icelandic = dataset['train'][i]['translation']['is']
        pairs.append([normalizeString(german), normalizeString(icelandic)])
    return pairs

tatoebaPairs = normalizeDataset(tatoebaData)

ccmatrixPairs = normalizeDataset(ccmatrixData)

print(tatoebaPairs[0])
print(tatoebaPairs[1])
print(tatoebaPairs[2])