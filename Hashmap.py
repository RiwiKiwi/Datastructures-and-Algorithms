class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key,count_collisions = 0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self,hash_code):
      return hash_code % self.array_size

  #MY SETTER
  def assign(self,key,value):
    get_hash_code = self.hash(key)
    getindex = self.compressor(get_hash_code)
    # self.array[getindex] = value
    # need to check if there is an already existing value present
    current_array_value = self.array[getindex]
    # there are 3 options now (handeling collisions):
      #- It has the same key as key.
      #- It has a different key than key.
      #- It’s None

    #CASE ONE: THERE IS NOTHING
    if current_array_value == None:
      self.array[getindex] = [key,value]
    #CASE TWO: THERE IS SOMETHING
    elif current_array_value != None:
      # CASE TWO A)  == > check if the saved key is the same then overwrite the value
      if current_array_value[0] == key:
        current_array_value[1] = value
      # CASE TWO B) == > THE KEYS AREN'T THE SAME
      elif current_array_value[0] != key:
        number_collisions = 1
        while current_array_value[0] != key:
          new_hash_code = self.hash(key,number_collisions)
          new_array_index = self.compressor(new_hash_code)
          #this will be our new value
          current_array_value = self.array[new_array_index]

          if current_array_value == None:
            self.array[new_array_index] = [key,value]
            return
          if current_array_value != None:
            if current_array_value[0] == key:
              self.array[new_array_index] = [key,value]
              return
            if current_array_value[0] != key:
              number_collisions += 1
        return

  #MY GETTER
  def retrieve(self,key):
    get_hash_code = self.hash(key)
    getindex =  self.compressor(get_hash_code)
    # 2 keys could point at the same arrayindex so store it first in a variable
    possible_return_value = self.array[getindex]
    # CASE ONE: THAT ARRAY INDEX IS EMPTY
    if possible_return_value == None:
      return None
    # CASE TWO: THAT ARRAY INDEX ISN'T EMPTY
    elif possible_return_value != None:
      # CASE TWO A) if the retrieving key is the same as key as the input
      if possible_return_value[0] == key:
        return possible_return_value[1]
      # CASE TWO B) if the retrieving key is different
      elif possible_return_value[0]!= key:
        retrieval_collisions = 1

        while possible_return_value[0] != key:
          new_hash_code = self.hash(key,retrieval_collisions)
          retrieving_array_index = self.compressor(new_hash_code)
          # this could be the one we are looking for
          possible_return_value = self.array[retrieving_array_index]

          if possible_return_value == None:
            return None
          elif possible_return_value != None:

            if possible_return_value[0] == key:
              return possible_return_value[1]
            elif possible_return_value[0] != key:
              retrieval_collisions += 1
        return


hash_map = HashMap(15)
hash_map.assign("gabbro","igneous")
hash_map.assign("sandstone","sedimentary")
hash_map.assign("gneiss","metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))




