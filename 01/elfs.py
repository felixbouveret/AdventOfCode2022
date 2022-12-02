import glob


class Elfs:
    elfs: list[int] = []

    def __init__(self, inputPath: str):
        self.elfs = self.formatElfsInput(inputPath)

    def formatElfsInput(self, inputPath: str) -> list[int]:
        elfs = []
        for infile in glob.glob(inputPath):
            file = open(infile, 'r').read()
            for elf in file.split('\n\n'):
                elfs.append(
                    sum(list(map(int, list(filter(lambda x: x, elf.split('\n')))))))
        return sorted(elfs)

    def getElfs(self) -> list[int]:
        return self.elfs

    def getBiggestElf(self) -> int:
        return max(self.elfs)

    def getTopThreeElfsAmount(self) -> int:
        return sum(self.elfs[-3:])
