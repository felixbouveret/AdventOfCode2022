import glob


class Rucksack:
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data = []

    def __init__(self, inputPath: str):
        self.strategy_guide = self.formatInput(inputPath)

    def formatInput(self, inputPath: str) -> list[list[str]]:
        with open(inputPath, "r") as myfile:
            self.data = myfile.read().splitlines()

    def getRucksacks(self) -> list[str]:
        return self.data

    def splitRucksack(self, rucksack) -> list[str]:
        return [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]

    def getItemImportanceNumber(self, item: str) -> int:
        return self.alphabet.index(item) + 1

    def getTotalImportanceNumber(self) -> int:
        importantItems = []
        splitedRucksack = list(
            map(self.splitRucksack, self.data))
        for rucksack in splitedRucksack:
            for item in rucksack[0]:
                if item in rucksack[1]:
                    importantItems.append(item)
                    break

        importanceNumber = 0
        for item in importantItems:
            importanceNumber += self.getItemImportanceNumber(item)
        return importanceNumber

    def getTotalImportanceNumberGroupes(self) -> int:
        importantItems = []
        splitedSize = 3
        groupes = [self.data[x:x+splitedSize]
                   for x in range(0, len(self.data), splitedSize)]

        for groupe in groupes:
            member1 = groupe[0]
            for item in member1:
                if item in groupe[1] and item in groupe[2]:
                    importantItems.append(item)
                    break

        importanceNumber = 0
        for item in importantItems:
            importanceNumber += self.getItemImportanceNumber(item)
        return importanceNumber


rpcIntance = Rucksack('./03/input.txt')
print(rpcIntance.getTotalImportanceNumber())
print(rpcIntance.getTotalImportanceNumberGroupes())
