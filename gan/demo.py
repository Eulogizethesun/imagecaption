#from image_captioning import image_captioning, Vocabulary
from gan.image_captioning import image_captioning,Vocabulary


class Vocabulary(object):
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def __call__(self, word):
        if not word in self.word2idx:
            return self.word2idx['<unk>']
        return self.word2idx[word]

    def __len__(self):
        return len(self.word2idx)


def caption():

    caption_set = image_captioning('media/0.jpg')

    print(caption_set)
    for caption in caption_set:
        print(caption.strip('<sos> ').strip(' <eos>'))
