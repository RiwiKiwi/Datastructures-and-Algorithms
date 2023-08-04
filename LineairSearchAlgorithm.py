# Basic lineair search
def linear_search(search_list,target_value):
  for eln in range(len(search_list)):
        if search_list[eln] == target_value:
            #returning the index of that value
          return eln
        else:
          continue
  raise ValueError(f"{target_value} not in list")


values = [54, 22, 46, 99]
print(linear_search(values, 99))

#BEST CASE => O(1)
#WORST CASE => O(N)
#AVERAGE CASE => O(N/2) or just O(N)

#COMPLEXITY => O(N)

# FINDING MAXIMUM VALUE IN A LIST
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
highest_score = linear_search(test_scores)

#Prints out the highest score in the list
print(highest_score)

