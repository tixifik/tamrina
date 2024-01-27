class MrKrabs:
    def process(self, dna):
        dna = dna + dna[:10]
        dna = dna.replace('tt', 'o')
        return dna


class SpongeBob(MrKrabs):
    def process(self, dna):
        sorted_length = sorted(str(len(super().process(dna))))
        sorted_length_str = ''.join(sorted_length)
        return int(sorted_length_str)


class Squidward:
    def process(self, dna):
        index = dna.find('x')
        if index != -1:
            dna = dna + str(index)
        i = 0
        while i + 2 < len(dna):
            if dna[i] == dna[i + 1] == dna[i + 2]:
                dna = dna.replace(dna[i:i + 3], '(0_0)')
            else:
                i += 1
        return dna


def process_dna(input_dna):
    if input_dna[0] == 'm':
        mrkrabs = MrKrabs()
        return mrkrabs.process(input_dna)
    elif input_dna[0] == 's' and not input_dna[0:2] == 'sb':
        squidward = Squidward()
        return squidward.process(input_dna)
    elif input_dna[0:2] == 'sb':
        spongebob = SpongeBob()
        return spongebob.process(input_dna)
    elif input_dna[::-1][0] == 'm':
        mrkrabs = MrKrabs()
        return mrkrabs.process(input_dna[::-1])
    elif input_dna[::-1][0] == 's' and not input_dna[::-1][0:2] == 'sb':
        squidward = Squidward()
        return squidward.process(input_dna[::-1])
    elif input_dna[::-1][0:2] == 'sb':
        spongebob = SpongeBob()
        return spongebob.process(input_dna[::-1])
    else:
        return 'invalid input'


DNA = input()
result = process_dna(DNA)
print(result)
