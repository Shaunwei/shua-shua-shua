class Packer:
    delimiter = '#|#'

    @staticmethod
    def pack(string_list):
        packed = ''
        for s in string_list:
            mlist = list(s)
            for i, char in enumerate(mlist):
                if char == '#':
                    mlist[i] = char + char
            packed += ''.join(mlist)
            packed += Packer.delimiter
        return packed

    @staticmethod
    def unpack(string):
        slist = []
        s = ''
        i = 0
        while i < len(string):
            if string[i] != '#':
                s += string[i]
                i += 1
            else:
                if i < len(string) - 1:
                    if string[i + 1] == '#':
                        s += string[i]
                        i += 2
                    else:
                        slist.append(s)
                        s = ''
                        i += 3
                else:
                    slist.append(s)
                    i += 1
        return slist




if __name__ == '__main__':
    slist = [
      'a##ab#d',
      '1)!*nac',
      '',
      '###|##',
      '|',
      '12ab91@'
    ]

    packed_string = Packer.pack(slist)
    print('Packed String: ' + packed_string)
    print('Unpacking...')
    print(Packer.unpack(packed_string))
    #Packed String: a####ab##d#|#1)!*nac#|##|#######|#####|#|#|#12ab91@#|#
    #Unpacking...
    #['a##ab#d', '1)!*nac', '', '###|##', '|', '12ab91@']
