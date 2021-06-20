if __name__ == '__main__':
    # class Shop:
    #     def __init__(self, inputs, costs, delivery_costs):
    #         self.total_items = int(inputs[0])
    #         self.items_to_select = int(inputs[1])
    #         self.costs = list(map(lambda x: float(x), costs))
    #         self.delivery_costs = list(map(lambda x: float(x), delivery_costs))
    #         self.__validate_data(inputs, costs, delivery_costs)
            
    #     def __validate_data(self, inputs, costs, delivery_costs):
    #         if self.total_items != float(inputs[0]) or self.items_to_select != float(inputs[1]):
    #             raise "Total Items passed as float which is invalid, we are performing operation considering int values"
    #         if len(self.costs) + len(self.delivery_costs) != self.total_items * 2:
    #             raise "Invalid cost or delivery cost input"

    def get_index_positions_2(list_of_elems, element):# fetches the index values for the givem element in the list
        index_pos_list = []
        for i in range(len(list_of_elems)):
            if list_of_elems[i] == element:
                index_pos_list.append(i)
        return index_pos_list

    def maxPrice(list1): # To get te max price the ownner can get
        total_items = list1[0][0] #N value, total number of sweets
        #print(total_items)
        items_to_select = list1[0][1] # M values, number of ssweets to be selected
        #print(items_to_select)
        Sweet_Cost = list1[1] # list of sweets
        #print(Sweet_Cost)
        delivery_cost = list1[2] #list of delivery cost
        delivery_cost_copy = delivery_cost.copy() #copy the delivery cost list for comparing later
        #print(delivery_cost)      
        delivery_cost.sort(reverse=True) # Sorting the delivery cost in descending order
        #print(delivery_cost)
        #print(delivery_cost_copy)
        unique_dilevery_cost = list( dict.fromkeys(delivery_cost) ) # removing the duplicates from the delivery list
        #print(unique_dilevery_cost)
        listo3 = []
        master_cost_list = []
        for i in range(0,len(unique_dilevery_cost)):
            b = get_index_positions_2(delivery_cost_copy,unique_dilevery_cost[i]) #from uniques duelivery cost we compare the main deliver cost list to see if any value is beeing repeated or not
            #print(b)
            if(len(b) > 1): #if value is repeated we will have number more than 1 , then we compare the corrrespoding sweet value to fetch the one with highest price
                for j in b:
                    listo3.append(Sweet_Cost[j])
                master_cost_list.append(max(listo3))
                #print(master_cost_list)
            else: #if number is not dupicated even then we take corresponding sweet cost and store it
                if i <= items_to_select:
                    master_cost_list.append(Sweet_Cost[b[0]])
                    #print(master_cost_list)
        
        master_cost_list_main = [] #we will be taking he number of elemets which we have to choose
        for i in range(0,items_to_select):
            master_cost_list_main.append(master_cost_list[i])
        #print(master_cost_list_main)

        deliverycharge_main = [] #we will be chooosing the delivery cost of the sweets basedon th items we have to choose
        for i in range(0,items_to_select):
            deliverycharge_main.append(unique_dilevery_cost[i])
        #print(deliverycharge_main)

        minimum_dlevery_charge = (min(deliverycharge_main))*items_to_select #fetching the minimun delivery charge
        #print(minimum_dlevery_charge)

        total_price = (sum(master_cost_list_main))+minimum_dlevery_charge #calculatng the toal cost and returning it
        #print(total_price)

        return total_price
            
        # amax = max(delivery_cost)
        # #print(amax)
        # listo1=[]
        # listo2=[]
        # for i in range(0,items_to_select):
        #     a=delivery_cost[i]
        #     listo1.append(a)
        #     i+=1
        # print(listo1)

    file = open("inputPS9.txt", "r")
    TOTAL_INPUTS = (file.readlines()) 
    #print(TOTAL_INPUTS)

    i=0
    input_list = []
    while i < len(TOTAL_INPUTS): # Reading the values from the file and convertng it to the list of varible in string format
        a = TOTAL_INPUTS[i].strip().split(' ')
        if a == ['']:
            pass
        else:
            input_list.append(a)
        i+=1
    #print(input_list)

    i=0
    list_int = []
    while i in range(0,len(input_list)): # Converting the string format to the int format
        str_to_int = [int(x) for x in input_list[i]]
        list_int.append(str_to_int)
        i+=1
    #print(list_int)

    aa = list_int[0][0] # No of test cases
    #print(aa)
    if aa > 1:# when more than 1 test case is present
        finall_rices_of_all_inputs = []
        cc = list_int.pop(0)
        #print(aa)
        #print(list_int)
        j=0
        ii=0
        while ii < aa:
            dd = list_int[j:j+3]
            #print(dd)
            ee = maxPrice(dd)
            finall_rices_of_all_inputs.append(ee)
            j+=3
            ii+=1


    else: # when test case is 1
        ab = list_int[1:4]
        #print(ab)
        finall_rices_of_all_inputs = maxPrice(ab)
    
    #print( finall_rices_of_all_inputs)
    fileOp = open("outputPS9.txt","w+")
    for item in (finall_rices_of_all_inputs):
        fileOp.write(str(item))
        fileOp.write('\n')
        #fileOp.write('\n')

    
    
    


