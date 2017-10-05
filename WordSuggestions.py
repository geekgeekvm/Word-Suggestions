class Node:
    def __init__(self,k):
        self.k=k
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def PrintList(self):
        temp=self.head
        while temp is not None:
            print(temp.k)
            temp=temp.next

    def Push(self,k):
        if self.head is None:
            self.head=Node(k)
        else:
            newNode=Node(k)
            newNode.next=self.head
            self.head=newNode

    def Pop(self):
        ret=self.head
        self.head=self.head.next
        return ret

    def Search(self,k):
        temp=self.head
        while temp is not None:
            if temp.k==k:
                print(k,end=' ')
                return True
            temp=temp.next
        return False


class HashTable:
    def __init__(self):
        self.ht=[None]*30
        

    def HashMap(self,k):
        x=33
        l=len(k)
        charList=[b for b in k]
        PolynomialAccumulation=ord(charList[0])
        for i in range(1,l):
            PolynomialAccumulation+=x*(ord(charList[i]))
        return PolynomialAccumulation
    
    def CompressionMap(self,i):
        value=i%30
        return value
    
    def Insert(self,key):
        self.key=key
        v=self.HashMap(key)
        value=self.CompressionMap(v)
        if self.ht[value] is None:
            ll=LinkedList()
            self.ht[value]=ll
            ll.Push(key)
        else:
            self.ht[value].Push(key)

    def Search(self,key):
        v=self.HashMap(key)
        value=self.CompressionMap(v)
        if self.ht[value] is None:
            return False
        else:
            return self.ht[value].Search(key)
        
    def Keys(self):
        for i in range(30):
            if self.ht[i] is not None:
                self.ht[i].PrintList()




def main():
    table=HashTable()
    f=open("spellis.dict")
    for line in f:
        for word in line.split():
            table.Insert(word)

    isValid=input("Enter a word to check for spelling")
    if (table.Search(isValid) is True):
        print("is a valid word")
    else:
        print("Not found in our dictionary. Did you mean: ")
        for i in range(0,len(isValid)):
            for charInt in range(97,123):
                if isValid[i] != chr(charInt):
                    newWord=isValid[:i]+str(chr(charInt))+isValid[i+1:]
                    table.Search(newWord)

        
        
        
        
    

if __name__=='__main__':
    main()