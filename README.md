# I_before_E_except_after_C
How accurate is the famous rhyme "I before E except after C"? 
This repository seeks to answer that question.


### TL;DR
The rhyme is bullshit. A more accurate rhyme would be "I before E, except when it sounds like "E" as in 'receive'"


### Weighted Results
Weighing the results by word frequency we found that "ie" is almost twice as common as "ei", 
even taking into account cases after "c". 

```
ie vs. ei
65.8% - 34.2%

cie vs. cei
66.7% vs 33.3%
```

### Non-weighted Results
The non-weighted results are even more striking! 
```
ie vs. ei
69.4% - 30.6%

cie vs. cei
81.1% - 18.9%
```



### Explorations
Examples have been extracted and placed in `cei_words.txt` and `cie_words.txt`

### Data Source:
https://github.com/okuchaiev/f-lm/blob/master/1b_word_vocab.txt

### Contribute. 
Have a better corpus/dataset to test the rhyme on? Please create an issue or a merge request!