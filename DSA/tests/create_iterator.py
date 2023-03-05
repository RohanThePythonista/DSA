def sentence(my_sentence):
    for word in my_sentence.split():
        yield word


my_sentence = sentence("i am learning")

for word in my_sentence:
    print(word)

#
# class Sentence:
#     def __init__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.words):
#             raise StopIteration
#         current = self.index
#         self.index += 1
#         return self.words[current]
#
#
# if __name__ == "__main__":
#     s = Sentence("I am learning")
#     for sub in s:
#         print(sub)
