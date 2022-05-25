def findsubstringscontroller(list1, list2):
        length = len(list1)
        count = 0
        for x in range(length):
                issubstring = findsubstrings(list1[x], list2[x])
                if (issubstring):
                        count += 1
        return count;


def findsubstrings(string1, string2):
        def _iter():
                for a, b in zip(string1, string2):
                        if a == b:
                                yield a
                        else:
                                return
        return ''.join(_iter())



list1 = ["dog", "cat", "house"]
list2 = ['doggy', "catastrophic", "village"]

answer = findsubstringscontroller(list1, list2)
print(answer)

