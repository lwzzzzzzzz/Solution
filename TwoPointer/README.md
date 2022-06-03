### 双指针
- 通过利用两个指针对数组或序链表进行操作，协同完成一些任务。
    *当两个指针一个方向时叫快慢指针；不同方向叫对撞指针，并且进行操作的数组或链表可以先进行排序或其他操作，以满足一些特定需求。*
    
较为典型问题
1、链表环问题（链表快慢指针）
    双指针中有一种很典型的问题，即单链表环问题，这里对问题做了一个剖析[FloydCycle](./FloydCycle.md)
    - [LinkedListCycle2](./LinkedListCycle2.py)
    
2、对自身做对撞指针
    其中TwoSum问题最为典型
    - [TwoSum2](./TwoSum2.py)
    - [SumOfSquareNumbers](./SumOfSquareNumbers.py)
    - [ValidPalindrome2](./ValidPalindrome2.py)
   > 适用于这种方式的问题，一般是有唯一解（但凡事皆有例外 - -！

3、对自身做快慢指针
    以快慢指针维护一个滑动窗口(slide window)，处理或判断滑动窗口内的子序列，返回需要的结果
    - [MinimumWindowSubstring](./MinimumWindowSubstring.py)
    - [LongestSubstringWithKUniqueCharacters](LongestSubstringWithKUniqueCharacters.py)    
        
   > 其本质就是通过滑动窗口穷尽所有符合要求的连续子序列，再在窗口移动（穷举）过程中保留最优解

    * 因其问题可能会稍微复杂一些，故给出伪代码模版大致如下（灵活变动）：*
    
    ```python
    # 假设给定序列为 li
    
    left, right = 0, 0 # 左右指针
    for i in range(len(li)):
        # maybe you will do sth in this to get result

        while (slide window condition):
            # todo someting make slide window condition been satisfied
            # or maybe you will do sth in this to get result

            left += 1 # 窗口左边界移动
            
        # or maybe you will do sth in this to get result

        right += 1 # 窗口右边界移动
    ```
    
3、对两个不同序列做双指针
    最典型的就是两个已有序的序列，按一定要求归并；并且涉及到两个序列操作的问题，一般需要对序列做必要的排序。
    - [MergeSortedArray](./MergeSortedArray.py)
    - [LongestWordInDictionaryThroughDeleting](./LongestWordInDictionaryThroughDeleting.py) （归并变形题）