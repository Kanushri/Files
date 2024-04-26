
#Core Code

import re
from datetime import datetime

def callPythonScript(ocr_string):
    data = "food Basics 634-1896 ( 905 ) # 100656 Store R105216170 HST # E & OE GROCERY 1.39 PUDD SELECTION 3.99 JAM SELECTION 2.99 PICKLE SELECTION H FR.PUN 2 ) SELECTION ( 4.98 2 @ $ 2.49 2.49 SELECTION APPL.G 4.99 TOSTITOS DIP TOST.SCOOP CHIP H 3.50 1 @ 2 / $ 7.00 Saving 0.49 BEARPAWS BROWNIE 2.99 Saving 0.50 ( 2 ) BOYARD.CAN . MEAL 2 @ $ 1.79 3.58 Saving 0.40 CINCRUNCH CER . 5.49 BCROCK.FRUIT.SNA 3.99 H KOOLA FRUIT DRNK H 2.99 CHAHOY MINI COOK 2 @ 2 / $ 5.00 5.00 Saving 1.98 CC.SOFT DRK H 3.49 UNICO OLIVE 1.99 Saving 1.50 ( 3 ) Y Y AM - GUEU.AL.V H 3 @ $ 1.48 4.44 Saving 2.43 REDBULL EN . DRINK H 7.99 Saving 1.50 NEAT IR SPRING ROLLS 4.99 PRODUCE ROMAINE HEARTS 2.88 Saving 1.10 GREEN GRAPES SEE 0.980 kg Gross -0.005 kg Tare = 0.975 kg Net @ $ 6.77 / kg 8.55 Saving 1.08 SEEDLESS MEDIUM 2.25 STRAWBERRIES 4.88 Saving 1.10 DELI SELECTION SAL.PE 5.99 PI HUNGARIAN SA 3.99 FS . TRADITIONAL M 4.99 FROZEN FOOD ( 3 ) HUNGMAN FRIED CH 3 @ $ 5.99 17.97 POPS 3 CHSE PIZZ 2.99 Saving 1.50 MICHELINA FETTUC 2.49 ( 2 ) MICHELINA FETTU . 2 @ $ 2.49 4.98 DAIRY STARB.CARA.MACC . 7.99 GAYLEA REFR.TOPP 4.49 GENERAL MERC FB 25X19T SH.REU H 4 @ 3 / $ 0.99 1.32 SERV . BAKERY WHOLE WHEPT PITA 1.39 SUBTOTAL 148.42 32.70 HST ( 13.000 ) % 4.25 TOTAL 152.67 CREDIT CR 152.67 Total number of items sold = 44 ****** Your savings today ****** Promotional discounts 13.58 Total of your savings 13.58 RETAIN RECEIPT FOR PRODUCT RETURN WITHIN 14 DAYS . SEE STORE FOR DETAILS . * CUSTOMER CARE NUMBER 1-866-595-5554 * *** foodbasics.ca *** Transferring your prescriptions to our Pharmacy is easy . ( 905 ) 634-2391 How did we do ? Tell us at FOODBASICSFEEDBACK.COM to win $ 1000 IN FREE GROCERIES . Monthly winners Your code 24350970024220700423 Trans . Type : PURCHASE Account : VISA CAD $ 152.67 Card Type : CREDIT Card ********* Number : 2012 P DateTime 24/01/29 09 : : 51.39 158704 Ref . # : Auth # : 479584 SCOTIABANK VISA A0000020031010 0000000000 00 APPROVED - THANK YOU Keep this copy for your records *** CUSTOMER COPY *** 01/29/2024 09:51 AM CASHIER 185 100656 02 4520 ce355ea9-410a-42a7-95c0-bb7dda62073f "
    data_array = data.split()

    def data_split():
       return data.split()
    def Get_Date(StoreName):
      #print("XXXXXXXXXXXXXX Fetching Date XXXXXXXXXXXXx")
      date= None
      if StoreName=="CVS" or StoreName=="cvs":
          string_dates=[]
          pattern = r'\b((?:\b(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+\d{1,2}\s+\d{4}\b))\b'
          matches = re.findall(pattern, data, re.IGNORECASE)
          for match in matches:
              date_obj=datetime.strptime(str(match),"%B %d %Y")
              formatted_date = date_obj.strftime("%m/%d/%Y")
              string_dates.append(formatted_date)
          #print(string_dates)
          date=min(string_dates)
          return date

      elif StoreName=="LCBO" or StoreName=="metro":
          string_dates=[]
          pattern = r'\b(\d{2}/\d{2}/\d{2}|\d{1}/\d{2}/\d{2}|\d{2}/\d{2}/\d{4}|\d{2}/\d{4}|(?:\d{1,2} (?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC) \d{4}))\b'
          matches = re.findall(pattern, data, re.IGNORECASE)
          for match in matches:
              formats = ["%d/%m/%y", "%d/%m/%Y", "%d %b %Y", "%b %d %Y"]
              for fmt in formats:
                try:
                  date_obj = datetime.strptime(str(match), fmt)
                  formatted_date = date_obj.strftime("%m/%d/%Y")
                  string_dates.append(formatted_date)
                  break
                except ValueError:
                  pass
          if string_dates:
            return min(string_dates)
          else:
              return None
      elif date is None:
          # Iterate through the data array to find the date
          for date in data_array:
                  if re.match(r'\d{2}/\d{2}/\d{2}|\d{1}/\d{2}/\d{2}|\d{2}/\d{2}/\d{4}|\d{2}/\d{4}', date):
                      # print("Date found:", date)
                      return date
                      break
      elif date is None:
            #print("Date not Found")
            return ("Date not Found")
    def Get_Total_Cash(StoreName,Card_details):
          store_card_data=None
          # Pattern to extract text between 'storeName' and 'CardDetails'
          store_card_pattern = re.escape(StoreName) + "(.*?)" + re.escape(str(Card_details))
          # Extract text between 'storeName' and 'CardDetails'
          store_card_match = re.search(store_card_pattern, data, re.IGNORECASE | re.DOTALL)
          if store_card_match:
            store_card_data = store_card_match.group(1).strip()
          else:
            #print("Text between storeName and CardDetails not found.")
            exit()
          #initializing the variable
          Total_Cash = None
          if  StoreName=="CVS":
            #patterns to search for
            pattern = r'(?:TOTAL).*?(\d+\.\d+)'
            #print("XXXXXXXXXX  Calculating Total Amount for word TOTAL or TOTTL XXXXXXXXXXXXXX")
            #Search for pattern in the text
            matches = re.findall(pattern, data, re.IGNORECASE)
            numeric_matches = [float(match) for match in matches]
            #print(numeric_matches)
            #Fetch the next available numeric value
            if matches:
              Total_Cash=max(numeric_matches)
              #print("TOTAL AMOUNT :",Total_Cash)
              return(Total_Cash)
          elif  StoreName=="Walmart":
            # Pattern to extract text between 'storeName' and 'CardDetails'
            store_card_pattern = re.escape("SUBTOTAL") + "(.*?)" + re.escape("ACCOUNT")
            # Extract text between 'storeName' and 'CardDetails'
            store_card_match = re.search(store_card_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_card_match:
              store_card_data = store_card_match.group(1).strip()
            else:
              #print("Text between storeName and CardDetails not found.")
              exit()
            #patterns to search for
            pattern = r'(?:TOTAL).*?(\d+\.\d+)'
            #print("XXXXXXXXXX  Calculating Total Amount for word TOTAL or TOTTL XXXXXXXXXXXXXX")
            #Search for pattern in the text
            matches = re.findall(pattern, data, re.IGNORECASE)
            numeric_matches = [float(match) for match in matches]
            #print(numeric_matches)
            #Fetch the next available numeric value
            if matches:
              Total_Cash=max(numeric_matches)
              #print("TOTAL AMOUNT :",Total_Cash)
              return(Total_Cash)
          elif  StoreName=="SPROUTS":
            #search for the below pattern
            pattern =r'(?:Amount).*?(\d+\.\d+)'
            matches = re.findall(pattern, data, re.IGNORECASE)
            # print("MATCHES",matches)
            for match in matches:
              index = data.find(match)
              if index != -1:
                  # Look for float value in the next 4 places
                  for i in range(index, index +5):
                      try:
                          Total_Cash = float(data[i:i+5])
                          #print("TOTAL AMOUNT :", Total_Cash)
                          return Total_Cash
                      except ValueError:
                          pass
                  # If float value not found, look in the previous 4 places
                  for i in range(index, index - 5, -1):
                      try:
                          Total_Cash = float(data[i:i+5])
                          #print("TOTAL AMOUNT :", Total_Cash)
                          return Total_Cash
                      except ValueError:
                          pass

          #Since Target word is at the end in the receipt, we are not slicing the text between storename and card_details
          elif StoreName=="Target" or StoreName=="TARGET" or StoreName=="Walmart":
            #patterns to search for
            pattern = r'(?:TOTAL||TOTTL).*?(\d+\.\d+)'
            #print("XXXXXXXXXX  Calculating Total Amount for word TOTAL or TOTTL XXXXXXXXXXXXXX")
            #Search for pattern in the text
            matches = re.findall(pattern, data, re.IGNORECASE)
            numeric_matches = [float(match) for match in matches]
            #print(numeric_matches)
            #Fetch the next available numeric value
            if matches:
              Total_Cash=max(numeric_matches)
              #print("TOTAL AMOUNT :",Total_Cash)
              return(Total_Cash)

          #Since WinnDixie word has a tick mark in the receipt, changing the storename for text extraction
          elif StoreName=="WinnDixie":
            #patterns to search for
            pattern = r'(?:TOTAL|BALANCE|AMOUNT|TOTTL).*?(\d+\.\d+)'
            #print("XXXXXXXXXX  Calculating Total Amount for word TOTAL or TOTTL XXXXXXXXXXXXXX")
            #Search for pattern in the text
            matches = re.findall(pattern, store_card_data, re.IGNORECASE)
            numeric_matches = [float(match) for match in matches]
            #print(numeric_matches)
            #Fetch the next available numeric value
            if matches:
              Total_Cash=max(numeric_matches)
              #print("TOTAL AMOUNT :",Total_Cash)
              return(Total_Cash)

          elif StoreName=="COSTCO WHOLESALE":
            #search for the below pattern
            pattern = r'\bTOTAL\b.*?(\d+\.\d+)'
            matches = re.findall(pattern, data, re.IGNORECASE)
            #print("MATCHES",matches)
            for match in matches:
              index = data.find(match)
              if index != -1:
                  # Look for float value in the next 4 places
                  for i in range(index, index + 5):
                      try:
                          Total_Cash = float(data[i:i+5])
                          #print("TOTAL AMOUNT :", Total_Cash)
                          return Total_Cash
                      except ValueError:
                          pass
                  # If float value not found, look in the previous 4 places
                  for i in range(index, index - 5, -1):
                      try:
                          Total_Cash = float(data[i:i+5])
                          #print("TOTAL AMOUNT :", Total_Cash)
                          return Total_Cash
                      except ValueError:
                          pass
          # print("No total amount found")
            return None

            # Initialize an array to store extracted values
            numeric_matches=[]
            # Iterate from the start and end of the string, capturing up to 4 matches on each side
            for i in range(1, 5):
                if len(matches) >= i:
                    numeric_matches.append(float(matches[-i]))  # Append the matched value as a float
                if len(matches) >= i:
                    numeric_matches.append(float(matches[i - 1]))  # Append the matched value as a float
            # Fetch the maximum value from the array
            Total_Cash = max(numeric_matches)
            return Total_Cash

          #if the store name is not walmart or Target, then execute the below if method
          elif Total_Cash is None:
            #patterns to search for
            pattern = r'(?:TOTAL|BALANCE|Total|AMOUNT|TOTTL).*?(\d+\.\d+)'
          # print("XXXXXXXXXX  Calculating Total Amount XXXXXXXXXXXXXX")
            #Search for pattern in the text
            matches = re.findall(pattern, data, re.IGNORECASE)


            numeric_matches = [float(match) for match in matches]
            #print(numeric_matches)
            #Fetch the next available numeric value
            if matches:
              Total_Cash=max(numeric_matches)
              #print("TOTAL AMOUNT :",Total_Cash)
              return(Total_Cash)
            else:
              # print("Total amount not found.")
              return("Total amount not found.")
    def Get_LineItems(StoreName,Total_cash):
          num=None
          if StoreName=="Target" or StoreName=="TARGET":
              # Extract product codes using regular expression
              product_codes = re.findall(r'\b\d{9}\b', data)
              #print(product_codes)
              # Count the number of unique product codes
              num = len(product_codes)
              #print("Number of line items:", num)
              return num
          elif StoreName=="Walmart" or StoreName=="walmart":
              if "DISCOUNT MULTI" in data or "MULTI DISCOUNT" in data:
                # Pattern to extract text between the word "StoreName" and "DISCOUNT"
                store_cash_pattern = re.escape(StoreName) + "(.*?)" + re.escape("DISCOUNT")
                # Extract text between  word "StoreName" and "DISCOUNT"
                store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
                if store_cash_match:
                  store_cash_data = store_cash_match.group(1).strip()
                else:
                  exit()
                # Search for numbers 12 digits in the extracted text
                product_codes1 = re.findall(r'\b\d{12}\b', store_cash_data)
                product_codes2 = re.findall(r'\b\d{12}[A-Za-z]\b', store_cash_data)
                product_codes = product_codes1 + product_codes2
                #print(product_codes)
                # Count the number of matches
                num = len(product_codes)
                #print("Number of items:", num)
                return num
              else:
                # Extract product codes using regular expression
                product_codes1 = re.findall(r'\b\d{12}\b', data)
                product_codes2 = re.findall(r'\b\d{12}[A-Za-z]\b', data)
                product_codes = product_codes1 + product_codes2
                #print(product_codes)
                # Count the number of unique product codes
                num = len(product_codes)
                #print("Number of line items:", num)
                return num
          elif StoreName=="PAVILIONS" or StoreName=="pavilions" or StoreName=="SAFEWAYS":
              # Find the index of "GROCERY" and total_cash
              start_index = data.find("GROCERY")
              end_index = data.find(str(Total_cash))

              # Extract the text between "GROCERY" and total_cash
              extracted_text = data[start_index:end_index+3]
              #print(extracted_text)
              # Search for numbers between 4 to 11 digits in the extracted text
              pattern = r'\b\d{4,11}\b'
              matches = re.findall(pattern, extracted_text)
              #print(matches)
              # Count the number of matches
              num = len(matches)
              #print("Number of items:", num)
              return num
          elif StoreName=="Walgreens" or StoreName=="WALGREENS" :
              # Search for numbers between 4 to 11 digits in the extracted text
              pattern = r'\b\d{11}\b'
              matches = re.findall(pattern, data)
              #print(matches)
              # Count the number of matches
              num = len(matches)
              #print("Number of items:", num)
              return num
          elif StoreName=="REDNERS":
            # Pattern to extract text between the word "Terminal" and Total_cash
            store_cash_pattern = re.escape("Terminal") + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "Terminal" and Total_cash
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{5,12}\b'
            matches = re.findall(pattern, store_cash_data)
          # print(matches)
            # Count the number of matches
            num = len(matches)
          # print("Number of items:", num)
            return num
          elif StoreName=="COSTCO WHOLESALE":
            # Pattern to extract text between the word "Terminal" and "TOTAL"
            store_cash_pattern = re.escape("CHECKOUT") + "(.*?)" + re.escape("TOTAL")
            # Extract text between  word "Terminal" and "TOTAL"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{6,7}\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          elif StoreName=="LCBO":
            # Pattern to extract text between the word "QUESTIONS " and "Total_cash"
            store_cash_pattern = re.escape("QUESTIONS") + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "QUESTIONS" and "Total_cash"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{8}\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          elif StoreName=="CVS" or StoreName=="cvs":
            # Pattern to extract text between the word "StoreName " and "Total_cash"
            store_cash_pattern = re.escape(StoreName) + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "StoreName" and "Total_cash"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d+\.\d+[A-Z]\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          elif StoreName=="Rexall" :
            # Pattern to extract text between the word "StoreName " and "Total_cash"
            store_cash_pattern = re.escape(StoreName) + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "StoreName" and "Total_cash"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{11}\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          elif StoreName=="Osco shaws" or StoreName=="shaws Osco":
            # Pattern to extract text between the word "GROCERY " and "Total_cash"
            store_cash_pattern = re.escape("GROCERY") + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "GROCERY" and "Total_cash"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{5,10}\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          elif StoreName=="VONS" or StoreName=="Randalls" :
            # Pattern to extract text between the word "GROCERY" and "Total_cash"
            store_cash_pattern = re.escape("GROCERY") + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "GROCERY" and "Total_cash"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{4,12}\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          elif StoreName=="DOLLARAMA" :
            # Pattern to extract text between the word "StoreName" and "Total_cash"
            store_cash_pattern = re.escape(StoreName) + "(.*?)" + re.escape(str(Total_cash))
            # Extract text between  word "StoreName" and "Total_cash"
            store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
            if store_cash_match:
              store_cash_data = store_cash_match.group(1).strip()
            else:
              exit()
            # Search for numbers between 4 to 11 digits in the extracted text
            pattern = r'\b\d{12}\b'
            matches = re.findall(pattern, store_cash_data)
            #print(matches)
            # Count the number of matches
            num = len(matches)
            #print("Number of items:", num)
            return num
          # elif StoreName=="Longos" :
          #   # Pattern to extract text between the word "GROCERY" and "Subtotal"
          #   store_cash_pattern = re.escape("GROCERY") + "(.*?)" + re.escape("Subtotal")
          #   # Extract text between  word "StoreName" and "Total_cash"
          #   store_cash_match = re.search(store_cash_pattern, data, re.IGNORECASE | re.DOTALL)
          #   if store_cash_match:
          #     store_cash_data = store_cash_match.group(1).strip()
          #   else:
          #     exit()
          #   # Search for numbers between 4 to 11 digits in the extracted text
          #   pattern = r'\b\d+\.\d+\b'
          #   matches = re.findall(pattern, store_cash_data)
          #   #print(matches)
          #   # Count the number of matches
          #   num = len(matches)
          #   #print("Number of items:", num)
          #   return num
          elif num is None:
            # Define the search patterns
            line_item_phrase=["SOLD","sold","items","ITEMS","diten","ditem","VENDUS","articles","Items","count"]
            found_match = False
            num= None
            #FROM HERRE
            for phrase in line_item_phrase:
                for index, item in enumerate(data_array):
                    if phrase in item:
                        #print(f"Found '{phrase}' in '{item}'")
                        # Search in the next 5 items for a numeric value
                        for i in range(index + 1, min(len(data_array), index + 6)):

                            if re.match(r'\b\d{1,2}\b$', data_array[i]):
                                num=float(data_array[i])
                                if num>0:
                                    #print(f"Found numeric value '{num}' in the next 5 items")
                                    found_match= True
                                    break


                        if found_match:
                            break  # Exit the outer loop if a match is found

                        # Search in the previous 5 items for a numeric value
                        for i in range(max(0, index - 4), index):

                            if re.match(r'\b\d{1,2}\b$', data_array[i]):
                                num=float(data_array[i])
                                if num>0:
                                    #print(f"Found numeric value '{num}' in the previous 5 items")
                                    found_match= True
                                    break

                        if found_match:
                            break  # Exit the outer loop if a match is found

                if found_match:
                    #print("ITEM COUNT:",num)
                    return num
                    break  # Exit the outermost loop if a match is found
    def Multiple_card_scenario(result_array):
          #print("XXXXXXXXXXXXXXXXXXXXXXXXXX MULTIPLE CARD SCENARIO XXXXXXXXXXXXXXXXXXXXXXXXXXX")
          phrase2=["Auth","AUTH","APPROVED","SOLD","AID","Account","Ref"]
          required_array=[] #array for storing index of result array
          final_array=[] #array which stores the subtracted value of indexes
          #iterating in the result_array which consists of 4 digit numbers to fetch the index numbers of the values
          for element in result_array:
            #try:
              for index, item in enumerate(data_array):
                if element in item:
                  required_array.append(index) #appending the index values into array
            #except:
            # pass
          #iterate in phrase2
          for x in phrase2:

            #check if each value is available in main array
            if x in data_array:
              # print("MATCHING PHRASE :",x)
              pattern_phrase_index=data_array.index(x)

              #iterating over the 4 digit value indexes to subtract the values from the phrase match index
              for y in required_array:
                subtracted_value=pattern_phrase_index-y
                final_array.append(subtracted_value)


              # Initialize variables
              lowest_value = None
              lowest_index = None

              # Find the lowest value ignoring values less than or equal to 0
              for a, value in enumerate(final_array):
                  if value > 0 and (lowest_value is None or value < lowest_value):

                      lowest_value = value
                      lowest_index = a

              if lowest_index is not None:
                card_number=result_array[lowest_index]
                #print("Card Number:", card_number)
                return card_number
                break
              else:
                #print("No CARD NUMBER FOUND")
                return ("No CARD NUMBER FOUND")
    def Single_card_scenario():
          #print("XXXXXXXXXXXXXXXXXXXXXXXXXX SINGLE CARD SCENARIO XXXXXXXXXXXXXXXXXXXXXXXXXXX")

          # Initialize variables to track the position and result
          position = 0
          result = None
          phrase=["VISA","DEBIT","MASTERCARD","Account","ACCOUNT","ACCT","DEBIT card"]

          # Loop through the data array
          while position < len(data_array):
              # Search for a pattern similar to "***" or "XXX"
              if re.match(r'\*{3}|XXX', data_array[position]):
                  # Check the next 5 elements for a 4-digit numeric value
                  for i in range(1, 4):
                      if position + i < len(data_array) and re.match(r'^\d{4}$', data_array[position + i]):
                          result = data_array[position + i]
                          break
                  # If 4-digit numeric value not found in next 5 elements, check the previous 5 elements
                  if not result:
                      for i in range(1, 4):
                          if position - i >= 0 and re.match(r'^\d{4}$', data_array[position - i]):
                              result = data_array[position - i]
                              break

              #if none of the result matches, search for the phrase and match searching for next and previous 5 elements which is 4 digit
              elif not result:
                if any(word in data_array[position] for word in phrase):
                  # Check the next 5 elements for a 4-digit numeric value
                  for i in range(1, 6):
                      if (
                          position + i < len(data_array) and
                          re.match(r'^\d{4}$', data_array[position + i])
                      ):
                          result = data_array[position + i]
                          break
                  # If 4-digit numeric value not found in next 5 elements, check the previous 5 elements
                  if not result:
                      for i in range(1, 6):
                          if (
                              position - i >= 0 and
                              re.match(r'^\d{4}$', data_array[position - i])
                          ):
                              result = data_array[position - i]
                              break
              #if none of the above case works, trying to search for *** or XXX and fetching the 4 digit value which is with out space
              elif not result:
                for element in data_array:
                  if "***" in element or "XXX" in element:
                      match = re.search(r'\d{4}$', element)
                      if match:
                          result = match.group()
                          break
              if result:
                  break
              position += 1

          #print("Card Number:", result)

          return result
    def Check_IF_Multiple_card():
          #print("XXXXXXXXXXXXXXXXXXXXXXXXXX CHECKING FOR NO OF CARDS AVAILABLE XXXXXXXXXXXXXXXXXXXXXXXXXXX")
          cash=["CASH"]
          PaidCash= None
          # for b in data_array:
          #   for c in cash:
          #     if b==c:
          #       PaidCash ="Cash"
          #       break
          #     break

          if PaidCash is None:
            # Initialize an empty array to store the 4-digit numbers
            result_array = []

            # Iterate through the data array
            for i, word in enumerate(data_array):
                # Check if the word contains "***" or "XXX"
                if "***" in word or "XXX" in word:
                    # Search for 4-digit numbers in the next 5 elements
                    for j in range(1, 6):
                        if i + j < len(data_array) and re.match(r'^\d{4}$', data_array[i + j]):
                            result_array.append(data_array[i + j])
                            break
                    # If no match found in the next 5 elements, search in the previous 5 elements
                    else:
                        for j in range(1, 6):
                            if i - j >= 0 and re.match(r'^\d{4}$', data_array[i - j]):
                                result_array.append(data_array[i - j])
                                break
            #if none of the above case works, trying to search for *** or XXX and fetching the 4 digit value which is with out space
            if not result_array:
              for element in data_array:
                  if "***" in element or "XXX" in element:
                      match = re.search(r'\d{4}$', element)
                      if match:
                          result_array.append(match.group())
            result_array=list(set(result_array))    # Remove duplicates by converting to Sets
            # print("CARD NUMBERS FOUND:",result_array)


            if len(result_array) > 1:
              return Multiple_card_scenario(result_array)
            elif len(result_array)<1:
              return Single_card_scenario()
            else:
              return result_array[0]
          else:
            #print(PaidCash)
            return PaidCash
    def extract_store_name():
          string=data
          patterns = [
            r"\b(Albertsons|METRO|Winn|Target|TARGET|food Basics|Walmart|BAZAAR HOME|meijer|LONDON DRUGS|VONS|CVS|BIGLOTS|CARDENAS |RITE AID|SPROUTS FARMERS MARKET|PETSMART|DOLLARAMA|SAFEWAY|SAFEWAYS|SPROUTS|Randalls|PAVILIONS|shaws Osco|Walgreens|Longos|Jewel|ADONIS|REDNERS|THE FRESH MARKET|ho WHOLESALE|LCBO|Coles|Osco shaws|Rexall|ACME|RITE AID Store|GARAGE LIBERTY VILLAGE MARKET|Winn\Dixie)\b",
          ]
          store = 'storeName'
          # Iterate through patterns to find matches
          for pattern in patterns:
              match = re.search(pattern, string, re.IGNORECASE)
              if match:
                  try:
                      store = match.group(1)
                  except IndexError:
                      regex_used = 'No store found'
                      pass
                  else:
                      break

          if store == 'storeName':
              pattern = r"\b(?:[A-Za-z]+\s*){1,3}(?:Store|Shop|Market|Supermarket)\b"
              match = re.search(pattern, string, re.IGNORECASE)

              if match:
                  try:
                      store = match.group(0).strip()
                  except IndexError:
                      regex_used = 'No store found'
                      pass
          elif store == 'storeName':
              StoreName_phrase=["AAlbertsons","metro","meijer","Target","TARGET","LONDON DRUGS","BIGLOTS","food Basics","CARDENAS ","Walmart","RITE AID","shaws Osco","DOLLARAMA","Randalls","BAZAAR HOM","VONS","CVS","PETSMART","extracare","SPROUTS FARMERS MARKET","SAFEWAY","SAFEWAYS","PAVILIONS","Walgreens","Longos","Jewel"]
              matched_store=None

              for phrase in StoreName_phrase:
                for item in string:
                  if phrase.lower() in item.lower():
                    store = item
                    break
                  if store != 'storeName':
                    break



          # print("Store Name: ",store)
          return store
    
    StoreName = extract_store_name()
    date_info = Get_Date(StoreName)
    Card_details = Check_IF_Multiple_card()
    Total_cash = Get_Total_Cash(StoreName,Card_details)
    Line_count = Get_LineItems(StoreName,Total_cash)
    return StoreName

