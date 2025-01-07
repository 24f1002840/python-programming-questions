# print('soyabeans' in ['Water','Soyabeans','Vitamin B12','Sugar'])
# l = [99.17,48.39,5.67,14.84,74.75]
# a=sum(l)/len(l)
# print(a)
# print(round(a,2))
# print("--------------------------------")
# s = "IITM_is_a_prestigious_institue"
# print(len(s))
# ascii = map(lambda x : ord(x),s)
# af = filter(lambda x : x>111,ascii)
# ch = map(lambda x: chr(x),af)
# print(list(ch),len(list(ch)))
# # af = filter(lambda x : x<=111,ascii)
# # ch = map(lambda x: chr(x),af)
# # print(list(ch),len(list(ch)))
# ascii = map(lambda x : ord(x),s)

# af = filter(lambda x : x<=96,ascii)
# x = list(af)
# print(len(x))

# ascii = map(lambda x : ord(x),s)
# ascii = list(ascii)
# ascii.sort()
# ch = map(lambda x: chr(x),ascii)
# # print(list(ch))
# from functools import reduce

# print(str(reduce(lambda x , y : x+y,ch)))

# print(len(s))
# print(19**2+11**2)
# print(list("str(reduce(lambda x , y : x+y,ch))"))
def sort_sentence_by_ascii(sentence: str, k: int) -> tuple:
    sorted_sentence = ''.join(sorted(sentence))  # Sort sentence by ASCII value
    x = sum(1 for char in sentence if ord(char) <= k)  # Count of chars ≤ k
    y = len(sentence) - x  # Count of chars > k
    return sorted_sentence, x**2 + y**2  # Return tuple

# Example usage:
# sentence = "hello world"
# k = 110
# print(sort_sentence_by_ascii(sentence, k))  
def func():
    global data 
    data = 'jalepenos'
func()
def func1():
    print(data)
func1()
print("staurday",13880)
