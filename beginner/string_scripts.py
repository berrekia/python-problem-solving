import re
class String:
    def __init__(self, seq, seq_list):
        self.seq = seq
        self.seq_list = seq_list

    def get_seq(self):
        return self.seq

    def string_split(self):
        if re.search(r"\s",self.seq):
            return "\n".join(self.seq.split())
        return self.seq
    
    def string_sort(self):
        return self.seq_list.sort(key=len)