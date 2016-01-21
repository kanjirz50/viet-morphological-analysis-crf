# Vietnamese Morphological Anlyzer with CRF

Vietnamese morphological analysis with using CRF

## Requirements
* Python 2
* [CRF++ 0.58](https://taku910.github.io/crfpp/)

## How to make model file

### Get tagged Corpus
* [vnPOS](http://vnlp.net/2009/06/25/corpus-vnpos/)

### Convert format from vnPOS to IOB2 tag format

Corpus is given below format.

```
Tấp_nập//JJ sắm//VB đtdđ//NN đầu//NN năm//NC
...
```

Change format to IOB2 tag format.(Use only I tag and B tag.)

```sh
% cat vnPOS.txt | python ./utils/vnPOS_to_iob2.py > vnPOS.iob2
# Output likes below one.
Tấp		B-JJ
nập		I_JJ 
sắm		B-VB 
đtdđ	B-NN 
đầu		B-NN 
năm		B-NC

...
```

Training with CRF++

```sh
% crf_learn ./crf_template ./vnPOS.iob2 ./vnPOS.crfpp.model
```

"crf_template" is a feature template files.
You can change features.

## Usage

```python
from crfpp import CRF_PP

viet_morph_analyzer = CRF_PP('/path/to/model_file')

sentence = 'Số điện thoại của trường'
result = viet_morph_analyzer.analyze(sentence)
```