'''
2. Взявши за основу код домашнього завдання лекції 14, розробіть
набір тестів з використання бібліотеки рутезі для методів додавання
нових елементів, пошуку мінімального і максимального значень та
видалення елементів бінарного дерева.
'''

from binarytree import *

class Тгее:
    
    def __init__(self):
        self.vals = []
    
    def insert(self, nums):
        try:
            bst1 = [nums[0]]
            def main():
                i = 0
                for x in range(len(nums)):
                    if nums[2*i+1] <= nums[i]:
                        bst1.append(nums[2*i+1])
                    else:
                        print('ERROR:Wrong item in list!!!')
                    if nums[2*i+2] >= nums[i]:
                        bst1.append(nums[2*i+2])
                    else:
                        print('ERROR:Wrong item in list!!!')
                    if i < (len(nums) - 3):
                        i = i+1
            main()
        except:
            self.vals = bst1[:]
            print(self.vals)
    
    def get_min(self):
        min1 = []
        min = self.vals[:]
        for x in min:
            if x != None:
                min1.append(x)
        min1.sort()
        print(f'minimum: {min1[0]}')
        return min1[0]
  
        
    def get_max(self):
        max1 = []
        max = self.vals[:]
        for x in max:
            if x != None:
                max1.append(x)
        max1.sort()
        print(f'maximum: {max1[-1]}')
        return max1[-1]

    def delete(self, index):
        try:
            self.vals[index] = self.vals[2*index+2]  
            self.vals.pop(index)
            self.vals.insert(index, self.vals[2*index+1]) 
            self.vals[2*index+2] = None
            print(self.vals)
        except:
            self.vals.pop(index)
            self.vals.insert(index, None)
            print(self.vals)
            
    def printer(self):
        binary_tree = build(self.vals)
        print('Binary Search Tree from list \n',
        binary_tree)
        

def main_insert(nums):
    bst = Тгее()
    bst.insert(nums)
    bst.printer()
    return bst.vals

def main_max(nums):
    bstmx = Тгее()
    bstmx.insert(nums)
    bstmx.printer()
    return bstmx.get_max()

def main_min(nums):
    bstmn = Тгее()
    bstmn.insert(nums)
    bstmn.printer()
    return bstmn.get_min()

def main_del(nums, val):
    bstdl = Тгее()
    bstdl.insert(nums)
    bstdl.delete(val)
    bstdl.printer()
    return bstdl.vals



