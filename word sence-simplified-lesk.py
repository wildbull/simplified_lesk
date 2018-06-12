from nltk.wsd import lesk
from nltk import word_tokenize
sentence='An overabundance of oxygen was produced by the plant in the third week of the study'
sent = word_tokenize(sentence)
print(sent)



print(lesk(sent, 'plant', 'n'))


sentence='The plant is producing far too little to sustain its operation for more than a year'
sent = word_tokenize(sentence)
print(sent)



print(lesk(sent, 'plant', 'n'))


sentence='They deposit money in the bank'
sent = word_tokenize(sentence)
print(sent)



print(lesk(sent, 'bank', 'n'))



sentence='Allahabad is situated on the bank of river Ganga.'
sent = word_tokenize(sentence)
print(sent)



print(lesk(sent, 'bank', 'n'))


sentence1='Allahabad is situated on the bank of river Ganga.'
sentence2='They deposit money in the bank'
sentence3='yes bank has the best interest rates'

sent1=word_tokenize(sentence1)
sent2=word_tokenize(sentence2)
sent3=word_tokenize(sentence3)
def simplified_lesk(word,sent3,sent1,sent2):
    a=lesk(sent1, 'bank', 'n')
    b=lesk(sent2, 'bank', 'n')
    c=lesk(sent3, 'bank', 'n')
    if a==b and b==c:
        best_sence=b
    elif a==b and a==c:
        best_sence=a
    elif b==c and a==c:
        best_sence=c
    max_overlap=0
    count_final=0
    
    for word in sent3:
        count=0
        if word in sent1:
            count=count+1
        if count>count_final:
            max_overlap=1
    
    for word in sent3:
        count=0
        if word in sent2:
            count=count+1
        if count>count_final:
            max_overlap=2
            
    return max_overlap
    
print(simplified_lesk('bank',sent3,sent1,sent2))

print(sense[simplified_lesk('bank',sent3,sent1,sent2)])


