DNA = input()


class MrKrabs:
    def process(self):
        dna = DNA + DNA[0:10]
        dna = dna.replace('tt', 'o')

        return dna


class SpongeBob(MrKrabs):
    def process(self):
        sorted_length = sorted(str(len(super().process())))
        sorted_length_str = ''.join(sorted_length)
        return int(sorted_length_str)


class Squidward:
    def process(self):
        index = DNA.find('x')
        if index != -1:
            dna = DNA + str(index)
        else:
            dna = DNA

        i = 0
        while i + 2 < len(dna):
            if dna[i] == dna[i + 1] == dna[i + 2]:
                dna = dna.replace(dna[i:i + 3], '(0_0)')
            else:
                i += 1

        return dna


if DNA[0] == 'm':
    mrkrabsdna = MrKrabs()
    print(mrkrabsdna.process())
elif DNA[0] == 's' and not DNA[0:2] == 'sb':
    squidwarddna = Squidward()
    print(squidwarddna.process())
elif DNA[0:2] == 'sb':
    spongebobdna = SpongeBob()
    print(spongebobdna.process())
elif DNA[::-1][0] == 'm':
    DNA = DNA[::-1]
    mrkrabsdna = MrKrabs()
    print(mrkrabsdna.process())
elif DNA[::-1][0] == 's' and not DNA[::-1][0:2] == 'sb':
    DNA = DNA[::-1]
    squidwarddna = Squidward()
    print(squidwarddna.process())
elif DNA[::-1][0:2] == 'sb':
    DNA = DNA[::-1]
    spongebobdna = SpongeBob()
    print(spongebobdna.process())
else:
    print('invalid input')