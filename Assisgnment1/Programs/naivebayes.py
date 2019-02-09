"""
@author: sundesh raj
UTA_ID : 1001633297
"""
import decimal
import math

mHeightMean = 0.0
mWeightMean = 0.0
mAgeMean = 0.0
mHeightVariance = 0.0
mWeightVariance = 0.0
mAgeVariance = 0.0

wHeightMean = 0.0
wWeightMean = 0.0
wAgeMean = 0.0
wHeightVariance = 0.0
wWeightVariance = 0.0
wAgeVariance = 0.0

#calculate the p(height|man)
def probHeightMale (inputHeight, manMeanHeight, manVarianceHeight):
    top = (-(inputHeight-manMeanHeight)**2)
    bottom = 2*(decimal.Decimal(manVarianceHeight)**2)
    temp = decimal.Decimal(str(math.exp(top/bottom)))
    loc = decimal.Decimal(str(1/math.sqrt(2*decimal.Decimal(str(math.pi))*(manVarianceHeight)**2)))
    return loc*temp
    
#calculate the p(weight|man)
def probWeightMale (inputWeight, manMeanWeight, manVarianceWeight):
    top = (-(inputWeight-manMeanWeight)**2)
    bottom = 2*(decimal.Decimal(manVarianceWeight)**2)
    temp = decimal.Decimal(str(math.exp(top/bottom)))
    loc = decimal.Decimal(str(1/math.sqrt(2*decimal.Decimal(str(math.pi))*(manVarianceWeight)**2)))
    return loc*temp

#calculate the p(age|man)
def probAgeMale (inputAge, manMeanAge, manVarianceAge):
    top = (-(inputAge-manMeanAge)**2)
    bottom = 2*(decimal.Decimal(manVarianceAge)**2)
    temp = decimal.Decimal(str(math.exp(top/bottom)))
    loc = decimal.Decimal(str(1/math.sqrt(2*decimal.Decimal(str(math.pi))*(manVarianceAge)**2)))
    return loc*temp

#calculate the p(height|woman)
def probHeightWoman (inputHeight, wMeanHeight, wVarianceHeight):
    top = (-(inputHeight-wMeanHeight)**2)
    bottom = 2*(decimal.Decimal(wVarianceHeight)**2)
    temp = decimal.Decimal(str(math.exp(top/bottom)))
    loc = decimal.Decimal(str(1/math.sqrt(2*decimal.Decimal(str(math.pi))*(wVarianceHeight)**2)))
    return loc*temp
    
#calculate the p(weight|woman)
def probWeightWoman (inputWeight, wMeanWeight, wVarianceHeight):
    top = (-(inputWeight-wMeanWeight)**2)
    bottom = 2*(decimal.Decimal(wVarianceHeight)**2)
    temp = decimal.Decimal(str(math.exp(top/bottom)))
    loc = decimal.Decimal(str(1/math.sqrt(2*decimal.Decimal(str(math.pi))*(wVarianceHeight)**2)))
    return loc*temp
    
#calculate the p(age|woman)
def probAgeWoman (inputAge, wMeanAge, wVarianceAge):
    top = (-(inputAge-wMeanAge)**2)
    bottom = 2*(decimal.Decimal(wVarianceAge)**2)
    temp = decimal.Decimal(str(math.exp(top/bottom)))
    loc = decimal.Decimal(str(1/math.sqrt(2*decimal.Decimal(str(math.pi))*(wVarianceAge)**2)))
    return loc*temp

if __name__ == '__main__':
    
    height = 155
    weight = 40
    age = 30
    
    #datasets
    heights = [170,192,150,170,175,185,170,155,160,182,175,180,160,170]
    weights = [57,95,45,65,78,90,65,48,55,80,69,80,50,72]
    ages = [32,28,30,29,35,32,28,31,30,30,28,27,31,30]
    genderClass = ['W','M','W','M','M','M','W','W','W','M','W','M','W','M']
    
    pMcount=0
    for i in genderClass:
        if (i == 'M'):
            pMcount += 1
    probMan = pMcount/len(genderClass)#probability of Man
    
    pWcount = 0
    for i in genderClass:
        if (i == 'W'):
            pWcount += 1
    probWoman = pWcount/len(genderClass)#probability of Woman
    
    #height mean with respect to MAN
    hMeanArray = []
    hcount = 0
    for x in heights:
        if genderClass[hcount] == 'M':
            hMeanArray.append(heights[hcount])
        hcount += 1
    
    #weight mean with respect to MAN
    wMeanArray = []
    wcount = 0
    for y in weights:
        if genderClass[wcount] == 'M':
            wMeanArray.append(weights[wcount])
        wcount += 1
        
    #age mean with respect to MAN
    aMeanArray = []
    acount = 0
    for z in ages:
        if genderClass[acount] == 'M':
            aMeanArray.append(ages[acount])
        acount += 1
        
    #height mean with respect to WOMAN
    hwMeanArray = []
    hwCount = 0
    for x in heights:
        if genderClass[hwCount] == 'W':
            hwMeanArray.append(heights[hwCount])
        hwCount += 1
        
    #weight mean with respect to WOMAN
    wwMeanArray = []
    wwCount = 0
    for y in weights:
        if genderClass[wwCount] == 'W':
            wwMeanArray.append(weights[wwCount])
        wwCount += 1
        
    #age mean with respect to WOMAN
    awMeanArray = []
    awCount = 0
    for z in ages:
        if genderClass[awCount] == 'W':
            awMeanArray.append(ages[awCount])
        awCount += 1
        
    #height variance with respect to MAN
    hVarArray = []
    hVarCount = 0
    for x in heights:
        if genderClass[hVarCount] == 'M':
            hVarArray.append(heights[hVarCount])
        hVarCount += 1
        
    #weight variance with respect to MAN
    wVarArray = []
    wVarCount = 0
    for y in weights:
        if genderClass[wVarCount] == 'M':
            wVarArray.append(weights[wVarCount])
        wVarCount += 1
        
    #age variance with respect to MAN
    aVarArray = []
    aVarCount = 0
    for z in ages:
        if  genderClass[aVarCount] == 'M':
            aVarArray.append(ages[aVarCount])
        aVarCount += 1
        
    #height variance with respect to WOMAN
    hwVarArray = []
    hwVarCount = 0
    for x in heights:
        if genderClass[hwVarCount] == 'W':
            hwVarArray.append(heights[hwVarCount])
        hwVarCount += 1
        
    #weight variance with respect to MAN
    wwVarArray = []
    wwVarCount = 0
    for y in weights:
        if genderClass[wwVarCount] == 'W':
            wwVarArray.append(weights[wwVarCount])
        wwVarCount += 1
        
    #age variance with respect to MAN
    awVarArray = []
    awVarCount = 0
    for z in ages:
        if  genderClass[awVarCount] == 'W':
            awVarArray.append(ages[awVarCount])
        awVarCount += 1
        
    #Conditional Probabilities for Man
    mHeightMean = decimal.Decimal(sum(hMeanArray))/len(hMeanArray)
    mWeightMean = decimal.Decimal(sum(wMeanArray))/len(wMeanArray)
    mAgeMean = decimal.Decimal(sum(aMeanArray))/len(aMeanArray)
    mHeightVariance = decimal.Decimal(sum((xi - mHeightMean) ** 2 for xi in hVarArray)/(len(hVarArray)-1))
    mWeightVariance = decimal.Decimal(sum((xi - mWeightMean) ** 2 for xi in wVarArray)/(len(wVarArray)-1))
    mAgeVariance = decimal.Decimal(sum((xi - mAgeMean) ** 2 for xi in aVarArray)/(len(aVarArray)-1))
    
    #Conditional probabilities for Woman
    wHeightMean = decimal.Decimal(sum(hwMeanArray))/len(hwMeanArray)
    wWeightMean = decimal.Decimal(sum(wwMeanArray))/len(wwMeanArray)
    wAgeMean = decimal.Decimal(sum(awMeanArray))/len(awMeanArray)
    wHeightVariance = decimal.Decimal(sum((xi - wHeightMean) ** 2 for xi in hwVarArray)/(len(hwVarArray)-1))
    wWeightVariance = decimal.Decimal(sum((xi - wWeightMean) ** 2 for xi in wwVarArray)/(len(wwVarArray)-1))
    wAgeVariance = decimal.Decimal(sum((xi - wAgeMean) ** 2 for xi in awVarArray)/(len(awVarArray)-1))
    
    #p(height/weight/age|Man)
    resultProbHeightMan = probHeightMale(height, mHeightMean, mHeightVariance)
    resultProbWeightMan = probWeightMale(weight, mWeightMean, mWeightVariance)
    resultProbAgeMan = probAgeMale(age, mAgeMean, mAgeVariance)
    
    #p(height/weight/age|Woman)
    resultProbHeightWoman = probHeightWoman(height, wHeightMean, wHeightVariance)
    resultProbWeightWoman = probWeightWoman(weight, wWeightMean, wWeightVariance)
    resultProbAgeWoman = probAgeWoman(age, wAgeMean, wAgeVariance)
    
    #posterior numberator values for Man and Woman
    numeratorMan = decimal.Decimal(probMan)*resultProbHeightMan*resultProbWeightMan*resultProbAgeMan
    numeratorWoman = decimal.Decimal(probWoman)*resultProbHeightWoman*resultProbWeightWoman*resultProbAgeWoman
    
    #conditional check to determine the predictions
    if (numeratorMan > numeratorMan):
        print('The predicted class for %d, %d, %d = Man' %(height,weight,age))
    else:
        print('The predicted class for %d, %d, %d = Woman' %(height,weight,age))