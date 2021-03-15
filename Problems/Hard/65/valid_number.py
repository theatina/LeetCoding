class Solution:
    def isNumber(self, s: str) -> bool:
        
        # s = " +12e++1 "

        it_is_decimal = True
        test = s.split(" ")
        test = list(filter(("").__ne__, test))

        if '' in test:
          test.remove('')

        if len(test)==0:
            it_is_decimal = False
            return it_is_decimal

        if len(test)<2:
            test = test[0]
            test = test.replace(" ","")

            if not test.isdecimal():
                # lens = [len(i) for i in test ]
                # # print(lens)
                # test = test [lens.index(max(lens))]
                
                temp_str = test.replace("e","")
                temp_str = temp_str.replace(".","")
                temp_str = temp_str.replace("+","")
                temp_str = temp_str.replace("-","")
                if not temp_str.isdecimal():
                    it_is_decimal = False 
                    return it_is_decimal
                # print(temp_str,test)
                if ("e" in test) and (test.count("e")<2) and (not test.startswith("e")):
                    test_e = test.replace(" ","")
                    test_e = test_e.split("e")

                    if '' in test_e:
                        test_e.remove('')
                    if len(test_e)>1:
                        test_e[1] = test_e[1].replace(" ","")
                        
                        if test_e[1].isdecimal():
                            random = 1
                        elif ( ("-" in test_e[1]) or ("+" in test_e[1]) ) and len(test_e[1])>1:
                            
                            if ("+" in test_e[1]):
                                
                                if (test_e[1].startswith("+")):
                                    # print(it_is_decimal)
                                    if ( test_e[1].count("+") >1):# or ( not test_e[1][1].isdecimal()):
                                        
                                        it_is_decimal = False 
                                        return it_is_decimal
                                else:
                                    it_is_decimal = False 
                                    return it_is_decimal

                            if ("-" in test_e[1]):
        
                                if (test_e[1].startswith("-")):
                                    if ( test_e[1].count("-") >1):

                                        it_is_decimal = False 
                                        return it_is_decimal
                            
                                
                                else:

                                    it_is_decimal = False
                                    return it_is_decimal
                        else:

                            it_is_decimal = False
                            return it_is_decimal

                    else:

                        it_is_decimal = False
                        return it_is_decimal
                elif ("e" in test) and test.count("e")>1:
                    it_is_decimal = False
                    return it_is_decimal
                elif ("e" in test) and test.startswith("e"):
                    it_is_decimal = False
                    return it_is_decimal

                # print(it_is_decimal)
                all_plus_s = [ i for i in range(len(test)) if test[i] is "+" ]
                all_minus_s = [ i for i in range(len(test)) if test[i] is "-" ]
                test_temp = test
                if ("e" not in test) and ( ("-" in test) or ("+" in test) ):
                    
                    if ("+" in test):
                        if (test.startswith("+")):
                            if ( test.count("+") >1):
                                it_is_decimal = False
                                return it_is_decimal
                        else:
                            it_is_decimal = False
                            return it_is_decimal
                    
                    if  ("-" in test): 
                        if (test.startswith("-")):
                            if( test.count("-") >1):

                                it_is_decimal = False
                                return it_is_decimal
                        else:
                            it_is_decimal = False
                            return it_is_decimal

                elif ("e" in test ):

                    
                    test_temp = test.split("e")[0]
                    if ("-" in test_temp) or ("+" in test_temp):
                        if len(test_temp) < 2:
                            it_is_decimal = False
                            return it_is_decimal 
                        
                        
                        if ("+" in test_temp):
                            if (test_temp.startswith("+")):
                                if ( test_temp.count("+") >1):
                                    it_is_decimal = False
                                    return it_is_decimal
                            else:
                                it_is_decimal = False
                                return it_is_decimal
                        
                        if ("-" in test_temp):
                            if (test_temp.startswith("-")):
                                if( test_temp.count("-") >1):

                                    it_is_decimal = False
                                    return it_is_decimal
                            else:
                                it_is_decimal = False
                                return it_is_decimal
                        
                    
                

                # print(test)
    
                if ("." in test)  and test.count(".") <2:
                    # if test.count(".") > 1:
                    #     loops = test.count(".")

                    test = test.replace(" ","")
                    # separ_list = [".", "e", "+", "-"]
                    all_dots = [ i for i in range(len(test)) if test[i] is "." ]
                    # print(all_dots)
                    # exit()
                    for i in all_dots:
                        pos_of_dot = i


                        if (pos_of_dot>0 and pos_of_dot<len(test)-1):
                            if (not test[pos_of_dot-1].isdecimal())  and (not test[pos_of_dot+1].isdecimal()) :
                                it_is_decimal = False
                                return it_is_decimal
                            # elif not test[pos_of_dot+1].isdecimal():
                            #     it_is_decimal = False
                            #     return it_is_decimal
                        elif pos_of_dot == 0 and not test[pos_of_dot+1].isdecimal():
                            it_is_decimal = False
                            return it_is_decimal
                        elif pos_of_dot == len(test)-1 and not test[pos_of_dot-1].isdecimal():
                            it_is_decimal = False
                            return it_is_decimal
                elif ("." in test)  and test.count(".") >1:
                    it_is_decimal = False
                    return it_is_decimal
        else:
            it_is_decimal = False
            return it_is_decimal

        return it_is_decimal
