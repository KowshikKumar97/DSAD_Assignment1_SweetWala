# Custom Errors
class FileEmpty(Exception):
    pass

class NumberOfTestCasesMisMatchWithData(Exception):
    pass

class FirstLineOfATestSetIsIncorrect(Exception):
    pass

class NoOfSweetsToBeSelectedIsGreaterThanOrEqualToTheTotalNoOfSweets(Exception):
    pass

class PriceOfTheSweetsProvidedDoesNotMatchWithTheActualCount(Exception):
    pass

class DeliveryCostOfTheSweetsProvidedDoesNotMatchWithTheActualCount(Exception):
    pass

# Custom Classes
class TestSet():
    def __init__(self, total_no_of_sweets, no_of_sweets_to_select, price_list, delivery_cost_list):
        self.total_no_of_sweets = total_no_of_sweets
        self.no_of_sweets_to_select = no_of_sweets_to_select
        self.price_list = price_list
        self.delivery_cost_list = delivery_cost_list

def getIndexPositions(listOfElements, element):# fetches the index values for the givem element in the list
    indexList = []
    for i in range(len(listOfElements)):
        if listOfElements[i] == element:
            indexList.append(i)
    return indexList

def maxPrice(inputlist): # To get te max price the ownner can get
    total_items = inputlist[0][0] #N value, total number of sweets
    #print(total_items)
    itemsToSelect = inputlist[0][1] # M values, number of ssweets to be selected
    #print(itemsToSelect)
    sweetCost = inputlist[1] # list of sweets
    #print(sweetCost)
    deliveryCost = inputlist[2] #list of delivery cost
    deliveryCostCopy = deliveryCost.copy() #copy the delivery cost list for comparing later
    #print(deliveryCost)      
    deliveryCost.sort(reverse=True) # Sorting the delivery cost in descending order
    #print(deliveryCost)
    #print(deliveryCostCopy)
    uniqueDileveryCost = list( dict.fromkeys(deliveryCost) ) # removing the duplicates from the delivery list
    #print(uniqueDileveryCost)
    tempList = []
    masterCostList = []
    for i in range(0,len(uniqueDileveryCost)):
        q = getIndexPositions(deliveryCostCopy,uniqueDileveryCost[i]) #from uniques duelivery cost we compare the main deliver cost list to see if any value is beeing repeated or not
        #print(b)
        if(len(q) > 1): #if value is repeated we will have number more than 1 , then we compare the corrrespoding sweet value to fetch the one with highest price
            for w in q:
                tempList.append(sweetCost[w])
            masterCostList.append(max(tempList))
            #print(masterCostList)
        else: #if number is not dupicated even then we take corresponding sweet cost and store it
            if i <= itemsToSelect:
                masterCostList.append(sweetCost[q[0]])
                #print(masterCostList)
    
    masterCostListMain = [] #we will be taking he number of elemets which we have to choose
    for i in range(0,itemsToSelect):
        masterCostListMain.append(masterCostList[i])
    #print(masterCostListMain)

    deliveryChargeMain = [] #we will be chooosing the delivery cost of the sweets basedon th items we have to choose
    for i in range(0,itemsToSelect):
        deliveryChargeMain.append(uniqueDileveryCost[i])
    #print(deliveryChargeMain)

    minimumDeliveryCharge = (min(deliveryChargeMain))*itemsToSelect #fetching the minimun delivery charge
    #print(minimumDeliveryCharge)

    totalPrice = (sum(masterCostListMain))+minimumDeliveryCharge #calculatng the toal cost and returning it
    #print(totalPrice)

    return totalPrice
        
    # amax = max(deliveryCost)
    # #print(amax)
    # listo1=[]
    # listo2=[]
    # for i in range(0,itemsToSelect):
    #     a=deliveryCost[i]
    #     listo1.append(a)
    #     i+=1
    # print(listo1)


validInput = True # Flag that will stop the execution of the program, if any validation fails

try:
    file = open("inputPS9.txt", "r") # Reading the Input file
    totalInputs = (file.readlines()) # Reading the valus under input file and assigning it to the variable totalInputs
    #print(TOTAL_INPUTS)

except FileNotFoundError:
    validInput = False
    print('Input File not found. Please ensure that the input file is present.')

except OSError:
    validInput = False
    print('An OS error occured while trying to open the input file. Please retry.')

except Exception as err:
    validInput = False
    print('Some unexpected error occured while trying to open the input file: ', repr(err))

if validInput:
    try: 
        inputFileContents = totalInputs # Reading the contents of the file
        if not inputFileContents: # When the file is empty
                raise FileEmpty

        if validInput:
            #print(inputFileContents)
            noOfTestCases = inputFileContents[0]
            #print('No of Test Cases: ', noOfTestCases)
            inputFileContents.remove(noOfTestCases)
            #print('Elements in the list after removing the test case count', inputFileContents)
            testCasesData = []
            tempList = []
            # Validation for the no.of test cases
            i = 0
            while i < len(inputFileContents):
                if inputFileContents[i] != '\n':
                    tempList.append(inputFileContents[i])
                else: 
                    testCasesData.append(tempList)
                    tempList = []
                i = i + 1
                if (i >= len(inputFileContents)):
                    testCasesData.append(tempList)
            
            try:
                if len(testCasesData) != int(noOfTestCases):
                    raise NumberOfTestCasesMisMatchWithData
                
                #print('testCasesData: ', testCasesData)

                test_sets = []
                # validate whether the value of the selected no. of sweets is less than the total no. of sweets provided
                # validate whether the total no. of sweets and the count of the price and delivery charge match
                i = 0
                while i < len(testCasesData):
                    test_set = testCasesData[i]
                    line_one = test_set[0]
                    total_count_and_wanted_count = line_one.split()
                    total_no_of_sweets = int(total_count_and_wanted_count[0])
                    no_of_sweets_to_be_selected = int(total_count_and_wanted_count[1])
                    price_of_the_sweets = test_set[1].split()
                    delivery_cost_of_the_sweets = test_set[2].split()

                    if len(total_count_and_wanted_count) != 2:
                        raise FirstLineOfATestSetIsIncorrect
                        
                    if no_of_sweets_to_be_selected >= total_no_of_sweets:
                        raise NoOfSweetsToBeSelectedIsGreaterThanOrEqualToTheTotalNoOfSweets
                    
                    if len(price_of_the_sweets) != total_no_of_sweets:
                        raise PriceOfTheSweetsProvidedDoesNotMatchWithTheActualCount
                    
                    if len(delivery_cost_of_the_sweets) != total_no_of_sweets:
                        raise DeliveryCostOfTheSweetsProvidedDoesNotMatchWithTheActualCount

                    # populating the test sets
                    test_set_temp = TestSet(total_no_of_sweets, no_of_sweets_to_be_selected, [float(element) for element in price_of_the_sweets], [float(element) for element in delivery_cost_of_the_sweets])
                    test_sets.append(test_set_temp)
                    i = i + 1

                    i=0
                    inputList = []
                    while i < len(totalInputs): # Reading the values from the file and convertng it to the list of varible in string format
                        a = totalInputs[i].strip().split(' ') # spliting the input format and removin the blank spaces
                        if a == ['']:
                            pass
                        else:
                            inputList.append(a)
                        i+=1
                    #print(input_list)

                    i=0
                    listInt = []
                    while i in range(0,len(inputList)): # Converting the string format to the int format
                        strToInt = [int(x) for x in inputList[i]]
                        listInt.append(strToInt)
                        i+=1
                    #print(list_int)

                    noOfTestCases = listInt[0][0] # No of test cases
                    finalPricesOfAllInputs = []
                    #print(aa)
                    if noOfTestCases > 1:# when more than 1 test case is present
                        #finalPricesOfAllInputs = []
                        removingTheNoOfTestCases = listInt.pop(0)
                        #print(aa)
                        #print(list_int)
                        j=0 
                        t=0
                        while t < noOfTestCases:
                            r = listInt[j:j+3]
                            #print(dd)
                            s = maxPrice(r)
                            finalPricesOfAllInputs.append(s)
                            j+=3
                            t+=1

                    else: # when test case is 1
                        b = listInt[1:4]
                        #print(ab)
                        finalPricesOfAllInputs.append(maxPrice(b))
                    
                    #print( finall_rices_of_all_inputs)
                    fileOutput = open("outputPS9.txt","w+")
                    for jh in range(0,len(finalPricesOfAllInputs)):
                        fileOutput.write(str(finalPricesOfAllInputs[jh]))
                        fileOutput.write('\n')
                        #fileOp.write('\n')

            except NumberOfTestCasesMisMatchWithData:
                validInput = False
                print('Number of test cases specified in the first line is not matching with the data given. Please check the input file and give valid data')
            
            except FirstLineOfATestSetIsIncorrect:
                validInput = False
                print('The First Line of a test set is incorrect. It should contain only two values. Please correct and retry')

            except NoOfSweetsToBeSelectedIsGreaterThanOrEqualToTheTotalNoOfSweets:
                validInput = False
                print('The No. of sweets to be selected is greater than or equal to the total no.of sweets in one or more of the test sets. Please correct them and retry')
            
            except PriceOfTheSweetsProvidedDoesNotMatchWithTheActualCount:
                validInput = False
                print('The No. of values provided for the price of the sweets does not match with the total no. of sweets')
            
            except DeliveryCostOfTheSweetsProvidedDoesNotMatchWithTheActualCount:
                validInput = False
                print('The No. of values provided for the delivery cost of the sweets doesnot match with the total no. of sweets')
            
    except FileEmpty as err:
        validInput = False
        print('Input file is empty. Please check the input file and retry.', repr(err))
    except Exception as err:
        validInput = False
        print('Some unexpected error occured while trying to read the contents of the file. Please retry', repr(err.message))

else:
    print('Execution Terminated due to invalid input file')