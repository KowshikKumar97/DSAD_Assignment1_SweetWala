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

    def get_index_positions_2(list_of_elems, element):
        index_pos_list = []
        for i in range(len(list_of_elems)):
            if list_of_elems[i] == element:
                index_pos_list.append(i)
        return index_pos_list

    def maxPrice(list1):
        total_items = list1[0][0]
        #print(total_items)
        items_to_select = list1[0][1]
        #print(items_to_select)
        Sweet_Cost = list1[1]
        #print(Sweet_Cost)
        delivery_cost = list1[2]
        delivery_cost_copy = delivery_cost.copy()
        #print(delivery_cost)      
        delivery_cost.sort(reverse=True)
        #print(delivery_cost)
        #print(delivery_cost_copy)
        unique_dilevery_cost = list( dict.fromkeys(delivery_cost) )
        #print(unique_dilevery_cost)
        listo3 = []
        master_cost_list = []
        for i in range(0,len(unique_dilevery_cost)):
            b = get_index_positions_2(delivery_cost_copy,unique_dilevery_cost[i])
            #print(b)
            if(len(b) > 1):
                for j in b:
                    listo3.append(Sweet_Cost[j])
                master_cost_list.append(max(listo3))
                #print(master_cost_list)
            else:
                if i <= items_to_select:
                    master_cost_list.append(Sweet_Cost[b[0]])
                    #print(master_cost_list)
        
        master_cost_list_main = []
        for i in range(0,items_to_select):
            master_cost_list_main.append(master_cost_list[i])
        #print(master_cost_list_main)

        deliverycharge_main = []
        for i in range(0,items_to_select):
            deliverycharge_main.append(unique_dilevery_cost[i])
        #print(deliverycharge_main)

        minimum_dlevery_charge = (min(deliverycharge_main))*items_to_select
        #print(minimum_dlevery_charge)

        total_price = (sum(master_cost_list_main))+minimum_dlevery_charge
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
    while i < len(TOTAL_INPUTS):
        a = TOTAL_INPUTS[i].strip().split(' ')
        if a == ['']:
            pass
        else:
            input_list.append(a)
        i+=1
    #print(input_list)

    i=0
    list_int = []
    while i in range(0,len(input_list)):
        str_to_int = [int(x) for x in input_list[i]]
        list_int.append(str_to_int)
        i+=1
    #print(list_int)

    aa = list_int[0][0]
    #print(aa)
    if aa > 1:
        pass
    else:
        ab = list_int[1:4]
        #print(ab)
        cc = maxPrice(ab)
    
    print("Total price is:", + cc)
    


